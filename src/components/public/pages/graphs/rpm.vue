<template>
    <div>    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/></div>
</template>
<script>
import { Bar } from 'vue-chartjs'
// import {Chart} from 'highcharts-vue'
  export default {
    name: 'Menu',
    extends: Bar,
    data(){
        return {
            chartOptions: {
                title: {text: "Gráficos de RPM"},
                series: [{
                data: [1,2,3,5,6,6,7,8,8,9,10,22,2,3,4,5]
                }]
            },
            chartdata: {
                labels: ['January', 'February'],
                datasets: [
                    {
                    label: 'Data One',
                    backgroundColor: '#f87979',
                    data: [40, 20]
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        }
    },
  mounted () {
    this.renderChart(this.chartdata, this.options)
  },
    components: {
        // highcharts: Chart 
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
