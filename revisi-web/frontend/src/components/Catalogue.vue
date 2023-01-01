<template>
  <div class="catalofue-section">
    <div v-for="(item, index) in items">
      <div class="gallery">
        <img :src="item.photo" alt="" style="width: 100px; height: 100px; align-self: center">
        <span style="font-weight: bold">{{item.nama_barang}}</span>
        <p class="price">Rp.{{item.harga}}</p>
        <button type="submit" class="butt" @click="getItem(index)">add</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Catalogue",
  props: ['items'],

  data(){
    return{
      groups: [],
    }
  },
  methods:{
    getItem(index){
      this.selectedIndex = index
      let product = this.items[this.selectedIndex]
      this.$emit('addItem', product)
    },
    // getImage(){
    //   const path = "http://127.0.0.1:5000/get-barang";
    //   axios.get(path)
    //   .then((response) => {
    //     let group = [];
    //     response.data.forEach(function (obj){
    //       obj.photo = "http://127.0.0.1:5000/" + obj.photo;
    //       // console.log(obj.photo)
    //       group.push(obj)
    //     });
    //     this.groups = group
    //   })
    // }
  },
  computed:{
    getSelectedIndex(){
      return this.getIndex(index)
    },
    // imagePath(){
    //   // '../assets/'+item.photo
    //   // console.log(`../assets/${this.items.photo}`)
    //   return `../assets/${this.items.photo}`
    // }
  },
  // created() {
  //   this.getImage()
  // },
  emits: ['addItem']
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
p{
  /* position: absolute; */
  color: white;
  padding-top: 5px;
  margin-top: 10px;
  /* padding: 60px 65px; */
  font-weight: 300;
  background-color:#941304;
}
a {
  color: #42b983;
}
.catalogue-section {
  max-height: 60vh;
  /* border-bottom: 0.5px solid grey; */
  padding: 20px;
  overflow-y:scroll;
}
.gallery{
 background-color: #941304;
 padding: 10px;
 margin: 20px 20px;
 float: left;
 width: 180px;
 height: 180px;
 display: flex;
 flex-direction: column;

}

.gallery span{
  margin: auto;
  color: white;
  background-color:#941304;
}
.gallery .butt{
  border-radius: 20px;
  width: 35%;
  margin-left: 33%;
  margin-bottom: 20px;
  border: hidden;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);
  padding-top: 0px;
}
.butt:hover{
  background-color: rgba(255, 43, 15, 0.747);
  color:white;
  border:hidden
}

</style>