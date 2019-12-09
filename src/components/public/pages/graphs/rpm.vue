<template>
	<div class="small">
		<line-chart :chart-data="datacollection" :options="chartOptions" :styles="myStyles"></line-chart>
	</div>
</template>

<script>
	import LineChart from './LineChart.js'

	export default {
		components: {
			LineChart
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
			//this.fillData();
		},
		methods: {
			fillData () {
				this.datacollection = {
					labels: [this.getRandomInt(), this.getRandomInt()],
					datasets: [
						{
							data: [this.getRandomInt(), this.getRandomInt()]
						}, {
							data: [this.getRandomInt(), this.getRandomInt()]
						}
					]
				}
			},
			getRandomInt () {
				return Math.floor(Math.random() * (50 - 5 + 1)) + 5
			}
		},
		computed: {
			myStyles () {
				let calculatedHeight = this.height;
				if (document.getElementById('car-alert')){
					calculatedHeight = this.height - document.getElementById('car-alert').offsetHeight;
				}
				return {
					height: `${calculatedHeight}px`,
					position: 'relative'
				}
			}
		}
	}
</script>

<style>
	.small {
		max-width: 740px;
		margin:  50px auto;
	}
</style>