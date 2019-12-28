<template>
    <div class="">
        <b-row class="mt-12 mx-12">
            <b-col>
               <canvas data-type="radial-gauge"
                    data-width="300"
                    data-height="300"
                    data-units="Km/H"
                    data-min-value="0"
                    data-max-value="220"
                    data-major-ticks="0,20,40,60,80,100,120,140,160,180,200,220"
                    data-minor-ticks="2"
                    data-stroke-ticks="true"
                    data-highlights='[
                        {"from": 200, "to": 220, "color": "rgba(200, 50, 50, .75)"}
                    ]'
                    :data-value="ecu.speed"
                     data-color-major-ticks="#ddd"
                    data-color-minor-ticks="#ddd"
                    data-color-title="#eee"
                    data-color-units="#ccc"
                    data-color-numbers="#eee"
                    data-color-plate="#222"
                    data-border-shadow-width="0"
                    data-borders="false"
                    data-needle-type="arrow"
                    data-needle-width="2"
                    data-needle-circle-size="7"
                    data-needle-circle-outer="true"
                    data-needle-circle-inner="false"
                    data-animation-duration="200"
                    data-animation-rule="linear"
                ></canvas>
            </b-col>
            <b-col>
                <canvas data-type="radial-gauge"
                    data-width="300"
                    data-height="300"
                    data-units="x1000 RPM"
                    data-min-value="0"
                    data-max-value="9000"
                    data-major-ticks="0,1,2,3,4,5,6,7,8,9"
                    data-minor-ticks="2"
                    data-stroke-ticks="true"
                    data-highlights='[
                        {"from": 7500, "to": 9000, "color": "rgba(200, 50, 50, .75)"}
                    ]'
                    :data-value="ecu.rpm"
                    data-color-major-ticks="#ddd"
                    data-color-minor-ticks="#ddd"
                    data-color-title="#eee"
                    data-color-units="#ccc"
                    data-color-numbers="#eee"
                    data-color-plate="#222"
                    data-border-shadow-width="0"
                    data-borders="false"
                    data-needle-type="arrow"
                    data-needle-width="2"
                    data-needle-circle-size="7"
                    data-needle-circle-outer="true"
                    data-needle-circle-inner="false"
                    data-animation-duration="400"
                    data-animation-rule="linear"
                ></canvas>
            </b-col>
            <b-col style="">
                <radial-gauge :options="{'max-value': 1000}" :value="ecu.rpm/100"></radial-gauge>
            </b-col>
        </b-row>
    </div>

</template>
<script>
  import RadialGauge from 'vue-canvas-gauges/src/RadialGauge'
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
      RadialGauge,
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
   
</style>
