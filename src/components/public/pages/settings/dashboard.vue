<template>
<v-card>
    <v-tabs color="accent-4" left>
      <v-tab>Kinek</v-tab>
      <v-tab>Dust</v-tab>
      <v-tab>General</v-tab>
      <v-tab-item >
        <v-container fluid>
          <v-row>
            <v-col cols="12" md="4">
                <v-card flat color="transparent">
                    <v-subheader>Yellow Shift Light RPM {{kinek.rpm.yellow}}</v-subheader>
                    <v-card-text>
                      <v-slider v-model="kinek.rpm.yellow" :tick-labels="rpm" :max="11" step="1" ticks tick-size="2" @click="save()"></v-slider>
                    </v-card-text>
                </v-card>
                <v-card flat color="transparent">
                    <v-subheader>Red Shift Light RPM</v-subheader>
                    <v-card-text>
                        <v-slider v-model="kinek.rpm.red" :tick-labels="rpm" :max="11" step="1" ticks tick-size="2" @click="save()"></v-slider>
                    </v-card-text>
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
        kinek: {
          rpm: {
            yellow: null,
            red: null
          }
        },
				rpm: ["OFF",3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000]
			}
		},
		mounted () {
			this.set_kinek();
		},
		methods: {
      set_kinek(){
        let self = this
        this.axios.get("settings/kinek").then(result => {
            self.kinek.rpm.red = parseInt(result.data["kinkek"][2])
            self.kinek.rpm.yellow = parseInt(result.data["kinkek"][3])
        }).catch(error => {
            console.log(error);
        })
      },
			save(){

        this.axios.post("settings/kinek",{red_line: this.kinek.rpm.red, yellow_line: this.kinek.rpm.yellow}).then(result => {
            console.log(result)
        }).catch(error => {
            console.log(error);
        }) 
      },
      set_to_rpm(value){
        if (value == 0) return 0
        if (value == 1) return 'teal'
        if (value == 2) return 'green'
        if (value == 3) return 'orange'
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
</style>