from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/webproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Barang(db.Model):
    no_barang = db.Column(db.Integer(), primary_key = True)
    nama_barang = db.Column(db.String(100))
    kategori_barang = db.Column(db.String(100))
    harga = db.Column(db.Integer())
    photo = db.Column(db.String(100))

    def __init__(self, nama_barang, kategori_barang, harga, photo):
        self.nama_barang = nama_barang
        self.kategori_barang = kategori_barang
        self.harga = harga
        self.photo = photo

class Invoice(db.Model):
    no_invoice = db.Column(db.Integer(), primary_key = True)
    tanggal = db.Column(db.DateTime, default=datetime.datetime.now())
    # nama_barang = db.Column(db.String(100))
    # qty = db.Column(db.String(100))
    total_harga = db.Column(db.String(100))

    def __init__(self, total_harga):
        # self.nama_barang = nama_barang
        # self.qty = qty
        self.total_harga = total_harga

class BarangSchema(ma.Schema):
    class Meta:
        fields = ('no_barang', 'nama_barang', 'kategori_barang', 'harga', 'photo')

class InvoiceSchema(ma.Schema):
    class Meta:
        fields = ('no_invoice', 'tanggal', 'total_harga')

barang_schema = BarangSchema()
barangs_schema = BarangSchema(many=True)
invoice_schema = InvoiceSchema()
invoices_schema = InvoiceSchema(many=True)

#Get All Data
@app.route('/get-barang', methods = ['get'])
def get_barang():
    all_barang = Barang.query.all()
    results = barangs_schema.dump(all_barang)
    return jsonify(results)

@app.route('/get-invoice', methods = ['get'])
def get_invoice():
    all_invoice = Invoice.query.all()
    resutls = invoices_schema.dump(all_invoice)
    return jsonify(resutls)

#Add Data
@app.route('/add-barang', methods = ['post'])
def add_barang():
    nama_barang = request.json['nama_barang']
    kategori_barang = request.json['kategori_barang']
    harga = request.json['harga']
    photo = request.json['photo']

    barang = Barang(nama_barang, kategori_barang, harga, photo)
    db.session.add(barang)
    db.session.commit()
    return barang_schema.jsonify(barang)


@app.route('/add-invoice', methods=['post'])
def add_invoice():
    # nama_barang = request.json['nama_barang']
    # qty = request.json['qty']
    total_harga = request.json['total_harga']

    invoice = Invoice(total_harga)
    db.session.add(invoice)
    db.session.commit()
    return barang_schema.jsonify(invoice)

#Get By Kategori
@app.route('/get-barang/<kategori_barang>', methods = ['get'])
def get_barang_kategori(kategori_barang):
    barang = Barang.query.get(kategori_barang)
    return barang_schema.jsonify(barang)

@app.route('/get-invoice/<no_invoice>', methods = ['get'])
def get_invoice_id(no_invoice):
    invoice = Invoice.query.get(no_invoice)
    return invoice_schema.jsonify(invoice)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTO_DEST'] = os.path.join(APP_ROOT, 'images')

@app.route('/static/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

if __name__ == '__main__':
    app.run(debug=True)