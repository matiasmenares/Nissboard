import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Line,
  mixins: [reactiveProp],
  props: ['options', 'datacollection'],
  data () {
	return {
		gradient: null,
		gradient2: null,
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
