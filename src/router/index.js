import Vue from 'vue';
import Router from 'vue-router';

/* Components */
import Application from '../components/public/application';
import e404 from '../components/error/404'
/* Components */

/* Routes */
import {PublicRoutes} from '../components/public/router';
/* Routes */

Vue.use(Router);

export default new Router({
  mode: 'history',//esta linea se saca para compilar cordova
  routes: [
    {
      path: '/',
      component: Application,
      children: PublicRoutes,
    },
    {
      path: '/404',
      component: e404
    }
  ]
})
