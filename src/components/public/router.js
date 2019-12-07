import GraphRpm from './pages/graphs/rpm.vue';
import DashboarCuga from './pages/dashboards/cuga.vue';
import DashboarKinek from './pages/dashboards/kinek.vue';

export const PublicRoutes =
  [
    {
      path: '/',
      component: DashboarCuga,
      name: 'dashboard-cuga',
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
  ];
