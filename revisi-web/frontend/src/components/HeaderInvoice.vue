<template>
  <div id="header-invoice">
    <div class="invoice-invo">
      <table>
        <tr>
          <td>Invoice: {{Invoice}}</td>
          <td>{{invoiceInfo}}</td>
        </tr>
        <tr>
          <td>Date</td>
          <td>{{currentDate()}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "HeaderInvoice",
  props:{
    invoiceInfo: String,
    date: String
  },
  data(){
    return{
      date: "",
      invoiceInfo: "",
      Invoice: 1
    }
  },
  methods:{
    currentDate(){
      const current = new Date()
      const date = `${current.getDate()}/${current.getMonth()}/${current.getFullYear()}`
      return this.date
    }
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
tr{
  width: 10px;
}
</style>