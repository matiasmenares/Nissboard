<template>
      <div>
        <b-row>
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
                    <div class="inner-text">
                      <h1>{{ecu.temp || 10}}</h1>
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
                  <h1>{{ecu.temp || 10}} <span class="size-letter">Kph</span></h1>
                </div>
              </vue-svg-gauge>
              </div>
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
                rpm: { gaugue:"#7FFF22",bar: "success" }, mph: "#008000", temp: "#008000" }
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
                    this.color.rpm.gaugue = "#7FFF22"
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
  font-size: 8px;
}
.left-gauge {
  position: absolute;
  margin-left: 13%;
  margin-top: 6%;
}
.right-gauge {
  position: absolute;
  margin-left: -7%;
  margin-top: 6%;
}
.inner-text {
  height: 100%;
  width: 100%;
  position: absolute;
  text-align: center;
  bottom: -65px;
  span {
    max-width: 100px;
    color: red;
  }
}
</style>
