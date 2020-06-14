<template>
	<div v-if="this.$store.state.alert.type">
		<v-dialog v-if="this.$store.state.alert.isModal" v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition" style="z-index: 1000">
			<v-card :color="this.$store.state.alert.type">
				<v-container class="vh-100">
					<v-toolbar flat dark color="transparent">
						<v-spacer></v-spacer>
						<v-toolbar-items>
							<v-btn dark text @click="dialog = false"><v-icon class="icon-lg">mdi-close</v-icon></v-btn>
						</v-toolbar-items>
					</v-toolbar>
					<v-row align="center" class=" text-center">
						<v-col cols="12">
							<v-icon class="icon-xl">mdi-alert-circle-outline</v-icon>
							<h1>{{this.$store.state.alert.text}}</h1>
						</v-col>
					</v-row>
				</v-container>
			</v-card>
		</v-dialog>
		<v-alert v-else :value="errorExists" prominent :type="this.$store.state.alert.type" border="top" id="car-alert" dismissible>
			<v-row align="center">
				<v-col class="grow"><b>Alerta</b> {{this.$store.state.alert.text}}</v-col>
				<v-col class="shrink"></v-col>
			</v-row>
		</v-alert>
	</div>
</template>
<script>
  export default {
    name: 'Alerts',
    components:{
    },
    data(){
		return{
			alert: {type: null, text: "", isModal: false},
			setting: true,
			dialog: false,
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
            this.sockets.subscribe('alert', (alert) => {
				if (alert.alarm_type_id == 1){
					this.$store.dispatch('showAlert', {type: "warning" , text: alert.description, isModal: false}).then(() => {
						this.dialog = true;
						return true
					})
				} else if(alert.alarm_type_id == 2){
					this.$store.dispatch('showAlert', {type: "danger" , text: alert.description, isModal: false}).then(() => {
						this.dialog = true;
						return true
					})
				} else if (alert.alarm_type_id == 3){
					this.$store.dispatch('showAlert', {type: "error" , text:  alert.description, isModal: true}).then(() => {
						this.dialog = true;
						return true
					})
				}
			})
        }
    }
  }
</script>
<style scoped>
	.v-alert{
		position: fixed;
		z-index: 10000;
		width: 100%;
	}
	.prelative{
		position: relative;
	}
	.vh-100{
		height: 100vh;
	}
	.icon-lg{
		font-size:4rem;
	}
	.icon-xl{
		font-size: 15rem;
	}
</style>
