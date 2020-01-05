<template>
<v-card>
    <v-tabs color="accent-4" left>
      <v-tab>Water Temp</v-tab>
      <v-tab-item>
        <v-container fluid>
          <v-row>
            <v-col cols="12" md="4">
                <v-card flat color="transparent">
                    <v-subheader>Max Cº</v-subheader>
                    <v-card-text>
                      <v-slider v-model="water.value" :tick-labels="water_values" :max="11" step="1" ticks tick-size="2" @click="save()"></v-slider>
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
        water: {
            value: "",
        },
        water_values: ["OFF",50,60,70,80,90,100,110,120,130,140,150]
      }
		},
		mounted () {
			this.set_kinek();
		},
		methods: {
      set_kinek(){
        this.axios.get("settings/water").then(result => {
            this.water.value = parseInt(result.data["Water"][5])
        }).catch(error => {
            console.log(error);
        })
      },
			save(){
          this.axios.post("settings/water",{alert_value: this.water.value, alert: this.set_to_temp(this.water.value) }).then(result => {
            console.log(result)
          }).catch(error => {
            console.log(error);
          })
      },
      set_to_temp(value){
        if (value == 0) return 0
        if (value == 1) return 50
        if (value == 2) return 60
        if (value == 3) return 70
        if (value == 4) return 80
        if (value == 5) return 90
        if (value == 6) return 100
        if (value == 7) return 110
        if (value == 8) return 120
        if (value == 9) return 130
        if (value == 10) return 140
        if (value == 11) return 150

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