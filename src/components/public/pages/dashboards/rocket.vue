<template>
    <div>
        <b-row no-gutters class="">
            <b-col class="text-center">
                <span class="switch">
                    <input id="switch1" type="checkbox" checked style=""/>
                    <span class="switch-led switch-led-green">
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    </span>
                    <span class="switch-led switch-led-red">
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    </span>
                </span>
            </b-col>
            <b-col class="text-center">
                <span class="switch">
                    <input id="switch1" type="checkbox" checked style=""/>
                    <span class="switch-led switch-led-green">
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    </span>
                    <span class="switch-led switch-led-red">
                        <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    <span class="switch-led-border">
                            <span class="switch-led-light">
                                <span class="switch-led-glow"></span>
                            </span>
                        </span>
                    </span>
                </span>
            </b-col>
        </b-row>
        <b-row no-gutters class="">
            <b-col class="text-center mt-1 max-letter">
                <h1>{{ecu.rpm}}</h1>
            </b-col>
        </b-row>
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
.normal-letter{
  font-size: 20px;
}
.max-letter {
  font-size: 100px;
}
.min-letter {
  font-size: 15px;
}

body {
	font-family: arial, verdana, sans-serif;
	font-size: 8px;
	background: #1E1E20 !important;
	text-align: center;
}

.switch {
	display: inline-block;
	margin: 10em 2em;
	position: relative;
	border-radius: 3.5em;
	-webkit-box-shadow: 0 0 0.5em rgba(255,255,255,0.2);
	-moz-box-shadow: 0 0 0.5em rgba(255,255,255,0.2);
	box-shadow: 0 0 0.5em rgba(255,255,255,0.2);
}

.switch span {
	display: block;
	-webkit-transition: top 0.2s;
	-moz-transition: top 0.2s;
	-ms-transition: top 0.2s;
	-o-transition: top 0.2s;
	transition: top 0.2s;
}

.switch-handle-left,
.switch-handle-right {
	content: '';
	display: block;
	width: 3.6em;
	height: 0;
	position: absolute;
	top: 6.6em;
	z-index: 2;
	border-bottom: 4.5em solid #111;
	border-left: 0.7em solid transparent;
	border-right: 0.7em solid transparent;
	border-radius: 0;
}


.switch-handle-base {
	width: 4.2em;
	height: 4.2em;
	position: absolute;
	top: 3.8em;
	left: 1.2em;
	z-index: 2;
	border-top: 0.2em solid rgba(255,255,255,0.35);
	border-radius: 2.1em;
	-webkit-box-shadow: 0 0 0.5em rgba(0,0,0,0.8) inset;
	-moz-box-shadow: 0 0 0.5em rgba(0,0,0,0.8) inset;
	box-shadow: 0 0 0.5em rgba(0,0,0,0.8) inset;
}

.switch-led {
	position: absolute;
	left: 2em;
	border-radius: 1.4em;
}

.switch-led-border {
	border: 0.2em solid black;
	border-radius: 1.3em;
}

.switch-led-light {
	border-radius: 1.1em;
	-webkit-box-shadow: 0 0 0.5em rgba(255,255,255,0.5) inset;
	-moz-box-shadow: 0 0 0.5em rgba(255,255,255,0.5) inset;
	box-shadow: 0 0 0.5em rgba(255,255,255,0.5) inset;
}

.switch-led-glow {
	width: 2em;
	height: 2em;
	position: relative;
	border-radius: 1em;
}

.switch-led-glow:before {
	content: '';
	display: block;
	width: 0.6em;
	height: 0.6em;
	position: absolute;
	top: 0.3em;
	left: 0.7em;
	background: rgba(255,255,255,0.2);
	border-radius: 0.3em;
	-webkit-box-shadow: 0 0 1em rgba(255,255,255,0.75);
	-moz-box-shadow: 0 0 1em rgba(255,255,255,0.75);
	box-shadow: 0 0 1em rgba(255,255,255,0.75);
}

.switch-led-glow:after {
	content: '';
	display: block;
	width: 0;
	height: 0;
	position: absolute;
	top: 0;
	left: 0;
	opacity: 0.2;
	filter: alpha(opacity=20);
	border: 1em solid #fff;
	border-color: transparent #fff transparent #fff;
	border-radius: 1em;
	-webkit-transform: rotate(45deg);
	-moz-transform: rotate(45deg);
	-ms-transform: rotate(45deg);
	-o-transform: rotate(45deg);
	transform: rotate(45deg);
}

.switch-led:after {
	display: block;
	width: 100%;
	position: absolute;
	left: 0;
	color: #666;
	font-family: arial, verdana, sans-serif;
	font-weight: bold;
	text-align: center;
	text-shadow: 0 0.1em rgba(0,0,0,0.7);
}

.switch-led-green:after {
	top: -1.8em;
}

.switch-led-red:after {
	bottom: -1.8em;
}

.switch-led-green {
	top: -5em;
	border-top: 0.1em solid rgba(0,161,75,0.5);
	border-bottom: 0.1em solid rgba(255,255,255,0.25);
}

.switch-led-green .switch-led-light {
	background: rgb(0,161,75);
	border: 0.1em solid rgb(0,104,56);
}

.switch-led-red {
	bottom: -5em;
	border-top: 0.1em solid rgba(237,28,36,0.2);
	border-bottom: 0.1em solid rgba(255,255,255,0.25);
	-webkit-box-shadow: 0 0 3em rgb(237,28,36);
	-moz-box-shadow: 0 0 3em rgb(237,28,36);
	box-shadow: 0 0 3em rgb(237,28,36);
}

.switch-led-red .switch-led-light {
	background: rgb(237,28,36);
	border: 0.1em solid rgb(161,30,45);
}

.switch-led-red .switch-led-glow {
	background: #fff;
	background: rgba(255, 255, 255, 0.3);
	filter: alpha(opacity=30);
}

/* Switch on */

.switch input:checked~.switch-handle-left, .switch input:checked~.switch-handle-right {
	top: 1.5em;
	border-bottom: 0;
	border-top: 4.5em solid #111;
}

.switch input:checked~.switch-handle {
	top: 1.5em;
}

.switch input:checked~.switch-handle-top  {
	top: -1em;
	border-top: 0;
	border-bottom: 0.2em solid #AEB2B3;
}

.switch input:checked~.switch-handle-bottom {
	top: 4.2em;
	border-top: 0;
	border-bottom: 0.2em solid #141414;
}

.switch input:checked~.switch-handle-base {
	top: 4.5em;
	border-top: 0;
	border-bottom: 0.2em solid rgba(255,255,255,0.35);
}

.switch input:checked~.switch-led-green {
	-webkit-box-shadow: 0 0 3em rgb(0,161,75);
	-moz-box-shadow: 0 0 3em rgb(0,161,75);
	box-shadow: 0 0 3em rgb(0,161,75);
}

.switch input:checked~.switch-led-green .switch-led-glow {
	background: #fff;
	background: rgba(255, 255, 255, 0.4);
	filter: alpha(opacity=40);
}

.switch input:checked~.switch-led-red {
	-webkit-box-shadow: none;
	-moz-box-shadow: none;
	box-shadow: none;
}

.switch input:checked~.switch-led-red .switch-led-glow {
	background: rgba(255, 255, 255, 0);
	filter: alpha(opacity=0);
}
</style>
