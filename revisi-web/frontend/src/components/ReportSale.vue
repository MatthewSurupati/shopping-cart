<template>
  <h3>Report Sale</h3>
  <div class="table-section">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">No Invoice</th>
          <th scope="col">Total</th>
          <th scope="col">Tanggal</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="report in reports">
          <td style="line-height: 20px">{{report.no_invoice}}</td>
          <td>{{report.total_harga}}</td>
          <td>{{report.tanggal}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ReportSale",
  // props: ['reports'],
  data(){
    return {
      reports:[],
    }
  },
  methods:{
    getInvoice(){
      axios.get('http://127.0.0.1:5000/get-invoice', {
        method: 'get',
      })
      .then((response) => {this.reports = response.data})
      .catch(function (error){
        console.log(error)
      })
    },
  },
  created() {
    this.getInvoice()
  }
}
</script>

<style scoped>
h3 {
  display: flex;
  padding-left: 15px;
  margin: 30px 0 0;
  align-items: flex-start;
  font-weight: 500px;
}
table thead tr th{
  padding-right: 25px;
}
</style>