import Vue from 'vue'
import App from './App.vue'
import router from './router';
import BootstrapVue from 'bootstrap-vue'
import VueAxios from "vue-axios";
import axios from "axios";
import VueSocketIO from 'vue-socket.io'
import VueSvgGauge from 'vue-svg-gauge'

Vue.use(new VueSocketIO({
  debug: true,
  connection: 'http://localhost:8090',
  vuex: {
      actionPrefix: 'SOCKET_',
      mutationPrefix: 'SOCKET_'
  },
}))
Vue.use(VueSvgGauge)
Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.router = router;
App.router = Vue.router;
const instance = axios.create({
  baseURL: "http://192.168.1.108:3000/api/v1/",
  params: {} // do not remove this, its added to add params later in the config
});
Vue.use(VueAxios, instance);

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
