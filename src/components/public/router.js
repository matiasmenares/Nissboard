import Index from './pages/index.vue';
import GraphRpm from './pages/graphs/rpm.vue';

export const PublicRoutes =
  [
    {
      path: '/',
      component: Index,
      name: 'index',
    },
    {
      path: '/graph/rpm',
      component: GraphRpm,
      name: 'graph-rpm',
    }
  ];
