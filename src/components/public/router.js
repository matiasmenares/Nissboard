import GraphRpm from './pages/graphs/rpm.vue';
import DashboarCuga from './pages/dashboards/cuga.vue';
import DashboarKinek from './pages/dashboards/kinek.vue';
import DashboarRocket from './pages/dashboards/rocket.vue';
import DashboarBlume from './pages/dashboards/blume.vue';
import DashboarDust from './pages/dashboards/dust.vue';
import SettingDashboard from './pages/settings/dashboard.vue';

export const PublicRoutes =
  [
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
      path: '/',
      component: DashboarKinek,
      name: 'dashboard-kinek',
    },
    {
      path: '/settings/dashboard',
      component: SettingDashboard,
      name: 'setting-dashboard',
    },
  ];
