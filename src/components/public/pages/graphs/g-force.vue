<template>
  <b-row>
    <b-col cols="12">
      <div class="home mt-8">
        <apexchart ref="realtimeChart1" type="line" height="350" :options="chartOptions" :series="series1" />
      </div>
    </b-col>
  </b-row>
</template>

<script>
// @ is an alias to /src
import VueApexCharts from "vue-apexcharts";

var  data1 = [],
  data2 = [];


function resetData() {
  data1 = data1.slice(data1.length - 10, data1.length);
  data2 = data2.slice(data2.length - 10, data2.length);
}

export default {
  name: "home",
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      x: 0,
			accelerometer: {lateral: {ms: 0.0, g:0.0, g_calculation: 0.0}, acceleration: {ms: 0.0, g: 0.0, g_calculation: 0.0 }},
      series1: [{ data: data1.slice() }],
      data: [],
      chartOptions: {
        chart: {
          animations: {
            enabled: true,
            easing: "linear",
            dynamicAnimation: {
              speed: 1000
            }
          },
          toolbar: {
            show: false
          },
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: "smooth"
        },

        title: {
          text: "G-Force Live Graph",
          align: "left",
            style: {
              color: '#FFFFFF'
            },
        },
        markers: {
          size: 0
        },
        xaxis: {
          type: "numeric",
          range: 30,
          labels: {
            style: {
              colors: '#FFFFFF'
            },
          }
        },
        yaxis: {
          max: 2,
          min: -2,
          labels: {
            style: {
              color: '#FFFFFF'
            },
          }
        },
        legend: {
          show: false
        }
      }
    };
  },
  mounted() {
    this.set_data();
    this.intervals();
  },
  methods: {
    set_data(){
				this.sockets.subscribe('accelerometer', (data) => {
					this.accelerometer = data;
				})
    },
    getNewSeries() {
      this.x = this.x + 1
      this.data.push({
        x: this.x,
        y: this.accelerometer.acceleration.g
      });
    },
    intervals: function() {
      var me = this;
      window.setInterval(function() {
        let self = me;
        self.getNewSeries();
        try {
          self.$refs.realtimeChart1.updateSeries([{ data: self.data }]);
        }catch(error){
          error
        }
      }, 1000);

      // every 60 seconds, we reset the data to prevent memory leaks
      window.setInterval(function() {
        resetData();
        me.$refs.realtimeChart1.updateSeries([{ data: [] }], false, true);
      }, 60000);
    }
  },
};
</script>
