<template>
  <v-card  max-width="100%" class="list-tracks" >
    <v-toolbar color="light-blue" dark>
      <v-toolbar-title> <v-icon >mdi-current-ac</v-icon> Channels Output</v-toolbar-title>
      <v-spacer></v-spacer>
        <v-menu bottom left>
          <template v-slot:activator="{ on }">
            <v-btn dark icon v-on="on" >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item>
              <v-list-item-title @click="goto_form()">New Analog</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="goto_form()">New Consult</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="goto_form()">New OBDII</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title @click="goto_form()">New CAN</v-list-item-title>
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
          <v-list-item-title v-text="item.name"></v-list-item-title>
          <v-list-item-subtitle v-text="item.subtitle + ' | ' + item.messure"></v-list-item-subtitle>
        </v-list-item-content>
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
          this.axios.get("/settings/channels/output").then(result => {
            result.data.channels.map(channel => {
              this.items.push({icon: 'mdi-current-ac', iconClass: 'blue white--text', messure: "Messure: "+(channel[5] == 1 ? "Voltage" : "Resistance"), title: channel[3], subtitle: channel.name, pin: "Pin: "+channel[4], channel: channel})
            })
          }).catch(error => {
            console.log(error);
          })
        },
        set_channel(channel){
          this.$router.push({ name: "setting-channel-analog-input", params: { analog: {id: channel.channel[1], pin: channel.channel[4], input: (channel.channel[5] == 1 ? "Voltage" : "Resistance"), name: channel.channel[3]}}});
        },
        goto_form(){
          this.$router.push({ name: "setting-channel-output-form"});
        }
    }
  }
</script>
<style scoped>
	.v-list{
		height: 361px;
	}
</style>