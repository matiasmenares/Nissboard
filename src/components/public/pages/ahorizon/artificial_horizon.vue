<template>
	<div id="" style="">

	<div id="container"></div>
	</div>
</template>
<script src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/691867/archer.min.js"></script>
<script>
	export default {
		components: {
		},
		data () {
			return {
				height: 350,
				size: 8,
				graphic: null,
				accelerometer: {lateral: {ms: 0.0, g: 0.0, g_calculation: 0.0}, acceleration: {ms: 0.0, g: 0.0, g_calculation: 0.0 }},
			}
		},
		mounted () {
			var svgUrl = 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/691867/artificial-horizon.archer.graphic.svg';
			var configUrl = 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/691867/artificial-horizon.archer.config.json';

			var container = document.getElementById('container');
			this.graphic = archer.create(container);
			var timer = 0;

			this.graphic.loadUrl(svgUrl, configUrl);
			let self = this
			this.graphic.on('ready', function() {
				self.graphic.view.zoomToFit();
			self.set_data()	
			setInterval(update, 10);
			
			});

			function update() {
				timer += 0.01
				self.graphic.setValue('pitch', ((Math.cos(1.57 - (self.accelerometer.lateral.g * -1)  )) * 90)); 
				self.graphic.setValue('roll', Math.sin(3.1 - self.accelerometer.acceleration.g) * 40);
				self.graphic.setValue('orientation', (timer% 360)*20 - 180 ); 
			}			
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
			},
		},
	}
</script>

<style>
body {
    margin: 0;
}

#container {
    position: absolute;
    width: 100%;
    height: 100%;
}
</style>