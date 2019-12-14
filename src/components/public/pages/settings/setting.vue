<template>
<v-card>
    <v-tabs color="accent-4" left>
      <v-tab>Cuga</v-tab>
      <v-tab>Graph</v-tab>
      <v-tab>General</v-tab>

      <v-tab-item >
        <v-container fluid>
          <v-row>
            <v-col cols="12" md="4">
                <v-card flat color="transparent">
                    <v-subheader>Yellow Shift Light RPM</v-subheader>
                    <v-card-text>
                        <v-slider v-model="cuga.rpm.yellow" :tick-labels="rpm" :max="11" step="1" ticks tick-size="1"></v-slider>
                    </v-card-text>
                </v-card>
                <v-card flat color="transparent">
                    <v-subheader>Red Shift Light RPM</v-subheader>
                    <v-card-text>
                        <v-slider v-model="cuga.rpm.red" :tick-labels="rpm" :max="11" step="1" ticks tick-size="1"></v-slider>
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
		components: {
		},
		data () {
			return {
        cuga: {
          rpm: {
            yellow: null,
            red: null
          }
        },
				rpm: ["OFF",3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000]
			}
		},
		mounted () {
			//this.fillData();
		},
		methods: {
			
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