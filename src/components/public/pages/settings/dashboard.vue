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
                    <v-subheader>Yellow Shift Light RPM</v-subheader>
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
			this.set_kinek();
		},
		methods: {
      set_kinek(){
        this.axios.get("settings/kinek").then(result => {
            this.kinek.rpm.red = parseInt(result.data["kinkek"][2])
            this.kinek.rpm.yellow = parseInt(result.data["kinkek"][3])
            this.kinek.rpm.last_red = parseInt(result.data["kinkek"][2])
            this.kinek.rpm.last_yellow = parseInt(result.data["kinkek"][3])
        }).catch(error => {
            console.log(error);
        })
      },
			save(){
        if(this.kinek.rpm.red > this.kinek.rpm.yellow){
          this.axios.post("settings/kinek",{red_line: this.kinek.rpm.red, yellow_line: this.kinek.rpm.yellow, yellow_line_rpm: this.set_to_rpm(this.kinek.rpm.yellow), red_line_rpm: this.set_to_rpm(this.kinek.rpm.red) }).then(result => {
            this.kinek.rpm.last_red = this.kinek.rpm.red
            this.kinek.rpm.last_yellow = this.kinek.rpm.yellow
            console.log(result)
          }).catch(error => {
            console.log(error);
          })
        }else{
          this.$store.dispatch('showAlert', {type: "warning", text: "Yellow line debe ser menor a redline"}).then(() => {
            this.kinek.rpm.red = this.kinek.rpm.last_red
            this.kinek.rpm.yellow = this.kinek.rpm.last_yellow
					})
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
</style>