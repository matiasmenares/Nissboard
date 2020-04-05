<template>
      <div class="mx-12">
        <b-row class="mt-1">
            <b-col>
                RPM
            </b-col>
            <b-col>
                <v-icon>mdi-gauge-full</v-icon> 
            </b-col>
            <b-col cols="8">
                <v-progress-linear
                    :background-opacity="0.5"
                    :height="40"
                    :value="values.rpm"
                    :color="colors.rpm"
                ></v-progress-linear>
            </b-col>
            <b-col>
                <span class="normal-letter">{{ecu.rpm}}</span>
            </b-col>
        </b-row>
        <b-row class="mt-1">
            <b-col>
                Speed
            </b-col>
            <b-col>
                <v-icon>mdi-speedometer</v-icon> 
            </b-col>
            <b-col cols="8">
                <v-progress-linear
                    :background-opacity="0.5"
                    :height="40"
                    :value="values.speed"
                    :color="colors.speed"
                ></v-progress-linear>
            </b-col>
            <b-col>
                <span class="normal-letter">{{ecu.speed}}</span> Kph
            </b-col>
        </b-row>
        <b-row class="mt-1">
            <b-col>
                Boost
            </b-col>
            <b-col>
                <v-icon>mdi-car-turbocharger</v-icon> 
            </b-col>
            <b-col cols="8">
                <v-progress-linear
                    :active="active"
                    :background-opacity="0.5"
                    :height="40"
                    :indeterminate="indeterminate"
                    :value="values.turbo"
                    :color="colors.turbo"
                ></v-progress-linear>
            </b-col>
            <b-col>
                <span class="normal-letter">{{analog.turbo.bar.value}}</span> Bar
            </b-col>
        </b-row>
        <b-row class="mt-1">
            <b-col>
                Temp.
            </b-col>
            <b-col>
                <v-icon>mdi-coolant-temperature</v-icon> 
            </b-col>
            <b-col cols="8">
                <v-progress-linear
                    :background-opacity="0.5"
                    :height="40"
                    :value="values.temp"
                    :color="colors.temp"
                ></v-progress-linear>
            </b-col>
            <b-col>
                <span class="normal-letter">{{ecu.temp}}</span> Cº
            </b-col>
        </b-row>
        <b-row class="mt-1">
            <b-col>
                Throttle
            </b-col>
            <b-col>
                <v-icon>mdi-gauge-full</v-icon> 
            </b-col>
            <b-col cols="8">
                <v-progress-linear
                    :background-opacity="0.5"
                    :height="40"
                    :value="values.tps"
                    :color="colors.tps"
                ></v-progress-linear>
            </b-col>
            <b-col>
                <span class="normal-letter">{{Math.round((((ecu.tps) * 100)/4100),2)}} </span>%
            </b-col>
        </b-row>
        <b-row class="mt-1">
            <b-col>
                Battery
            </b-col>
            <b-col>
                <v-icon>mdi-car-battery</v-icon> 
            </b-col>
            <b-col cols="8">
                <v-progress-linear
                    :background-opacity="0.5"
                    :height="40"
                    :value="values.batt"
                    :color="colors.batt"
                ></v-progress-linear>
            </b-col>
            <b-col>
                <span class="normal-letter">{{ecu.batt}} V</span>
            </b-col>
        </b-row>
    </div>
</template>
<script>
  export default {
    name: 'Kinek',
    data(){
        return{
            sheet: false,
            ecu: {rpm: 0, speed: 0, temp: 0, batt: 0, turbo: 0, tps: 0, intake: 0},
            colors: {rpm: "light-green", speed: "light-green", temp: "light-green", batt: "light-green", turbo: "light-green", tps: "light-green", intake: "light-green"},
            values: {rpm: 0, speed: 0, temp: 0, batt: 0, turbo: 0, tps: 0, intake: 0},
            dashboard:{
                colors:{ safe: "light-green" , warning: "amber" , danger: "red darken-2"}
            },
            analog: {turbo: { psi: {value: "0.0", raw: "0000", peak: "0.0"}, bar: {value: "0.0", raw: "0000", peak: "0.0"}}},
        }
    },
    components: {
    },
    mounted(){
    },
    created() {
        this.set_data()
        this.set_analog_sensors()
    },
    methods: {
        set_data(){
            this.sockets.subscribe('ecuData', (data) => {
                this.ecu = data;
            })
        },
        set_analog_sensors(){
            this.sockets.subscribe('analog', (data) => {
                this.analog = data;
            })
        },
    },
    watch: {
        "ecu.rpm": {
            handler: function() {
                this.values.rpm = (this.ecu.rpm * 100) / 9000
                if(this.ecu.rpm > 6500){
                    //danger
                    this.colors.rpm = this.dashboard.colors.danger
                } else if(this.ecu.rpm > 5500 && this.ecu.rpm < 9000) {
                    //warning
                    this.colors.rpm = this.dashboard.colors.warning
                } else {
                    //success
                    this.colors.rpm = this.dashboard.colors.safe
                }
            }
        },
        "ecu.speed": {
            handler: function() {
                this.values.speed = (this.ecu.speed * 100) / 120
                if(this.ecu.speed > 110){
                    //danger
                    this.colors.speed = this.dashboard.colors.danger
                } else if(this.ecu.speed > 90 && this.ecu.speed < 100) {
                    //warning
                    this.colors.speed = this.dashboard.colors.warning
                } else {
                    //success
                    this.colors.speed = this.dashboard.colors.safe
                }
            }
        },
        "ecu.temp": {
            handler: function() {
                this.values.temp = (this.ecu.temp * 100) / 200
                 if(this.ecu.temp > 150){
                    //danger
                    this.colors.temp = this.dashboard.colors.danger
                } else if(this.ecu.temp > 100 && this.ecu.temp < 150) {
                    //warning
                    this.colors.temp = this.dashboard.colors.warning
                } else {
                    //success
                    this.colors.temp = this.dashboard.colors.safe
                }
            }
        },
        "ecu.tps": {
            handler: function() {
                this.values.tps = Math.round((((this.ecu.tps) * 100)/4100),2)
            }
        },
        "ecu.batt": {
            handler: function() {
            this.values.batt = (this.ecu.batt * 100) / 16
                 if(this.values.batt > 90 || this.values.batt < 20 ){
                    //danger
                    this.colors.batt = this.dashboard.colors.danger
                } else if(this.values.batt > 80 && this.ecu.batt < 90) {
                    //warning
                    this.colors.batt = this.dashboard.colors.warning
                } else {
                    //success
                    this.colors.batt = this.dashboard.colors.safe
                }
            }
        },
        "analog.turbo.bar.value": {
            handler: function() {
                this.values.turbo = ((this.analog.turbo.bar.value * 100.0) / 2.0)
                 if(this.values.turbo > 80.0){
                    //danger
                    this.colors.turbo = this.dashboard.colors.danger
                } else if(this.values.turbo > 70.0 && this.ecu.turbo < 80.0) {
                    //warning
                    this.colors.turbo = this.dashboard.colors.warning
                } else {
                    //success
                    this.colors.turbo = this.dashboard.colors.safe
                }
            }
        },
    }
  }
</script>

<style scoped>
.normal-letter{
  font-size: 20px;
}
.max-letter {
  font-size: 40px;
}
.min-letter {
  font-size: 15px;
}
svg {
  position: absolute;
  width: 100%;
  height: 100%;
  margin: 0px;
  border: 0px;
  padding: 0px;
  overflow: hidden;
}
</style>
