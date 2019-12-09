<template>
    <v-alert prominent type="error" id="car-alert" dismissible>
      <v-row align="center">
        <v-col class="grow"><b>Alerta</b> Alta temperatura.</v-col>
        <v-col class="shrink">
        </v-col>
      </v-row>
    </v-alert>
</template>
<script>
  export default {
    name: 'Alerts',
    data(){
      return{

      }
    },
    mounted () {
      this.set_data()
    },
    methods:{
        set_data(){
            this.sockets.subscribe('ecuAlerts', (data) => {
                this.ecu = data;
            })
        }
    }
  }
</script>
<style scoped>
</style>
