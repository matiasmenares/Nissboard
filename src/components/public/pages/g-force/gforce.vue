<template>
	<div style="margin-top: 20px; width: 90%; margin-left: auto; margin-right: auto">
		<table style="width: 100%">
		<tr>
			<th style="vertical-align: top;">
				<h1>{{Math.abs(accelerometer.lateral.g)}} G</h1>
				<h3>Lateral</h3>
			</th>
			<th rowspan="4">
				<div id="ball1" class="csstelemetry-gball csstelemetry-center" style="height: 380px; width: 380px;"></div>
			</th>
			<th style="vertical-align: top;">
				<h1>{{Math.abs(accelerometer.acceleration.g)}} G</h1>
				<h3>Acceleration</h3>
			</th>
		</tr>
		<tr>
			<th style="vertical-align: bottom;">
				<h4>{{max_g.right}} G</h4>
				<h5>Right</h5>
			</th>
			<th style="vertical-align: bottom;">
				<h4>{{max_g.acc}} G</h4>
				<h5>Acceleration</h5>
			</th>
		</tr>
		<tr>
			<th style="vertical-align: bottom;">
				<h4>{{max_g.latetal}} G</h4>
				<h5>Left</h5>

			</th>
			<th style="vertical-align: bottom;">
				<h4>{{max_g.brake}} G</h4>
				<h5>Brake</h5>

			</th>
		</tr>
		<tr>
			<th style="vertical-align: bottom;">
				<h1>{{max_g.latetal}} G</h1>
				<h4>Peak Lateral</h4>
			</th>
			<th style="vertical-align: bottom;">
				<h1>{{max_g.acceleration}} G</h1>
				<h4>Peak Acceleration</h4>
			</th>
		</tr>
		</table>
	</div>
</template>

<script>
	export default {
		components: {
		},
		data () {
			return {
				height: 350,
				size: 8,
				scale: 2,
				gradient: null,
				gradient2: null,
				datacollection: {},
				accelerometer: {lateral: {ms: 0.0, g:0.0, g_calculation: 0.0}, acceleration: {ms: 0.0, g: 0.0, g_calculation: 0.0 }},
				max_g: {latetal: 0.0, acceleration: 0.0, left: 0.0, right: 0.0, acc: 0.0, brake: 0.0 }
			}
		},
		mounted () {
			this.set_data();
			let id = "ball1"
			this.ball = document.getElementById(id);
			this.cursor = document.createElement("div");
			this.cursor.classList.add("csstelemetry-gball-cursor");
			this.cursor.style.height = this.size + "%";
			this.cursor.style.width = this.size + "%";
			this.cursor.style.margin = -(this.size / 2) + "% 0 0 " + -(this.size / 2) + "%";
			this.ball.appendChild(this.cursor);
			/*Scale*/
			const steps = 3
			for (let i = steps; i > 0; i--) {
				let currentStep = (25 * i);
				let grid = document.createElement("div");
				grid.classList.add("csstelemetry-gball");
				grid.classList.add("csstelemetry-gball-rect");
				grid.style.width = grid.style.height = currentStep + "%";
				grid.style.margin = -(currentStep / 2) + "% 0 0 " + -(currentStep / 2) + "%";
				let span = document.createElement("span");
				span.innerText = ((currentStep / 100) * this.scale) + "G";
				grid.appendChild(span);
				if (i % 2 != 0) {
					grid.style.borderStyle = "dashed";
				}
				this.ball.appendChild(grid);
			}
			let span = document.createElement("span");
			span.innerText = Math.trunc(this.scale) + "G";
			this.ball.appendChild(span);
			this.showForce(0,0);
		},
		methods: {
			showForce(xAxis, yAxis) {
				let angle = Math.atan(yAxis / xAxis);
				let maxY = Math.sin(angle) * this.scale;
				let maxX = Math.cos(angle) * this.scale;
				let res = [(Math.abs(xAxis) > Math.abs(maxX)) ? maxX : xAxis, (Math.abs(yAxis) > Math.abs(maxY)) ? maxY : yAxis];
				this.cursor.style.left = 50 + ((50 - (this.size / 2)) * res[0]) / this.scale + "%";
				this.cursor.style.top = 50 + ((50 - (this.size / 2)) * res[1]) / this.scale + "%";
			},
			set_data(){
				this.sockets.subscribe('accelerometer', (data) => {
					this.accelerometer = data;
				})
			}
		},
		watch: {
			"accelerometer.lateral.ms": {
				handler: function() {
					
					if(this.accelerometer.lateral.g > 0.1 || this.accelerometer.lateral.g < -0.1){
						this.accelerometer.lateral.g = this.accelerometer.lateral.g;
					}else{
						this.accelerometer.lateral.g = 0.0
					}
					if(this.accelerometer.acceleration.g > 0.1 || this.accelerometer.acceleration.g < -0.1){
						this.accelerometer.acceleration.g = this.accelerometer.acceleration.g;
					}else{
						this.accelerometer.acceleration.g = 0.0
					}

					if(Math.abs(this.accelerometer.lateral.g) > this.max_g.latetal){
						if(Math.abs(this.accelerometer.lateral.g) < 4.0){
							this.max_g.latetal = Math.abs(this.accelerometer.lateral.g)
						}
					}

					if(Math.abs(this.accelerometer.acceleration.g) > this.max_g.acceleration){
						if(Math.abs(this.accelerometer.acceleration.g) < 4.0){
							this.max_g.acceleration = Math.abs(this.accelerometer.acceleration.g)
						}
					}

					if(this.accelerometer.lateral.g < 0.0){
						//Right
						if(Math.abs(this.accelerometer.lateral.g) > this.max_g.right){
							if(Math.abs(this.accelerometer.lateral.g) < 4.0){
								this.max_g.right = Math.abs(this.accelerometer.lateral.g)
							}
						}
					}

					if(this.accelerometer.lateral.g > 0.0){
						//Left
						if(Math.abs(this.accelerometer.lateral.g) > this.max_g.left){
							if(Math.abs(this.accelerometer.lateral.g) < 4.0){
								this.max_g.left = Math.abs(this.accelerometer.lateral.g)
							}
						}
					}

					if(this.accelerometer.acceleration.g > 0.0){
						//Acceleration
						if(Math.abs(this.accelerometer.acceleration.g) > this.max_g.acc){
							if(Math.abs(this.accelerometer.acceleration.g) < 4.0){
								this.max_g.acc = Math.abs(this.accelerometer.acceleration.g)
							}
						}
					}


					if(this.accelerometer.acceleration.g < 0.0){
						//Brake
						if(Math.abs(this.accelerometer.acceleration.g) > this.max_g.brake){
							if(Math.abs(this.accelerometer.acceleration.g) < 4.0){
								this.max_g.brake = Math.abs(this.accelerometer.acceleration.g)
							}
						}
					}
					this.showForce((this.accelerometer.lateral.g * - 1.0), this.accelerometer.acceleration.g)
				}
			},
		}
	}
</script>

<style>
.csstelemetry-gball {
  position: relative;
  border-radius: 50%;
  background: black;
  border: 1px solid white;
  color: #ffff;
  font-size: 100%;
  text-align: center;
}

.csstelemetry-center {
	margin: 0 auto;
}

.csstelemetry-right {
	margin: auto 0 0 auto;
}

.csstelemetry-left {
	margin: 0 auto auto 0;
}

.csstelemetry-gball-cursor{
  position: absolute;
  border-radius: 50%;
  background: red;
  top: 50%;
  left: 50%;
  z-index: 9999999;
}

.csstelemetry-gball-rect{
  position: absolute;
  background: transparent;
  top: 50%;
  left: 50%;
}

.csstelemetry-gball-cursor{
  transition: 300ms;
}
</style>