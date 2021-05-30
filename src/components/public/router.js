//Graph
import GraphRpm from './pages/graphs/rpm.vue';
import GraphGforce from './pages/graphs/g-force.vue';
import GraphChannel from './pages/graphs/channel.vue';
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
import SettingAlertList from './pages/settings/alerts/list.vue';
import SettingAlertForm from './pages/settings/alerts/form.vue';
import SettingChannelAnalogInput from './pages/settings/channels/analogs/input.vue';
import SettingChannelOBDInput from './pages/settings/channels/obd/form.vue';
import SettingChannelConsultinput from './pages/settings/channels/consult/form.vue';
import SettingChannelList from './pages/settings/channels/list.vue';
import SettingChannelOutputList from './pages/settings/channels/output/list.vue';
import SettingChannelOutputAnalog from './pages/settings/channels/output/analog.vue';
import SettingChannelOutputOBD from './pages/settings/channels/output/obd.vue';
import SettingChannelOutputConsult from './pages/settings/channels/output/consult.vue';
import SettingLedsList from './pages/settings/leds/list.vue';
import SettingLedsForm from './pages/settings/leds/form.vue';
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
      path: '/graph/channel',
      component: GraphChannel,
      name: 'graph-channel',
    },
    {
      path: '/settings/dashboard',
      component: SettingDashboard,
      name: 'setting-dashboard',
    },
    {
      path: '/settings/alert/form',
      component: SettingAlertForm,
      name: 'setting-alert-form',
      props: true
    },
    {
      path: '/settings/alert/list',
      component: SettingAlertList,
      name: 'setting-alert-list',
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
      path: '/settings/channels/obd/input',
      component: SettingChannelOBDInput,
      name: 'setting-channel-obd-input',
      props: true
    },
    {
      path: '/settings/channels/consult/input',
      component: SettingChannelConsultinput,
      name: 'setting-channel-consult-input',
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
      path: '/settings/channels/output/analog',
      component: SettingChannelOutputAnalog,
      name: 'setting-channel-output-analog',
    },
    {
      path: '/settings/channels/output/obd',
      component: SettingChannelOutputOBD,
      name: 'setting-channel-output-obd',
    },
    {
      path: '/settings/channels/output/consult',
      component: SettingChannelOutputConsult,
      name: 'setting-channel-output-consult',
    },
    {
      path: '/settings/leds/list',
      component: SettingLedsList,
      name: 'setting-leds-list',
    },
    {
      path: '/settings/leds/form',
      component: SettingLedsForm,
      name: 'setting-leds-form',
    },
  ];
