import Vue from 'vue'
import App from './App.vue'
import router from './router';
import BootstrapVue from 'bootstrap-vue'
import VueAxios from "vue-axios";
import axios from "axios";
import VueSocketIO from 'vue-socket.io'
import VueSvgGauge from 'vue-svg-gauge'
import vuetify from '@/plugins/vuetify'
import HighchartsVue from 'highcharts-vue'

Vue.use(new VueSocketIO({
  connection: 'http://10.0.1.6:8090/',
}))

Vue.use(HighchartsVue)
Vue.use(VueSvgGauge)
Vue.use(BootstrapVue)

Vue.config.productionTip = false

Vue.router = router;
App.router = Vue.router;

const instance = axios.create({
  baseURL: "http://192.168.1.108:3000/api/v1/",
  params: {}
});
Vue.use(VueAxios, instance);

new Vue({
  render: h => h(App),
  vuetify,
  router
}).$mount('#app')
