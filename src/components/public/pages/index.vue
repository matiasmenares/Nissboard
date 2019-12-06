<template>
	<div>
        <b-row>
            <b-col>
                <vue-svg-gauge
                    :start-angle="-90"
                    :end-angle="0"
                    :value="ecu.temp"
                    :separator-step="0"
                    :min="0"
                    :max="170"
                    :gauge-color="color.temp"
                    :scale-interval="10"
                    :inner-radius="80"
                />
                <h5 class="text-white">Coolant Temp {{ecu.temp}}</h5>
            </b-col>
            <b-col>
                <vue-svg-gauge :start-angle="-90" :end-angle="90" :value="ecu.rpm" :separator-step="0" :min="0" :max="7000" :gauge-color="color.rpm.gaugue" :scale-interval="1000" :inner-radius="80">
                    <div class="inner-text">
                        <span><h1>{{ecu.rpm}}</h1></span>
                    </div>
                </vue-svg-gauge>
                <h5 class="text-white">RPM {{ecu.rpm}}</h5>
            </b-col>
            <b-col>
                <vue-svg-gauge
                    :start-angle="-90"
                    :end-angle="90"
                    :value="ecu.mph"
                    :separator-step="0"
                    :min="0"
                    :max="120"
                    :gauge-color="color.mph"
                    :scale-interval=20
                    :inner-radius="80"
                />
                <h5 class="text-white">Speed: {{ecu.mph}} Kph</h5>
            </b-col>
            <b-col>
                <vue-svg-gauge
                    :start-angle="0"
                    :end-angle="100"
                    :value="ecu.temp"
                    :separator-step="0"
                    :min="0"
                    :max="170"
                    :gauge-color="color.temp"
                    :scale-interval="10"
                    :inner-radius="80"
                />
                <h5 class="text-white">MAF: {{ecu.temp}} Kph</h5>
            </b-col>
        </b-row>
        <!-- <b-row>
            <b-col>
                <radial-gauge :value="ecu.coolantTemp"></radial-gauge>
            </b-col>
            <b-col>
                <b-progress :max="7200" height="10rem">
                    <b-progress-bar :variant="color.rpm.bar" :value="ecu.rpm">
                        RPM: <strong>{{ecu.rpm}}</strong>
                    </b-progress-bar>
                </b-progress>

            </b-col>
        </b-row> -->
	</div>
</template>
<script>
// import RadialGauge from 'vue-canvas-gauges/src/RadialGauge'

  export default {
    name: 'Index',
    data(){
        return{
            sheet: false,
            ecu: {rpm: 0, mph: 0, temp: 0},
            color: {rpm: {gaugue:"#008000", bar: "success"}, mph: "#008000", temp: "#008000" }
        }
    },
	components: {
        // RadialGauge,
    },
    mounted(){
    },
    created() {
        this.set_data()
    },
	methods: {
        set_data(){
            this.sockets.subscribe('ecuData', (data) => {
                this.ecu = data;
            })
        }
	},
    watch: {
        "ecu.rpm": {
            handler: function() {
                if(this.ecu.rpm > 6500){
                    this.color.rpm.gaugue = "#FF0000"
                    this.color.rpm.bar = "danger"
                }else if(this.ecu.rpm > 5500 && this.ecu.rpm < 9000){
                    this.color.rpm.gaugue = "#FFFF00"
                    this.color.rpm.bar = "warning"
                }else{
                    this.color.rpm.gaugue = "#008000"
                    this.color.rpm.bar = "success"
                }
            }
        },
        "ecu.mph": {
            handler: function() {
            }
        },
        "ecu.coolantTemp": {
            handler: function() {
                if(this.ecu.coolantTemp > 120){
                    this.color.coolantTemp = "#FF0000"
                }else if(this.ecu.coolantTemp > 90 && this.ecu.coolantTemp < 120){
                    this.color.coolantTemp = "#008000"
                }else{
                    this.color.coolantTemp = "#0000FF"
                }
            }
        },   
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.inner-text {
  height: 100%;
  width: 100%;

  span {
    max-width: 100px;
    color: red;
  }
}
</style>
