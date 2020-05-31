<template>
      <div id="init-div">       
        <b-row no-gutters class="mt-10">
           <b-col class="text-center max-letter">
                <h1>{{ecu.speed}} <span class="min-letter">Kph</span></h1>
            </b-col>
            <b-col class="text-center max-letter">
                <h1>{{ecu.rpm}} <span class="min-letter">Rpm</span></h1>
            </b-col>
           <b-col class="text-center   max-letter">
                <h1>{{ecu.temp}} <span class="min-letter">Cº</span></h1>
            </b-col>
        </b-row>
        <hr>
        <b-row no-gutters class="mt-5">
           <b-col class="text-center max-letter">
                <h1>{{ecu.turbo}} <span class="min-letter">Psi</span></h1>
            </b-col>
            <b-col class="text-center max-letter">
                <h1>{{Math.round((((ecu.tps) * 100)/4100),2)}} <span class="min-letter">% Tps</span></h1>
            </b-col>
           <b-col class="text-center max-letter">
                <h1>{{ecu.batt}} <span class="min-letter">V</span></h1>
            </b-col>
           <b-col class="text-center max-letter">
                <h1>{{ecu.timming}} <span class="min-letter">Timming</span></h1>
            </b-col>
        </b-row>
        <hr>
        <b-row no-gutters class="mt-5">
           <b-col class="text-center max-letter">
                <h1>{{ecu.O2}} <span class="min-letter">02</span></h1>
            </b-col>
            <b-col class="text-center max-letter">
                <h1> {{ecu.aac}}<span class="min-letter"> AAC</span></h1>
            </b-col>
           <b-col class="text-center max-letter">
                <h1>{{ecu.injector}} <span class="min-letter">Inj.</span></h1>
            </b-col>
           <b-col class="text-center max-letter">
                <h1>{{ecu.af}} <span class="min-letter">Air/Fuel</span></h1>
            </b-col>
        </b-row>
    </div>
</template>
<script>
  export default {
    name: 'Init',
    data(){
        return{
            sheet: false,
            ecu: {rpm: 0, speed: 0, temp: 0, batt: 0, turbo: 0.0, tps: 0, intake: 0, timming: 0, O2: 0, aac: 0, injector: 0, af: 0},
            color: {rpm: "light-blue"},
            value: 0,
            red_line: 0,
            yellow_line: 0
        }
    },
    components: {
    },
    mounted(){
    },
    created() {
        this.set_data()
        this.set_kinek()
    },
    methods: {
        set_data(){
            this.sockets.subscribe('ecuData', (data) => {
                this.ecu = data;
            })
        },
        set_kinek(){
            this.axios.get("settings/kinek").then(result => {
                this.red_line = parseInt(result.data["kinkek"][4])
                this.yellow_line = parseInt(result.data["kinkek"][5])
            }).catch(error => {
                console.log(error);
            })
        }
    },
    watch: {
        "ecu.rpm": {
            handler: function() {
                this.value = (this.ecu.rpm * 100) / 9000
                if (this.red_line > 0){
                    if(this.ecu.rpm > this.red_line){
                    //danger
                        this.color.rpm = "red darken-2"
                    }else if(this.yellow_line > 0){
                        if(this.ecu.rpm > this.yellow_line && this.ecu.rpm < this.red_line){
                            //warning
                            this.color.rpm = "amber"
                        }else{
                        //success
                        this.color.rpm = "light-blue" 
                         }
                    }else{
                        //success
                        this.color.rpm = "light-blue" 
                    }
                }else if(this.yellow_line > 0){
                    if(this.ecu.rpm > this.red_line){
                        //warning
                        this.color.rpm = "amber"
                    }
                }else{
                    //success
                    this.color.rpm = "light-blue"
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
@import url('https://fonts.googleapis.com/css?family=Quantico');
#init-div {
  font-family: 'Quantico', sans-serif;
}
.normal-letter{
  font-size: 20px;
}
.max-letter {
  font-size: 33px;
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
