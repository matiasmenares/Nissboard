//Graph
import GraphRpm from './pages/graphs/rpm.vue';
//Dashboard
import DashboarCuga from './pages/dashboards/cuga.vue';
import DashboarKinek from './pages/dashboards/kinek.vue';
import DashboarRocket from './pages/dashboards/rocket.vue';
import DashboarBlume from './pages/dashboards/blume.vue';
import DashboarDust from './pages/dashboards/dust.vue';
import DashboarInit from './pages/dashboards/init.vue';
//Setting
import SettingDashboard from './pages/settings/dashboard.vue';
import SettingAlert from './pages/settings/alert.vue';
//G-force
import GforceGforce from './pages/g-force/gforce.vue';

export const PublicRoutes =
  [
    {
      path: '/',
      component: DashboarKinek,
      name: 'dashboard-kinek',
    },
    {
      path: '/g-force/gforce',
      component: GforceGforce,
      name: 'g-force-gforce',
    },
    {
      path: '/dashboard/cuga',
      component: DashboarCuga,
      name: 'dashboard-cuga',
    },
    {
      path: '/dashboard/rocket',
      component: DashboarRocket,
      name: 'dashboard-rocket',
    },
    {
      path: '/dashboard/init',
      component: DashboarInit,
      name: 'dashboard-init',
    },
    {
      path: '/dashboard/blume',
      component: DashboarBlume,
      name: 'dashboard-blume',
    },
    {
      path: '/dashboard/dust',
      component: DashboarDust,
      name: 'dashboard-dust',
    },
    {
      path: '/graph/rpm',
      component: GraphRpm,
      name: 'graph-rpm',
    },
    {
      path: '/settings/dashboard',
      component: SettingDashboard,
      name: 'setting-dashboard',
    },
    {
      path: '/settings/alert',
      component: SettingAlert,
      name: 'setting-alert',
    },
  ];
