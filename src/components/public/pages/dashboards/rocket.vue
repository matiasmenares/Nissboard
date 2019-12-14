<template>
      <div class="gauge-container">
        <b-row class="element">
            <b-col class="rpm-container">
              <vue-svg-gauge
                    :start-angle="-130"
                    :end-angle="130"
                    :value="ecu.rpm"
                    :separator-step="0"
                    :min="0"
                    :max="7000"
                    :gauge-color="color.rpm.gaugue"
                    :scale-interval="1000"
                    :inner-radius="76"
                    class="rpm">
              </vue-svg-gauge>
              <div class="inner-text" style="display: table;">
                <div class="rpm-text" style="display: table-cell; vertical-align: middle">
                    {{ecu.rpm}}<br/>
                    <small>RPM</small>
                </div>
              </div>
            </b-col>
        </b-row>
        <div class="box">BOX</div>
    </div>
</template>
<script>
  // import RadialGauge from 'vue-canvas-gauges/src/RadialGauge'
  export default {
    name: 'Rocket',
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
    .border{
        border: 1px solid red;
    }
	.size-letter {
        font-size: 20px;
        width: 100%;
        margin-left: 20%;
	}
    .rpm-container{
        max-height: 400px;
        margin-right: auto;
        margin-left: auto;
        padding: 0;
        position: relative;
    }
    .rpm{
        margin-left: auto;
        margin-right: auto;
    }
    .rpm > svg{
        z-index: -1;    
    }
    .rpm-text{
        font-size: 70px;
        line-height: 50px;
    }
    .rpm-text small{
        font-size: .45em;
    }
    .inner-text {
		height: 100%;
        width: 100%;
		position: absolute;
        text-align: center;
        top: 20px;
	}
	.element{
        margin-top: 30px;
    }
    .box{
        width: 100%;
        background: linear-gradient( #6d6d6d 0%, #000 100%);
        margin-top: -80px;
        height: 200px;
        position: absolute;
    }
</style>
