<template>
  <div class="categories-section">
    <h3>CATEGORIES</h3>
    <div class="thecategories" >
<!--      <div @click="filterCategory({cat})"><span>{{cat}}</span></div>-->
      <div @click="filterCategory('Nasi')"><span>Nasi</span></div>
      <div @click="filterCategory('Minuman Tradisional')"><span>Minuman Tradisional</span></div>
      <div @click="filterCategory('Jajanan')"><span>Jajanan</span></div>
      <div @click="filterCategory('Semua')"><span>All</span></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Categories",
  props:['kategori'],
  data(){
    return{

    }
  },
  methods:{
    filterCategory(kategori){
      return this.$emit('filtrasi', kategori)
    }
  }
}
</script>

<style scoped>
.categories-section{
  text-align: left;
}
h3 {
  margin: 10px 20px;
  text-align: left;
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

.thecategories{
  display: flex;
  margin: 20px;
}

.thecategories{
  margin-top: 0px;
}
.thecategories span{
  margin: 0px 20px;
  padding: 20px;
}
span{
  background-color: #6D3399;
  border-radius:5px;
  text-align: left;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);
}

span:hover{
  background-color: rgba(19, 19, 19, 0.94)
}
.material-symbols-outlined{
  color: white;
}
</style>