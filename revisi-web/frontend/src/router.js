import {createRouter, createWebHistory} from 'vue-router'
import Home from "./components/Home.vue";
import ReportSale from "./components/ReportSale.vue";
import Payment from "./components/Payment.vue";

const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/report',
        name: 'report',
        component: ReportSale
    },
    {
        path: '/payment',
        name: 'payment',
        component: Payment
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router