<template>
	<div class="small">
        <div id="ball1" class="csstelemetry-gball csstelemetry-center" style="height: 300px; width: 300px;"></div>
	</div>
</template>

<script>
	export default {
		components: {
		},
		data () {
			return {
				height: 350,
				gradient: null,
				gradient2: null,
				datacollection: {},
				chartOptions: {
					responsive: true,
					maintainAspectRatio: false
				}
			}
		},
		mounted () {
			let id = "ball1"
			let size = 6;
			let scale = 2;
			this.ball = document.getElementById(id);
			this.cursor = document.createElement("div");
			this.cursor.classList.add("csstelemetry-gball-cursor");
			this.cursor.style.height = size + "%";
			this.cursor.style.width = size + "%";
			this.cursor.style.margin = -(size / 2) + "% 0 0 " + -(size / 2) + "%";
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
				span.innerText = ((currentStep / 100) * scale) + "G";
				grid.appendChild(span);
				if (i % 2 != 0) {
					grid.style.borderStyle = "dashed";
				}
				this.ball.appendChild(grid);
			}
			let span = document.createElement("span");
			span.innerText = Math.trunc(this.scale) + "G";
			this.ball.appendChild(span);
			this.showForce(20,10)           
		},
		methods: {
			showForce(xAxis, yAxis) {
				let angle = Math.atan(yAxis / xAxis);
				let maxY = Math.sin(angle) * this.scale;
				let maxX = Math.cos(angle) * this.scale;
				let res = [(Math.abs(xAxis) > Math.abs(maxX)) ? maxX : xAxis, (Math.abs(yAxis) > Math.abs(maxY)) ? maxY : yAxis];
				this.cursor.style.left = 50 + ((50 - (this.size / 2)) * res[0]) / this.scale + "%";
				this.cursor.style.top = 50 + ((50 - (this.size / 2)) * res[1]) / this.scale + "%";
			}
		},
		computed: {

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
  transition: 500ms;
}
</style>