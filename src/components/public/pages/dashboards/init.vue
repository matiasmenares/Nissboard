<template>
      <div id="init-div">       
        <b-row no-gutters class="mt-10">
            <b-col class="text-center" v-if="channel_output[0]">
                <span class="max-letter">{{channel_output[0]['value']}}</span> <span class="min-letter">{{channel_output[0]['name']}}</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center" v-if="channel_output[1]">
                <span class="max-letter">{{channel_output[1]['value']}}</span> <span class="min-letter">{{channel_output[1]['name']}}</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center" v-if="channel_output[2]">
                <span class="max-letter">{{channel_output[2]['value']}}</span> <span class="min-letter">{{channel_output[2]['name']}}</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
        </b-row>
        <hr>
        <b-row no-gutters class="mt-5">
            <b-col class="text-center max-letter" v-if="channel_output[3]">
                <span class="max-letter">{{channel_output[2]['value']}} </span><span class="min-letter">{{channel_output[3]['name']}}</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center max-letter" v-if="channel_output[4]">
                <h1>{{channel_output[4]['value']}} <span class="min-letter">{{channel_output[4]['name']}}</span></h1>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center max-letter" v-if="channel_output[5]">
                <h1>{{channel_output[5]['value']}} <span class="min-letter">{{channel_output[5]['name']}}</span></h1>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center max-letter" v-if="channel_output[6]">
                <h1>{{channel_output[6]['value']}} <span class="min-letter">{{channel_output[6]['name']}}</span></h1>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
        </b-row>
        <hr>
        <b-row no-gutters class="mt-5">
            <b-col class="text-center max-letter" v-if="channel_output[7]">
                <h1>{{channel_output[7]['value']}} <span class="min-letter">{{channel_output[7]['name']}}</span></h1>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center max-letter" v-if="channel_output[8]">
                <h1>{{channel_output[8]['value']}} <span class="min-letter">{{channel_output[8]['name']}}</span></h1>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center max-letter" v-if="channel_output[9]">
                <h1>{{channel_output[9]['value']}} <span class="min-letter">{{channel_output[9]['name']}}</span></h1>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center max-letter" v-if="channel_output[10]">
                <h1>{{channel_output[10]['value']}} <span class="min-letter">{{channel_output[2]['name']}}</span></h1>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
        </b-row>
    </div>
</template>
<script>
  import outputs from "../../mixins/outputs"

  export default {
    name: 'Init',
    mixins: [outputs],
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
        this.set_dash_output()
    },
    methods: {
      set_dash_output(){
            this.axios.get("dashboards").then(result => {
                this.slots = result.data.dashboard_outputs.filter(slot => slot.dashboard_id == 3 )
            }).catch(error => {
                console.log(error);
            })
        },
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
  font-size: 55px;
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
