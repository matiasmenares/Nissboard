<template>
      <div class="gauge-container">
        <b-row class="mt-2">
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
                    :value="analog.turbo.psi.value"
                    :separator-step="0"
                    :min="0"
                    :max="14"
                    :gauge-color="color.rpm.gaugue"
                    :scale-interval="4"
                    :inner-radius="80"
                    class="rpm">
              <div class="inner-text">
                <h1>{{analog.turbo.psi.value}}</h1>
                <span class="size-letter">Boost</span>
              </div>
              </vue-svg-gauge>
            </b-col>
        </b-row>
        <b-row class="mt-2">
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
  // import RadialGauge from 'vue-canvas-gauges/src/RadialGauge'
  export default {
    name: 'Cuga',
    data(){
        return{
            sheet: false,
            ecu: {rpm: 0, mph: 0, temp: 0},
            analog: {turbo: { psi: {value: "0.0", raw: "0000", peak: "0.0"}, bar: {value: "0.0", raw: "0000", peak: "0.0"}}},
            color: {
                rpm: { gaugue:"#008000", bar: "success" }, mph: "#008000", temp: "#008000" }
        }
    },
    components: {
      // RadialGauge,
    },
    mounted(){
    },
    created() {
        this.set_data()
        this.set_analog()

    },
    methods: {
        set_data(){
            this.sockets.subscribe('ecuData', (data) => {
                this.ecu = data;
            })
        },
        set_analog(){
            this.sockets.subscribe('analog', (data) => {
                this.analog = data;
            })
        }
    },
    watch: {
        "ecu.rpm": {
            handler: function() {
                if(this.ecu.rpm > 6500){
                    this.color.rpm.gaugue = "#FF3232"
                    this.color.rpm.bar = "danger"
                } else if(this.ecu.rpm > 5500 && this.ecu.rpm < 9000) {
                    this.color.rpm.gaugue = "#FFFF00"
                    this.color.rpm.bar = "warning"
                } else {
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
	.size-letter {
		font-size: 14px;
	}
	.left-gauge {
		position: absolute;
		margin-left: 13%;
		margin-top: 6%;
		max-width: 150px;
	}
	.right-gauge {
		position: absolute;
		margin-left: -9%;
		margin-top: 6%;
		max-width: 150px;
	}
	.inner-text {
		height: 100%;
		width: 100%;
		position: absolute;
		text-align: center;
		bottom: -50px;
	}
	.inner-text-left {
		height: 100%;
		width: 1000%;
		position: absolute;
		text-align: center;
		bottom: -50px;
	}
	.inner-text span {
		max-width: 10px;
		color: rgb(255, 255, 255);
	}
	#element{
		margin-top: 10%;
	}
</style>
