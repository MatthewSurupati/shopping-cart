<template>
  <div class="buttons">
<!--    <button type="button" class="payment" @click="/payment">Pay</button>-->
    <button type="button" class="payment" @click="addInvoice">Pay</button>
    <button type="button" class="cancel" @click="clearAll">Cancel</button>
  </div>
</template>

<script>
export default {
  name: "UserCommand",
  props:['clearAll', 'addInvoice']
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
.buttons{
  display: flex;
  justify-content: space-around;
  padding-top:40px;
  padding-right:10px ;
}

button{
  /*border-radius: 30px;*/
  padding: 12px;
  font-size: 14px;
}
.payment{
  background-color: #198754;
  color: white;
  border: hidden;
  width: 100px;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);
}

.cancel{
  background-color: #a52834;
  color: antiquewhite;
  border: hidden;
  width: 100px;
  box-shadow: 0 5px 10px 0 rgba(0,0,0,.5);

}
btn-success{
  --bs-btn-color:#fff;
  --bs-btn-bg:#198754;
  --bs-btn-border-color:#198754;
  --bs-btn-hover-color:#fff;
  --bs-btn-hover-bg:#157347;
  --bs-btn-hover-border-color:#146c43;
  --bs-btn-focus-shadow-rgb:60,153,110;
  --bs-btn-active-color:#fff;
  --bs-btn-active-bg:#146c43;
  --bs-btn-active-border-color:#13653f;
  --bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);
  --bs-btn-disabled-color:#fff;
  --bs-btn-disabled-bg:#198754;
  --bs-btn-disabled-border-color:#198754
}

btn-danger{
  --bs-btn-color:#fff;
  --bs-btn-bg:#dc3545;
  --bs-btn-border-color:#dc3545;
  --bs-btn-hover-color:#fff;
  --bs-btn-hover-bg:#bb2d3b;
  --bs-btn-hover-border-color:#b02a37;
  --bs-btn-focus-shadow-rgb:225,83,97;
  --bs-btn-active-color:#fff;
  --bs-btn-active-bg:#b02a37;
  --bs-btn-active-border-color:#a52834;
  --bs-btn-active-shadow:inset 0 3px 5px rgba(0, 0, 0, 0.125);
  --bs-btn-disabled-color:#fff;
  --bs-btn-disabled-bg:#dc3545;
  --bs-btn-disabled-border-color:#dc3545
}
</style>