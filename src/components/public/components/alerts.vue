<template>
    <v-alert :value="errorExists" v-if="this.$store.state.alert.type" prominent :type="this.$store.state.alert.type" border="top" id="car-alert" dismissible>
      <v-row align="center">
        <v-col class="grow"><b>Alerta</b> {{this.$store.state.alert.text}}</v-col>
        <v-col class="shrink">
        </v-col>
      </v-row>
    </v-alert>
</template>
<script>
  export default {
    name: 'Alerts',
    components:{
    },
    data(){
      return{
          alert: {type: null, text: ""},
          setting: true
      }
    },
    computed:{
      errorExists: function() {
        let value = this.$store.state.alert.type;
        if (value != undefined && value != null) {
          return true;
        } else {
         return false;
        }
      }
    },
    mounted () {
      this.set_data()
    },
    methods:{
        set_data(){
            this.sockets.subscribe('Alerts', (data) => {
                console.log(data)
                this.$store.dispatch('showAlert', {type: data.type , text: data.text}).then(() => {
                  return true
                })
            })
        }
    }
  }
</script>
<style scoped>
</style>
