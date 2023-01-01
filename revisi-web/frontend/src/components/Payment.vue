<template>
  <div>
        <div class="container">
            <div class="left">
                <div class="left-header">

                    <div>
                        <p><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                                class="bi bi-person-circle" viewBox="0 0 16 16">
                                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
                                <path fill-rule="evenodd"
                                    d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z" />
                            </svg> user </p>
                    </div>

                    <div>
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor"
                            class="bi bi-box-arrow-right" viewBox="0 0 16 16">
                            <path fill-rule="evenodd"
                                d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z" />
                            <path fill-rule="evenodd"
                                d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z" />
                        </svg>
                    </div>
                </div>
                <h2>Payment</h2>
                <div class="box">
                    <label>Name: </label> <input type="text"><br>
                    <p></p><br>
                    <label>Category: </label>
                    <select name="kategori">
                        <option value="Nasi">Nasi</option>
                        <option value="Minuman Tradisional">Minuman Tradisional</option>
                        <option value="Jajanan">Jajanan</option>
                    </select><br>
                    <p></p><br>
                    <label>Payment method: </label>
                    <select name="paymethod">
                        <option value="cash">Cash</option>
                        <option value="paypal">Paypal</option>
                        <option value="bca">BCA</option>
                        <option value="mandiri">Mandiri</option>
                    </select><br>
                </div>
                <button class="payviewbutton" @click="paySuccess">Pay</button>
            </div>
            <div class="right">
                <h2>Grand Total</h2>
                <div class="box">
                    <h1>{{ grandTotal }}</h1>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "Payment"
}
</script>

<style scoped>
input,
select {
    font-size: 18px;
    font-family: 'Poppins', sans-serif;
    border-radius: 20px;
    padding: 8px;
}

.payviewbutton {
    background-color: #05BD2D;
    font-weight: bold;
    font-size: 18px;
    border: none;
    color: white;
    padding: 12px 24px;
    border-radius: 20px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
}

.container {
    display: flex;
    width: 90%;
    margin: auto;
}

.left {
    width: 70%;
    height: 650px;
    border-right: 2px solid black;
    padding-right: 20px;
}

.box {
    background: linear-gradient(180deg, #F1F1F1 0%, #F1F1F1 80%, #ECE9E9 80%, #ECE9E9 100%);
    height: 250px;
    padding: 30px 20px;
    border-radius: 20px;
}

.right .box {
    line-height: 250px;
    height: 300px;
    text-align: center;
}

.right .box h1 {
    font-size: 50px;
}

.right {
    width: 30%;
    padding-left: 20px;
}

.left-header {
    display: flex;
    justify-content: space-between;
    width: 100%;
}
</style>