import GraphRpm from './pages/graphs/rpm.vue';
import DashboarCuga from './pages/dashboards/cuga.vue';
import DashboarKinek from './pages/dashboards/kinek.vue';
import DashboarRocket from './pages/dashboards/rocket.vue';
import DashboarBlume from './pages/dashboards/blume.vue';
import SettingMain from './pages/settings/setting.vue';

export const PublicRoutes =
  [
    {
      path: '/',
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
      path: '/graph/rpm',
      component: GraphRpm,
      name: 'graph-rpm',
    },
    {
      path: '/dashboard/kinek',
      component: DashboarKinek,
      name: 'dashboard-kinek',
    },
    {
      path: '/settings/setting',
      component: SettingMain,
      name: 'setting-main',
    },
  ];
