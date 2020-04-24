<template>
    <div class="">
        <img class="picture" style="" src="../../../../../static/images/dashboards/gtr.jpg" width="710" height="330" />
        <b-row class="mt-2 front">
            <b-col>
              <vue-svg-gauge
                    :start-angle="-110"
                    :end-angle="110"
                    :value="ecu.rpm"
                    :separator-step="0"
                    :min="0"
                    :max="7000"
                    :gauge-color="color.rpm.gaugue"
                    base-color="#00000"
                    :scale-interval="1000"
                    :inner-radius="80"
                    class="left-gauge">
              <div class="inner-text">
                <h1>{{ecu.rpm}}</h1>
                <span class="size-letter">RPM</span>
              </div>
              </vue-svg-gauge>
            </b-col>
            <b-col>
                <vue-svg-gauge
                    :start-angle="-110"
                    :end-angle="110"
                    :value="ecu.mph"
                    :separator-step="0"
                    :min="0"
                    :max="120"
                    :gauge-color="color.mph"
                    :scale-interval=20
                    :inner-radius="80"
                >
                <div class="inner-text">
                  <h1>{{ecu.mph}}</h1>
                  <span class="size-letter">Speed</span>
                </div>
                </vue-svg-gauge>
            </b-col>
            <b-col>
              <vue-svg-gauge
                    :start-angle="-110"
                    :end-angle="110"
                    :value="ecu.rpm"
                    :separator-step="0"
                    :min="0"
                    :max="7000"
                    :gauge-color="color.rpm.gaugue"
                    :scale-interval="1000"
                    :inner-radius="80"
                    class="rpm">
              <div class="inner-text">
                <h1>{{ecu.rpm}}</h1>
                <span class="size-letter">RPM</span>
              </div>
              </vue-svg-gauge>
            </b-col>
        </b-row>
    </div>
</template>
<script>
//   import RadialGauge from 'vue-canvas-gauges/src/RadialGauge'
  export default {
    name: 'Rocket',
    data(){
        return{
            sheet: false,
            ecu: {rpm: 0, speed: 0, temp: 0},
            color: {
                rpm: { gaugue:"#008000", bar: "success" }, mph: "#008000", temp: "#008000" }
        }
    },
    components: {
    //   RadialGauge,
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
                    this.color.rpm.gaugue = "#000000"
                    this.color.rpm.bar = "danger"
                } else if(this.ecu.rpm > 5500 && this.ecu.rpm < 9000) {
                    this.color.rpm.gaugue = "#000000"
                    this.color.rpm.bar = "warning"
                } else {
                    this.color.rpm.gaugue = "#07080a"
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
                if(this.ecu.coolantTemp > 120) {
                    this.color.coolantTemp = "#FF3232"
                } else if(this.ecu.coolantTemp > 90 && this.ecu.coolantTemp < 120) {
                    this.color.coolantTemp = "#008000"
                } else {
                    this.color.coolantTemp = "#0000FF"
                }
            }
        },
    }
  }
</script>

<style scoped>
   .picture{
        z-index: 1;
        position: absolute;
        left: 45px;
        top: 45px;
   }
   .front{
       z-index: 2;
       position: absolute;
   }
	.left-gauge {
		position: absolute;
		margin-left: 13%;
		margin-top: 6%;
		max-width: 150px;
	}
</style>
