<template>
<v-card>
    <v-tabs class="settings tabs-y-scroll" color="accent-4" left>
      <v-tab>Kinek</v-tab>
      <v-tab>Dust</v-tab>
      <v-tab>General</v-tab>
      <v-tab-item>
        <v-container fluid>
          <v-row>
            <v-col cols="12" md="4">
                <v-card flat color="transparent">
                    <v-subheader>Yellow Shift Light RPM</v-subheader>
                    <v-card-text>
                      <v-slider v-model="kinek.yellow_line" :tick-labels="rpm" :max="11" step="1" ticks tick-size="2" @click="save()"></v-slider>
                    </v-card-text>
                </v-card>
                <v-card flat color="transparent">
                    <v-subheader>Red Shift Light RPM</v-subheader>
                    <v-card-text>
                        <v-slider v-model="kinek.red_line" :tick-labels="rpm" :max="11" step="1" ticks tick-size="2" @click="save()"></v-slider>
                    </v-card-text>
                </v-card>
            </v-col>
          </v-row>
          <v-card flat color="transparent">
            <v-subheader>Slot Position Output</v-subheader>
          </v-card>
          <v-row v-for="(output) in kinek.dashboard_outputs" :key="output.id">
            <v-col>
                <v-card flat color="transparent">
                    <v-select v-model="output.channel_output_id" :items="channel_outputs"  :rules="[v => !!v || 'Output sensor is required']" :label="output.name" @change="save()" required autocomplete="off" />
                </v-card>
            </v-col>
            <v-col>
                <v-card flat color="transparent">
                  <v-btn class="mr-4" @click="send_to('dashboard-proton')"><v-icon>mdi-eye-outline</v-icon> View</v-btn> Checkbox Peak
                </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
    </v-tabs>
  </v-card>
</template>
<script>
	export default {
		data () {
			return {
        dashboars: [],
        channel_outputs: [],
        kinek: {
          dashboard_outputs: null,
          yellow_line: 0,
          red_line: 0,
          rpm: {
            yellow: null,
            red: null,
            last_yellow: null,
            last_red: null,
            alert: {type: "", text: ""}
          }
        },
				rpm: ["OFF",3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000]
			}
		},
		mounted () {
			this.set_dashboards();
		},
		methods: {
      set_dashboards(){
        this.axios.get("settings/kinek").then(result => {
            result.data.outputs.map(out =>{ this.channel_outputs.push({text: out.name, value: out.id})})
            this.set_kinek(result.data)
        }).catch(error => {
            console.log(error);
        })
      },
      set_kinek(result){
        this.kinek.dashboard_outputs = result.dashboard_outputs.filter(output => output.dashboard_id == 1)
      },
			save(){
        if(this.validate_lines(this.kinek.red_line, this.kinek.yellow_line)){
          this.axios.post("settings/kinek", {kinek: this.kinek}).then(result => {
            this.kinek.rpm.last_red = this.kinek.red_line
            this.kinek.rpm.last_yellow = this.kinek.yellow_line
            console.log(result)
          }).catch(error => {
            console.log(error);
          })
        }else{
          this.$store.dispatch('showAlert', {type: "warning", text: "Yellow line must be less than redline"}).then(() => {
            this.kinek.yellow_line = 0
					})
        }
      },
      validate_lines(red_line, yellow_line){
        if(yellow_line != 0 && red_line != 0){
          if(yellow_line > red_line){
            return false
          }else{
            return true
          }
        }else{
          return true
        }
      },
      set_to_rpm(value){
        if (value == 0) return 0
        if (value == 1) return 3000
        if (value == 2) return 3500
        if (value == 3) return 4000
        if (value == 4) return 4500
        if (value == 5) return 5000
        if (value == 6) return 5500
        if (value == 7) return 6000
        if (value == 8) return 6500
        if (value == 9) return 7000
        if (value == 10) return 7500
        if (value == 11) return 8000

      }
		},
		computed: {
			
		}
	}
</script>

<style>
	.small {
		max-width: 740px;
		margin:  50px auto;
	}	
	.settings .v-tabs-items{
		height: 370px;
	}
	.tabs-y-scroll .v-tabs-items{
		overflow-y: scroll !important;
	}
</style>