<template>
  <div class="side-container">
    <div id="left">
      <HeaderInvoice invoiceInfo="10.252.234.132" date="13/12/2022"></HeaderInvoice>
      <BodyInvoice :details="details"></BodyInvoice>
      <UserCommand :clearAll="clearAll" :addInvoice="addInvoice"></UserCommand>
    </div>
    <div class="v1"></div>
    <div id="right">
      <Categories @filtrasi="filtrasi"></Categories>
      <Catalogue :items="filtrasi(selectedKategori)" @addItem="addItems"></Catalogue>
      <div id="admin-commands">
        <router-link to="/report">Report Sale</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import BodyInvoice from "./BodyInvoice.vue";
import Catalogue from "./Catalogue.vue";
import Categories from "./Categories.vue";
import UserCommand from "./UserCommand.vue";
import HeaderInvoice from "./HeaderInvoice.vue";

export default {
  name: "Home",
  components: {
    BodyInvoice,
    Catalogue,
    Categories,
    UserCommand,
    HeaderInvoice
  },
  data(){
    return{
      details: [],
      items: [],
      kategori: [],
      selectedKategori: "Semua"
    }
  },
  methods: {
    // unique(item){
    //   if(this.kategori.indexOf(item) === -1){
    //     this.kategori.push(item);
    //   } else {
    //
    //   }
    // },
    getImage(){
      const path = "http://127.0.0.1:5000/get-barang";
      axios.get(path)
      .then((response) => {
        let group = [];
        let cat = []
        response.data.forEach(function (obj){
          obj.photo = "http://127.0.0.1:5000/" + obj.photo;
          // console.log(obj.photo)
          // if(this.cat.indexOf(obj.kategori) === -1){
          //   cat.push(obj.kategori)
          // }
          group.push(obj)
        });
        this.items = group
        // this.kategori = cat
      })
    },
    // getItem(){
    //   fetch('http://127.0.0.1:5000/get-barang', {
    //     method: 'get',
    //     headers:{
    //       'Content-Type':'application/json'
    //     }
    //   })
    //   .then(resp => resp.json())
    //   .then(data => {
    //     // console.log(data)
    //     // this.kategori.push(data.kategori_barang);
    //     this.items.push(...data);
    //   })
    //   .catch(error => {
    //     console.log(error)
    //   })
    // },
    addItems(product){
      let alreadyin = this.details.map(alreadyitem => alreadyitem.nama_barang)
      let uniquename = [...new Set(alreadyin)];
      let addnew = uniquename.indexOf(product.nama_barang) > -1

      if(!addnew){
        this.details.push({
          nama_barang: product.nama_barang,
          qty:1,
          harga: product.harga
        })
      } else{
        let indexBarang = this.details.findIndex((obj => obj.nama_barang == product.nama_barang))
        this.details[indexBarang].qty += 1
      }
    },
    clearAll(){
      this.details = []
    },
    filtrasi(kategori){
      this.selectedKategori = kategori
      if (kategori == 'Semua'){
        return this.items
      } else {
        return this.items.filter(e => e.kategori_barang == kategori)
      }
    },
    addInvoice(){
      console.log(this.details)
      let total = 0
      for (let i = 0; i < this.details.length; i++){
        total += parseFloat(this.details[i].harga) * parseFloat(this.details[i].qty)
      }
      const summary = total
      const data = {
        "total_harga": summary,
      }
      if (summary > 0){
        this.clearAll()
        axios.post('http://127.0.0.1:5000/add-invoice', data)
        .then(res => {
          return res;
        })
      } else {
        this.clearAll()
      }
    },
  },
  created() {
    this.getImage();
  },
}
</script>

<style scoped>
*{
  background-color: black;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}

.side-container {
  display: flex;
  width: 100%;
}

#left {
  width: 430px;
  height: 100vh;
}

#right {
  /* background-color: #2c3e50; */
  width: 100%;
  height: 100vh;
}

.profile {
  display: flex;
  gap: 5px
}

.user {
  display: flex;
  justify-content: space-between;
  padding: 15px;
}

.invoice-info {
  text-align: left;
  margin-top: 20px;
}

.v1 {
  border-right: 1px solid antiquewhite;
  height: 600px;
  margin-top: 30px;
}

.invoice-info td {
  padding-left: 15px;
}

.v2 {
  border-bottom: 1px solid rgb(119, 119, 119);
  width: 90%;
  margin-left: 30px;
}
</style>