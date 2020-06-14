<template>
  <v-card  max-width="100%" class="list-tracks" >
    <v-toolbar color="light-blue" dark>
      <v-toolbar-title> <v-icon >mdi-alert</v-icon> Alerts</v-toolbar-title>
      <v-spacer></v-spacer>
        <v-menu bottom left>
          <template v-slot:activator="{ on }">
            <v-btn dark icon v-on="on" >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item>
              <v-list-item-title @click="goto_form()">New Alert</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
    </v-toolbar>
    <v-list two-line subheader class="overflow-y-auto">
      <v-list-item v-for="item in items" :key="item.title" @click="set_channel(item.alarm)" >
        <v-list-item-avatar>
          <v-icon
            :class="[item.iconClass]"
            v-text="item.icon"
          ></v-icon>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title v-text="item.alarm.name"></v-list-item-title>
          <v-list-item-subtitle v-text="item.alarm_type.name + ' | ' + item.alarm.description"></v-list-item-subtitle>
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
          this.axios.get("/settings/alarms").then(result => {
            result.data.alarms.map(alarm => {
              let alarm_type = result.data.alarm_types.find(filter => filter.id == alarm.alarm_type_id) 
              this.items.push({icon: 'mdi-alert', iconClass: 'blue white--text', alarm: alarm, alarm_type: alarm_type})
            })
          }).catch(error => {
            console.log(error);
          })
        },
        set_channel(alarm){
          this.$router.push({ name: "setting-alert-form", params: {alarm: alarm}});
        },
        goto_form(){
          this.$router.push({ name: "setting-alert-form"});
        }
    }
  }
</script>
<style scoped>
	.v-list{
		height: 361px;
	}
</style>