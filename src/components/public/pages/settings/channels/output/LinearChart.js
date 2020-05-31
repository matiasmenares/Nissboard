import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Line,
  mixins: [reactiveProp],
  props: ['options'],
  data () {
	return {
		gradient: null,
		gradient2: null,
		datacollection: {}
	}
  },
  mounted () {
	this.gradient = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450);
	this.gradient2 = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450);
	this.gradient.addColorStop(0, 'rgba(255, 0,0, 0.5)')
	this.gradient.addColorStop(0.5, 'rgba(255, 0, 0, 0.25)');
	this.gradient.addColorStop(1, 'rgba(255, 0, 0, 0)');

	this.gradient2.addColorStop(0, 'rgba(0, 231, 255, 0.9)')
	this.gradient2.addColorStop(0.5, 'rgba(0, 231, 255, 0.25)');
	this.gradient2.addColorStop(1, 'rgba(0, 231, 255, 0)');
	this.datacollection = {
		labels: [1, 2, 3, 4, 6],
		datasets: [
			{
				label: 'Rpm',
				backgroundColor: this.gradient,
				borderColor: '#FC2525', 
				pointBackgroundColor: '#FC2525', 
				borderWidth: 2, 
				pointBorderColor: '#FC2525',
				data: [800, 3000, this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
			}
			// }, {
			// 	label: 'Speed',
			// 	backgroundColor: this.gradient2,
			// 	borderColor: 'rgb(0, 231, 255)', 
			// 	pointBackgroundColor: 'rgb(0, 231, 255)', 
			// 	borderWidth: 2, 
			// 	pointBorderColor: 'rgb(0, 231, 255)',
			// 	data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
			// }
		]
	};
    // this.chartData is created in the mixin.
	// If you want to pass options please create a local options object
    this.renderChart(this.datacollection, this.options)
  },
  methods: {
	getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 9000
      }
  }
}
