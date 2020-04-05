<template>
  <v-card  max-width="100%" class="list-tracks" >
    <v-toolbar color="light-blue" dark>
      <v-toolbar-title> <v-icon >mdi-go-kart-track</v-icon> Tracks</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-view-module</v-icon>
      </v-btn>
    </v-toolbar>
    <v-list two-line subheader>
      <v-subheader inset>Circuit</v-subheader>
      <v-list-item v-for="item in items2" :key="item.title" @click="set_map(item.center)" >
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
          <v-btn icon>
            <v-icon color="grey lighten-1"> go-kart-track</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script>
  export default {
    data: () => ({
      items2: [
        { icon: 'mdi-go-kart-track', iconClass: 'blue white--text', title: 'AIC Codegua', subtitle: 'Codegua - Chile', center: [-70.6327262, -34.0382532]},
        { icon: 'mdi-go-kart-track', iconClass: 'blue white--text', title: 'Las Vizcachas', subtitle: 'Santiago - Chile', center: [-70.522903, -33.602304]},
        { icon: 'mdi-go-kart-track', iconClass: 'blue white--text', title: 'Autodromo de San antonio', subtitle: 'San antonio - Chile', center: [-71.5602362, -33.6648926] },
        { icon: 'mdi-go-kart-track', iconClass: 'blue white--text', title: 'Interlomas', subtitle: 'Lautaro - Chile', center: [-72.4689791,-38.6204621] },
        { icon: 'mdi-go-kart-track', iconClass: 'blue white--text', title: 'Huachalalume', subtitle: 'Huachalalume - Chile', center: [-71.2197329, -29.9823882] },

      ],
    }),
    methods:{
        set_map(center){
            this.$router.push({ name: "track-map", params: { center: center}});
        }
    }
  }
</script>
<style scoped>
.list-tracks{
}
</style>