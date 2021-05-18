<template>
    <div>
        <img class="picture" style="" src="../../../../../static/images/dashboards/nebula/nebula.png" />
        <vue-speedometer class="speed"
        :maxSegmentLabels="10"
        :segments="0"
        :needleTransitionDuration="80"
        :needleHeightRatio="0.8"
        :ringWidth="30"
        :value="analog.turbo.psi.raw"
        :minValue="205"
        :maxValue="1000"
        needleColor="#ea1c25"
        />
    </div>
</template>
<script>
import VueSpeedometer from "vue-speedometer"
  export default {
    name: 'Rocket',
    data(){
        return{
            sheet: false,
            ecu: {rpm: 0, speed: 0, temp: 0},
            timestamp: null,
            analog: {turbo: { psi: {value: "0.0", raw: "0000", peak: "0.0"}, bar: {value: "0.0", raw: "0000", peak: "0.0"}}},
            color: {
                rpm: { gaugue:"#008000", bar: "success" }, mph: "#008000", temp: "#008000" }
        }
    },
    components: { VueSpeedometer },
    created() {
        this.set_data()
        this.set_analog_sensors()
		setInterval(this.getNow, 1000);
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
		getNow: function() {
			const today = new Date();
			const time = today.getHours() + ":" + today.getMinutes()
			this.timestamp = time;
		}
    },
    watch: {
    }
  }
</script>

<style scoped>
	.picture{
		z-index: 1;
		position: absolute;
		left: 5px;
		width: 800px;
		height: 450px;
	}
	.speed{
		z-index: 2 !important;
        position: absolute;
		left: 255px;
        top: 75px;
	}
	.lower-row{
		margin-top: 60px;
	}
	.gauge{
		border: 0px;
		margin-left: auto;
		margin-right: auto;
		width: 70%;
		margin-top: 14px;
	}
	.inner-text {
		height: 100%;
		width: 100%;
		position: absolute;
		text-align: center;
		bottom: -50px;
	}
	.inner-text span {
		max-width: 10px;
		color: rgb(255, 255, 255);
	}
	.hours {
		position: absolute;
		z-index: 2;
		margin-left: 670px;
		font-size: 43px;
	}
	</style>
