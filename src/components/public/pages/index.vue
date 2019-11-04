<template>
	<div>
        <b-container block class="p-4">
            <b-row>
                <b-col>
                    <vue-svg-gauge
                        :start-angle="-100"
                        :end-angle="100"
                        :value="ecu.rpm"
                        :separator-step="0"
                        :min="0"
                        :max="7000"
                        gauge-color="#8CDFAD"
                        :scale-interval="1000"
                        :inner-radius="80"
                    />
                    <p class="text-white">RPM {{ecu.rpm}}</p>
                </b-col>
                <b-col>
                    <vue-svg-gauge
                        :start-angle="-100"
                        :end-angle="100"
                        :value="ecu.mph"
                        :separator-step="0"
                        :min="0"
                        :max="100"
                        gauge-color="#8CDFAD"
                        :scale-interval=20
                        :inner-radius="80"
                    />
                   <p class="text-white">Speed: {{ecu.mph}}</p>
                </b-col>
               <b-col>
                    <vue-svg-gauge
                        :start-angle="0"
                        :end-angle="100"
                        :value="ecu.coolantTemp"
                        :separator-step="0"
                        :min="0"
                        :max="200"
                        gauge-color="#8CDFAD"
                        :scale-interval="40"
                        :inner-radius="80"
                    />
                    <p class="text-white">Coolant {{ecu.coolantTemp}}</p>
                </b-col>
            </b-row>
                <RadialGauge :options="{ value: 200 }"></RadialGauge>

        </b-container>
	</div>
</template>

<script>
import RadialGauge from 'vue-canvas-gauges/src/RadialGauge'

  export default {
    name: 'Index',
    data(){
        return{
            ecu: {rpm: 0, mph: 0, coolantTemp: 0}
        }
    },
	components: {
        RadialGauge,
    },
    mounted(){
        this.set_data()
    },
	methods: {
        set_data(){
            this.sockets.subscribe('ecuData', (data) => {
                this.ecu = data;
            })
        }
	}
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
