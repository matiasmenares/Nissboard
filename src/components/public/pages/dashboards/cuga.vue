<template>
      <div class="gauge-container">
        <b-row id="element">
            <b-col>
              <div class="left-gauge">
                <vue-svg-gauge
                    :start-angle="-100"
                    :end-angle="20"
                    :value="ecu.temp"
                    :separator-step="0"
                    :min="0"
                    :max="170"
                    :gauge-color="color.temp"
                    :scale-interval="10"
                    :inner-radius="80">
                    <div class="inner-text-left">
                      <h1>{{ecu.temp || 0}}</h1>
                    </div>
                    </vue-svg-gauge>
                </div>
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
              <div class="right-gauge">
                <vue-svg-gauge
                    :start-angle="-22"
                    :end-angle="100"
                    :value="ecu.temp"
                    :separator-step="0"
                    :min="0"
                    :max="170"
                    :gauge-color="color.temp"
                    :scale-interval="10"
                    :inner-radius="80">
                    <div class="inner-text">
                    <h1>{{ecu.temp || 0}}</h1>
                    </div>
                </vue-svg-gauge>
              </div>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                Battery 14.0 V
            </b-col>
            <b-col>
                sadasdaaaa
            </b-col>
            <b-col>
                sadasdaaaa
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
		width: 90%;
		position: absolute;
		text-align: center;
		bottom: -65px;
	}
	.inner-text-left {
		height: 100%;
		width: 70%;
		position: absolute;
		text-align: center;
		bottom: -65px;
	}
	.inner-text span {
		max-width: 10px;
		color: rgb(255, 255, 255);
	}
	#element{
		margin-top: 10%;
	}
</style>
