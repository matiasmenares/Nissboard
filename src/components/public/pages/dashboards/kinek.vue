<template>
      <div>
        <b-row>
            <v-container>
                <v-progress-linear
                    :active="active"
                    :background-opacity="opacity"
                    :bottom="bottom"
                    :buffer-value="buffer"
                    :height="80"
                    :indeterminate="indeterminate"
                    :query="query"
                    :rounded="rounded"
                    :stream="stream"
                    :striped="striped"
                    :top="top"
                    :value="20"
                    color="light-blue"
                ></v-progress-linear>
                </v-container>
        </b-row>
        <b-row>
            <b-col class="text-center mt-5 size-letter">
                <h1>{{ecu.rpm}}</h1>
            </b-col>
        </b-row>
    </div>
</template>
<script>
  export default {
    name: 'Kinek',
    data(){
        return{
            sheet: false,
            ecu: {rpm: 0, mph: 0, temp: 0},
        }
    },
    components: {
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
                    this.color.rpm.gaugue = "#7FFF22"
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
.size-letter {
  font-size: 40px;
}
</style>
