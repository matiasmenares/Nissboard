<template>
    <div class="">
		<h1 class="hours">{{ timestamp }}</h1>
        <img class="picture-header" style="" src="../../../../../static/images/dashboards/header-gtr.png" />
        <img class="picture" style="" src="../../../../../static/images/dashboards/gtr.jpg" />
        <div class="picture">
			<b-row no-gutters class="mt-2 front">
				<b-col style="">
				<vue-svg-gauge
						:start-angle="-90"
						:end-angle="90"
						:value="speed.out"
						:separator-step="0"
						:min="0"
						:max="300"
						:transitionDuration="10"
						gauge-color="#f8f9f9"
						base-color="#000000"
						:scale-interval="1000"
						:inner-radius="80"
						class="gauge">
					<div class="inner-text">
						<h1>{{speed.out}}</h1>
						<span class="size-letter">Speed</span>
					</div>
				</vue-svg-gauge>
				</b-col>
				<b-col>
					<vue-svg-gauge
						:start-angle="-90"
						:end-angle="90"
						:value="rpm.out"
						:separator-step="0"
						:min="0"
						:max="8000"
						:transitionDuration="10"
						gauge-color="#f8f9f9"
						:scale-interval="20"
						:inner-radius="80"
						base-color="#000000"
						class="gauge"
					>
					<div class="inner-text">
					<h1>{{rpm.out}}</h1>
					<span class="size-letter">RPM</span>
					</div>
					</vue-svg-gauge>
				</b-col>
				<b-col>
				<vue-svg-gauge
						:start-angle="-90"
						:end-angle="90"
						:value="(temp.out-30)"
						:separator-step="0"
						:min="0"
						:max="130"
						:transitionDuration="10"
						gauge-color="#f8f9f9"
						:scale-interval="900"
						:inner-radius="80"
						base-color="#000000"
						class="gauge">
				<div class="inner-text">
					<h1>{{temp.out}}</h1>
					<span class="size-letter">Temp</span>
				</div>
				</vue-svg-gauge>
				</b-col>
			</b-row>
			<b-row no-gutters class="front lower-row">
				<b-col style="">
				<vue-svg-gauge
						:start-angle="-90"
						:end-angle="90"
						:value="0"
						:separator-step="0"
						:min="0"
						:max="1"
						:transitionDuration="10"
						gauge-color="#f8f9f9"
						base-color="#000000"
						:scale-interval="1000"
						:inner-radius="80"
						class="gauge">
				<div class="inner-text">
					<h1>{{ecu.rpm}}</h1>
					<span class="size-letter">RPM</span>
				</div>
				</vue-svg-gauge>
				</b-col>
				<b-col>
					<vue-svg-gauge
						:start-angle="-90"
						:end-angle="90"
						:value="0"
						:separator-step="0"
						:transitionDuration="10"
						:min="0"
						:max="1"
						gauge-color="#f8f9f9"
						:scale-interval="20"
						:inner-radius="80"
						base-color="#000000"
						class="gauge"
					>
					<div class="inner-text">
					<h1>{{ecu.mph}}</h1>
					<span class="size-letter">Speed</span>
					</div>
					</vue-svg-gauge>
				</b-col>
				<b-col>
				<vue-svg-gauge
						:start-angle="-90"
						:end-angle="90"
						:value="0"
						:separator-step="0"
						:min="0"
						:max="1"
						:transitionDuration="10"
						gauge-color="#f8f9f9"
						:scale-interval="1000"
						:inner-radius="80"
						base-color="#000000"
						class="gauge">
				<div class="inner-text">
					<h1>{{ecu.rpm}}</h1>
					<span class="size-letter">RPM</span>
				</div>
				</vue-svg-gauge>
				</b-col>
			</b-row>
		</div>
    </div>
</template>
<script>
//   import RadialGauge from 'vue-canvas-gauges/src/RadialGauge'
  import outputs from "../../mixins/outputs"

  export default {
	name: 'Blume',
    mixins: [outputs],
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
    components: {
    //   RadialGauge,
    },
    mounted(){
		this.set_dash_output()
    },
    created() {
		setInterval(this.getNow, 1000);
    },
    methods: {
		set_dash_output(){
			this.axios.get("dashboards").then(result => {
				this.slots = result.data.dashboard_outputs.filter(slot => slot.dashboard_id == 4 )
			}).catch(error => {
				console.log(error);
			})
		},
		set_output(output){
			if(!output)
				return {out: 0, percent: 0, color: "", max_value: 0}
			return {out: output["value"], percent: ((output['value'] * 100) / output['max_output']), color: "", max_value: output['max_output']}            
		},
		getNow: function() {
			const today = new Date();
			const time = today.getHours() + ":" + (today.getMinutes()<10?'0':'') + today.getMinutes()
			this.timestamp = time;
		}
	},
	computed:{
		rpm(){
			return this.set_output(this.channel_output[1])
		},
		speed(){
			return this.set_output(this.channel_output[0])
		},
		temp(){
			return this.set_output(this.channel_output[2])
		},
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
	.picture-header{
		z-index: 1;
		position: absolute;
		width: 800px;
		height: 65px;
	}
	.picture{
		z-index: 1;
		position: absolute;
		left: 10px;
		top: 70px;
		width: 785px;
		height: 340px;
	}
	.front{
		z-index: 2;
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
		right: 0px;
		font-size: 43px;
		background: #000;
		padding: 0px 18px;
		padding-top: 10px;
		border-bottom-left-radius: 30px;
		border: 1px solid #eee;
		border-top: 0px;
	}
	</style>
