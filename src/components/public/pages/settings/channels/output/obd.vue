<template>
  <div>
  <v-card>
    <v-tabs color="accent-4" left>
        <v-tab @click="hide">Básic</v-tab>
        <v-tab @click="hide" :disabled="this.form.channel_inputs_id == null || this.form.measure_id == null">Data</v-tab>
        <v-tab @click="hide" :disabled="this.form.channel_inputs_id == null || this.form.measure_id == null">Offset</v-tab>
        <v-tab @click="hide" :disabled="this.form.channel_inputs_id == null || this.form.measure_id == null">Confirm</v-tab>
        <v-tab-item>
            <v-container fluid>
                <v-form ref="form" v-model="valid">
                    <v-row>
                        <v-col cols="12">
                            <v-container class="py-0 mt-0">
                                <v-row align="center">
                                    <v-col cols="6">
                                        <v-text-field  v-model="form.name" :counter="10" :rules="nameRules"  label="Name" required  @focus="show" data-layout="compact" autocomplete="off" />
                                    </v-col>
                                    <v-col cols="6">
                                        <v-select v-model="form.channel_inputs_id" :items="input_value" item-text="name" item-value="id" :rules="[v => !!v || 'Input sensor is required']" label="Input Sensor" @focus="hide" required autocomplete="off" />
                                    </v-col>
                                    <v-col cols="6">
                                        <v-select v-model="form.measure_groups_id" :items="unit_groups"  :rules="[v => !!v || 'Unit Group is required']" label="Unit Group" @change="set_measures()" @focus="hide" required autocomplete="off" />
                                    </v-col>
                                    <v-col cols="6">
                                        <v-select v-model="form.measure_id" :items="units"  :rules="[v => !!v || 'Unit is required']" label="Unit" @focus="hide" required autocomplete="off" />
                                    </v-col>
                                </v-row>
                                <v-row v-if="measure.description">
                                    <h3>* {{measure.description}}</h3>
                                </v-row>
                            </v-container>
                        </v-col>
                    </v-row>
                </v-form>
            </v-container>
        </v-tab-item>
        <v-tab-item>
            <v-row>
                <v-col cols="12">
                    <v-container class="py-0 mt-0">
                        <v-row align="center">
                            <v-col cols="6">
                                <v-text-field  v-model="form.output_min_val"  :label="'Output Min '+this.measure.name+' Value'" required  @focus="show"  data-layout="numeric" />
                            </v-col>
                            <v-col cols="6">
                                <v-text-field  v-model="form.output_max_val" :counter="10" :rules="nameRules"  :label="'0utput Max '+this.measure.name+' Value'" required  @focus="show"  data-layout="numeric" />
                            </v-col>
                        </v-row>
                    </v-container>
                </v-col>
            </v-row>
        </v-tab-item>
        <v-tab-item>
            <v-row>
                <v-col cols="12">
                    <v-container class="py-0 mt-0">
                        <v-row align="center">
                            <v-col cols="12">
                                <v-text-field  v-model="form.offset" label="Offset Formula" required  @focus="show" data-layout="normal" />
                            </v-col>
                        </v-row>
                    </v-container>
                </v-col>
            </v-row>
        </v-tab-item>
        <v-tab-item>
            <v-row>
            </v-row>
            <v-row>
                <v-col cols="12">
                    <v-btn block color="success" @click="save">Save</v-btn>
                </v-col>
            </v-row>
        </v-tab-item>
    </v-tabs>
    </v-card>
        <div class="mt-10" style="cursor: default;">
            <vue-touch-keyboard id="keyboard" :options="options" v-if="visible" :layout="layout" :cancel="hide" :accept="accept" :input="input" />
        </div>
    </div>
</template>
<script>
export default {
    name: "obd",
    data(){
        return{
            visible: false,
            layout: "normal",
            options: { useKbEvents: false, preventClickEvent: false},
            valid: true,
            output: 0,
            voltage: 0.0,
            analog: {turbo: { psi: {value: "0.0", raw: "0000", peak: "0.0", voltage: 0.0}, bar: {value: "0.0", raw: "0000", peak: "0.0", voltage: 0.0}}},
            nameRules: [
              v => !!v || 'Input is required',
              v => (v && v.length <= 20) || 'Input must be less than 20 characters',
            ],
            input_data: null,
            input: null,
            form_type: 2,
            form: {
                id: null,
                name: null,
                input: null,
                measure_groups_id: null,
                output_min_val: null,
                output_max_val: null,
                offset: null,
            },
            measure: {id: null, name: null, calculation: null, description: null},
            input_value: [],
            unit_groups: [],
            units: [],
        }
    },
    beforeMount(){
        this.set_inputs()
        this.set_measures_group()
    },
    mounted(){
        if (this.analog)
            this.form = this.analog;
    },
    methods:{
        set_measures_group(){
            this.axios.get("/measure_groups").then(result => {
                result.data.data.map(measure => {
                    this.unit_groups.push({text: measure[1], value: measure[0]})
                })
            }).catch(error => {
              console.log(error);
            })
        },
        set_measures(){
            this.measure.description = ""
            this.axios.get("/measures?group_id="+this.form.measure_groups_id).then(result => {
                this.units = []
                result.data.data.map(measure => {
                    this.units.push({text: measure[1], value: measure[0]})
                })
            }).catch(error => {
                console.log(error);
            })
        },
        set_linear(){
            let total = (this.form.output_max_val / 10)
            let sum = 0
            this.datacollection.datasets[0].data = [0]
            for (var _i = 0; _i < 10; _i++) {
                sum += total
                this.datacollection.datasets[0].data.push(sum);
            }
        },
        accept() {
          this.hide()
        },
        set_inputs(){
            this.axios.get("/settings/channels/input").then(result => {
                this.input_value = result.data.obd_inputs
            }).catch(error => {
              console.log(error);
            })
        },
        show(e) {
          this.input = e.target;
          this.layout = e.target.dataset.layout;
          if (!this.visible)
            this.visible = true
        },
        hide() {
          this.visible = false;
        },
        save(){
          if(this.channel){
            this.axios.patch("/settings/channels/output",{ channel: this.form, form_type: 2 }).then(() => {
              this.$router.push({ name: "setting-channel-output-list"});
            }).catch(error => {
              console.log(error);
            })
          }else{
            this.axios.post("/settings/channels/output",{ channel: this.form, form_type: 2  }).then(() => {
              this.$router.push({ name: "setting-channel-output-list"});
            }).catch(error => {
              console.log(error);
            })
          }
        }
    },
    watch:{
        "form.measure_id":{
            handler: function() {
                this.axios.post("/measures", {id: this.form.measure_id}).then(result => {
                    this.measure = {id: result.data.data[0], name: result.data.data[1], calculation: result.data.data[2], description: result.data.data[4]}
                }).catch(error => {
                    console.log(error);
                })
            }
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
@import '../../../../../../../node_modules/vue-touch-keyboard/dist/vue-touch-keyboard.css';
#keyboard {
	position: fixed;
	left: 0;
	right: 0;
	bottom: 0;

	z-index: 1000;
	width: 100%;
	max-width: 1000px;
	margin: 0 auto;

	padding: 1em;

	background-color: rgb(47, 47, 47);
	box-shadow: 0px -3px 10px rgba(black, 0.3);

	border-radius: 10px;
}
</style>