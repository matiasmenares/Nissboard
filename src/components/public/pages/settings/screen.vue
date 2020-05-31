<template>
<v-card>
    <v-tabs color="accent-4" left>
      <v-tab>Screen</v-tab>
      <v-tab-item>
        <v-container fluid>
          <v-row>
            <v-col cols="12" md="4">
                <v-card flat color="transparent">
                    <v-subheader>Brightness %</v-subheader>
                    <v-card-text>
                      <v-slider v-model="brightness.value" :tick-labels="brightness_values" :max="19" step="1" ticks tick-size="2" @click="save()"></v-slider>
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
                brightness: {
                    value: 19,
                },
                brightness_values: [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
            }
		},
		mounted () {
			this.set_kinek();
		},
		methods: {
            set_kinek(){
                this.axios.get("settings/screen").then(result => {
                    this.brightness.value = parseInt(result.data.brightness)
                }).catch(error => {
                    console.log(error);
                })
            },
            save(){
                this.axios.post("settings/screen",{screen: this.set_to_brig(this.brightness.value) }).then(result => {
                    console.log(result)
                }).catch(error => {
                    console.log(error);
                })
            },
            set_to_brig(value){
            if (value == 0) return 5
            if (value == 1) return 10
            if (value == 2) return 15
            if (value == 3) return 20
            if (value == 4) return 25
            if (value == 5) return 30
            if (value == 6) return 35
            if (value == 7) return 40
            if (value == 8) return 45
            if (value == 9) return 50
            if (value == 10) return 55
            if (value == 11) return 60
            if (value == 12) return 65
            if (value == 14) return 70
            if (value == 15) return 75
            if (value == 16) return 80
            if (value == 17) return 85
            if (value == 18) return 90
            if (value == 19) return 95
            if (value == 20) return 100
            }
		}
	}
</script>

<style>
	.small {
		max-width: 740px;
		margin:  50px auto;
	}
</style>