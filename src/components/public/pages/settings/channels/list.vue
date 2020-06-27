<template>
  <v-card  max-width="100%" class="list-tracks" >
    <v-toolbar color="light-blue" dark>
      <v-toolbar-title> <v-icon >mdi-current-ac</v-icon> Channels Input</v-toolbar-title>
      <v-spacer></v-spacer>
        <v-menu bottom left>
          <template v-slot:activator="{ on }">
            <v-btn dark icon v-on="on" >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item>
              <v-list-item-title @click="goto_channel('setting-channel-analog-input')">New Analog</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="goto_channel()">New Consult</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="goto_channel('setting-channel-obd-input')">New OBDII</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
    </v-toolbar>
    <v-list two-line subheader class="overflow-y-auto">
      <v-list-item v-for="item in items" :key="item.title" @click="set_channel(item)" >
        <v-list-item-avatar>
          <v-icon
            :class="[item.iconClass]"
            v-text="item.icon"
          ></v-icon>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title v-text="item.title"></v-list-item-title>
          <v-list-item-subtitle v-text="item.subtitle"></v-list-item-subtitle>
        </v-list-item-content>
          <v-list-item-action>
            <v-list-item-action-text v-text="item.left"></v-list-item-action-text>
          </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script>
  export default {
    data: () => ({
      items: [],
    }),
    mounted(){
      this.set_list();
    },
    methods:{
        set_list(){
          this.axios.get("/settings/channels/input").then(result => {
            result.data.channels.map(channel => {
              if(channel.analog_input_id){
                this.items.push({type: 0, icon: 'mdi-current-ac', iconClass: 'blue white--text', title: channel[3], subtitle: "Analog | 5V Messure: "+(channel[5] == 1 ? "Voltage" : "Resistance"), left: "Pin: "+channel[4], channel: channel})
              }else if(channel.obd_input_id){
                var input = result.data.obd_inputs.find(obd => channel.obd_input_id == obd.id)
                var obd = result.data.obds.find(obd => input.obd_id == obd.id)
                this.items.push({type: 1, icon: 'mdi-chip', iconClass: 'blue white--text', title: channel[3], subtitle: input.name+" | Description: "+obd.description, left: "Command: "+obd.name, channel: channel})
              }
            })
          }).catch(error => {
            console.log(error);
          })
        },
        set_channel(channel){
          this.$router.push({ name: "setting-channel-analog-input", params: { analog: {id: channel.channel[1], pin: channel.channel[4], input: (channel.channel[5] == 1 ? "Voltage" : "Resistance"), name: channel.channel[3]}}});
        },
        goto_channel(path){
          this.$router.push({ name: path});
        }
    }
  }
</script>
<style scoped>
	.v-list{
		height: 361px;
	}
</style>