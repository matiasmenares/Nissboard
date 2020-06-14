<template>
  <b-row class="mt-8">
    <b-col cols="9">
      <div class="home">
        <apexchart ref="realtimeChart1" type="line" height="350" :options="chartOptions" :series="series1" />
      </div>
    </b-col>
    <b-col cols="3">
        <v-select v-model="output_selected_id" :items="outputs" item-text="name" item-value="id" :rules="[v => !!v || 'Alert Type is required']" label="Channel" required autocomplete="off" />
        <h1>{{this.channel_selected.value}} <small>{{this.channel_selected.measure}}</small></h1>
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
  name: "output",
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      x: 0,
      channel_output: [],
      outputs: [],
      measures: [],
      output_selected_id: 1,
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
          text: "Boost Live Graph (Rate 1 Hz)",
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
          max: 20,
          min: -20,
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
    this.set_channel_output();
    this.intervals();
    this.set_outputs();
  },
  methods: {
    set_outputs(){
        this.axios.get("/settings/channels/output").then(result => {
            this.outputs = result.data.channels
            this.measures = result.data.measures
        }).catch(error => {
            console.log(error);
        })
    },
    set_channel_output(){
        this.sockets.subscribe('channelOutput', (data) => {
            this.channel_output = data
        })
    },
    getNewSeries() {
      this.x = this.x + 1
      this.data.push({
        x: this.x,
        y: this.channel_selected.value
      });
    },
    intervals: function() {
      var me = this;
      window.setInterval(function() {
        let self = me;
        self.getNewSeries();
        try {
            self.$refs.realtimeChart1.updateSeries([{ data: self.data }]);
        } catch (error) {
            error
        }
      }, 900);

      // every 60 seconds, we reset the data to prevent memory leaks
      window.setInterval(function() {
        resetData();
            try {
                me.$refs.realtimeChart1.updateSeries([{ data: [] }], false, true);
            } catch (error) {
                error
            }
        }, 60000);
    }
  },
  computed:{
    channel_selected: function () {
        return this.channel_output.find(out => out.id == this.output_selected_id)
    }
  }
};
</script>
