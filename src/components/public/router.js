//Graph
import GraphRpm from './pages/graphs/rpm.vue';
import GraphGforce from './pages/graphs/g-force.vue';
//Dashboard
import DashboarCuga from './pages/dashboards/cuga.vue';
import DashboarKinek from './pages/dashboards/kinek.vue';
import DashboarRocket from './pages/dashboards/rocket.vue';
import DashboarBlume from './pages/dashboards/blume.vue';
import DashboarDust from './pages/dashboards/dust.vue';
import DashboarInit from './pages/dashboards/init.vue';
import DashboarProton from './pages/dashboards/proton.vue';
import DashboarNebula from './pages/dashboards/nebula.vue';

//Setting
import SettingDashboard from './pages/settings/dashboard.vue';
import SettingAlert from './pages/settings/alert.vue';
import SettingChannelAnalogInput from './pages/settings/channels/analogs/input.vue';
import SettingChannelList from './pages/settings/channels/list.vue';
import SettingChannelOutputList from './pages/settings/channels/output/list.vue';
import SettingChannelOutputForm from './pages/settings/channels/output/form.vue';
import SettingScreen from './pages/settings/screen.vue';

//G-force
import GforceGforce from './pages/g-force/gforce.vue';
//Map
import TrackMap from './pages/track/map.vue';
import TrackList from './pages/track/list.vue';


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
      path: '/dashboard/proton',
      component: DashboarProton,
      name: 'dashboard-proton',
    },
    {
      path: '/track/map',
      component: TrackMap,
      name: 'track-map',
      props: true
    },
    {
      path: '/track/list',
      component: TrackList,
      name: 'track-list',
    },
    {
      path: '/dashboard/blume',
      component: DashboarBlume,
      name: 'dashboard-blume',
    },
    {
      path: '/dashboard/nebula',
      component: DashboarNebula,
      name: 'dashboard-nebula',
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
      path: '/graph/g-force',
      component: GraphGforce,
      name: 'graph-gforce',
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
    {
      path: '/settings/screen',
      component: SettingScreen,
      name: 'setting-screen',
    },
    {
      path: '/settings/channels/analogs/input',
      component: SettingChannelAnalogInput,
      name: 'setting-channel-analog-input',
      props: true
    },
    {
      path: '/settings/channels/list',
      component: SettingChannelList,
      name: 'setting-channel-list',
    },
    {
      path: '/settings/channels/output/list',
      component: SettingChannelOutputList,
      name: 'setting-channel-output-list',
    },
    {
      path: '/settings/channels/output/form',
      component: SettingChannelOutputForm,
      name: 'setting-channel-output-form',
    },
  ];
