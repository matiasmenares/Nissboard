<template>
  <v-card  max-width="100%" class="list-tracks" >
    <v-toolbar color="light-blue" dark>
      <v-toolbar-title> <v-icon >mdi-led-on</v-icon> LED's</v-toolbar-title>
      <v-spacer></v-spacer>
        <v-menu bottom left>
          <template v-slot:activator="{ on }">
            <v-btn dark icon v-on="on" >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item>
              <v-list-item-title @click="goto_form()">New LED</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
    </v-toolbar>
    <v-list two-line subheader class="overflow-y-auto">
      <v-list-item v-for="item in items" :key="item.title" @click="go_to_alert(item.led)" >
        <v-list-item-avatar>
          <v-icon
            :class="[item.iconClass]"
            v-text="item.icon"
          ></v-icon>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title v-text="item.led.name"></v-list-item-title>
          <v-list-item-subtitle v-text="'Priority: '+item.led.priority + ' | Brigness: ' + item.led.brightness"></v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script>
  export default {
    data: () => ({
      items: [],
      led_outputs: []
    }),
    mounted(){
      this.set_list();
    },
    methods:{
        set_list(){
          this.axios.get("/settings/leds").then(result => {
            this.led_outputs = result.data.led_outputs
            result.data.leds.map(led => {
              let led_outputs = this.led_outputs.filter(output => output.led_id == led.id)
              this.items.push({icon: 'mdi-led-on', iconClass: 'blue white--text', led: led, led_outputs: led_outputs})
            })
          }).catch(error => {
            console.log(error);
          })
        },
        go_to_alert(alarm){
          let alarm_outputs = this.alarm_outputs.filter(output => output.alarm_id == alarm.id)
          this.$router.push({ name: "setting-leds-form", params: {alarm: alarm, alarm_outputs: alarm_outputs}});
        },
        goto_form(){
          this.$router.push({ name: "setting-leds-form"});
        }
    }
  }
</script>
<style scoped>
	.v-list{
		height: 361px;
	}
</style>