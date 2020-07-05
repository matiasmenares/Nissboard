<template>
  <div>
  <v-card>
    <v-tabs color="accent-4" left>
        <v-tab @click="hide">Básic</v-tab>
        <v-tab @click="hide">LED</v-tab>
        <v-tab @click="hide">Blink</v-tab>
        <v-tab @click="hide">Confirm</v-tab>
        <v-tab-item>
            <v-container fluid>
                <v-form ref="form" v-model="valid">
                    <v-row>
                        <v-col cols="12">
                            <v-container class="py-0 mt-0">
                                <v-row align="center">
                                    <v-col cols="4">
                                        <v-text-field v-model="form.name" :counter="10" :rules="nameRules"  label="Name" required  @focus="show" data-layout="compact" autocomplete="off" />
                                    </v-col>
                                    <v-col cols="4">
                                        <v-select v-model="form.channel_output_id" :items="channel_outputs" item-text="name" item-value="id" :rules="[v => !!v || 'Alert Type is required']" label="Channel" @focus="hide" required autocomplete="off" />
                                    </v-col>
                                    <v-col cols="4">
                                        <v-text-field v-model="form.priority" :counter="10" :rules="nameRules"  label="Priority" required  @focus="show" data-layout="numeric" autocomplete="off"/>
                                    </v-col>
                                    <v-col cols="4">
                                        <v-text-field v-model="form.brightness" :counter="3" :rules="nameRules"  label="% Brigness" required  @focus="show" data-layout="numeric" autocomplete="off"/>
                                    </v-col>
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
                            <v-col>
                                <v-select v-model="led_form.led_start" :items="leds" item-text="name" item-value="id" :rules="[v => !!v || 'Alert Type is required']" label="Led Start" @focus="hide" required autocomplete="off" />
                            </v-col>
                            <v-col>
                                <v-select v-model="led_form.color_start_id" :items="colors" item-text="name" item-value="id"  :rules="[v => !!v || 'Alert Type is required']" label="Color Led Start" @focus="hide" required autocomplete="off" />
                            </v-col>
                            <v-col>
                                <v-text-field v-model="led_form.value_start" :label="measure_text ? measure_text : 'Value'" required  @focus="show"  data-layout="numeric" />
                            </v-col>
                        </v-row>
                        <v-row class="center">
                            <v-col>
                                <v-select v-model="led_form.led_end" :items="leds" item-text="name" item-value="id" :rules="[v => !!v || 'Alert Type is required']" label="Led End" @focus="hide" required autocomplete="off" />
                            </v-col>
                            <v-col>
                                <v-select v-model="led_form.color_end_id" :items="colors" item-text="name" item-value="id"  :rules="[v => !!v || 'Alert Type is required']" label="Color Led End" @focus="hide" required autocomplete="off" />
                            </v-col>
                            <v-col>
                                <v-text-field v-model="led_form.value_end" :label="measure_text ? measure_text : 'Value'" required  @focus="show"  data-layout="numeric" />
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols=12>
                                <v-btn block @click="add_led()" ><v-icon>mdi-plus-thick</v-icon>  Add</v-btn>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-col>
                <hr>
            </v-row>
            <v-row>
                <v-col>
                    <v-data-table :headers="headers" :items="led_output_table" :items-per-page="5" class="elevation-2">
                        <template v-slot:item.actions="{ item }">
                            <v-icon small @click="delete_condition(item)">mdi-delete</v-icon>
                        </template>
                    </v-data-table>
                </v-col>
            </v-row>
        </v-tab-item>
        <v-tab-item>
            <v-row>
                <v-col cols="12">
                    <v-btn block color="success" @click="save()">Save</v-btn>
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
    name: "Alerts",
    props:{
        alarm: {default: null},
        alarm_outputs: {default: null}
    },
    data(){
        return{
            headers: [
                { text: 'Led Start',  align: 'led_start'},
                { text: 'Color Start', value: 'color_start_id' },
                { text: 'Value Start', value: 'value_start' },
                { text: 'Led End',  align: 'led_end' },
                { text: 'Color End', value: 'color_end_id' },
                { text: 'Value End', value: 'value_end' },
                { text: 'Actions', value: 'actions', sortable: false }
            ],
            led_output_table: [],
            condition_form: {value: null, channel_output_id: null, condition_id: null},
            led_form: {led_start: null, led_end: null, value_start: null, value_end: null},
            led_outputs: [],
            channel_outputs: [],
            leds: [{id: 1, name: "1",},{id: 2, name: "2"}, {id: 3, name: "3"},{id: 4, name: "4"}, {id: 5, name: "5"},{id: 6, name: "6"},{id: 7, name: "7"}, {id: 8, name: "8"}],
            colors: [{id: 1, name: "Blue",},{id: 2, name: "Red"}],
            visible: false,
            layout: "normal",
            options: { useKbEvents: false, preventClickEvent: false},
            valid: true,
            nameRules: [
              v => !!v || 'Input is required',
              v => (v && v.length <= 100) || 'Input must be less than 100 characters',
            ],
            input: null,
            form: {
            },
        }
    },
    created(){
        this.set_outputs()
    },
    methods:{
        set_props(){
            if(this.alarm){
                this.form = this.alarm
                this.alarm_outputs.map(alarm_output => {
                    var output = this.channel_outputs.find(out => out.id == alarm_output.channel_output_id)
                    var condition = this.conditions.find(con => con.id == alarm_output.condition_id)
                    var measure = this.measures.find(mes => mes.id == output.measure_id)
                    this.set_data_in_table(output, condition, measure.name, alarm_output.value)
                })
            }
        },
        add_led(){
            this.visible = false
            this.set_data_in_table()
        },
        delete_condition(item) {
            const index = this.conditions_table.indexOf(item)
            confirm('Are you sure you want to delete this item?') && this.conditions_table.splice(index, 1)
        },
        set_data_in_table(){
            this.led_output_table.push({id: "", led_start: this.led_form.led_start, color_start_id: this.led_form.color_start_id, value_start: this.led_form.value_start, led_end: this.led_form.led_end, color_end_id: this.led_form.color_end_id, value_end: this.led_form.value_end })
        },
        with_measure(item){
            return item.name + " (" +item.condition+")"
        },
        set_outputs(){
            this.axios.get("/settings/channels/output").then(result => {
                this.channel_outputs = result.data.channels
                this.measures = result.data.measures
            }).catch(error => {
                console.log(error);
            })
        },
        set_conditions(){
            this.axios.get("/settings/conditions").then(result => {
                this.conditions = result.data.conditions
                this.set_props()
            }).catch(error => {
                console.log(error);
            })
        },
        set_alarm_types(){
            this.axios.get("/settings/alarm_types").then(result => {
                this.alarm_types = result.data.alarm_types
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
        accept() {
          this.hide()
        },
        save(){
            this.axios.post("/settings/leds",{ led: this.form, led_outputs: this.led_output_table}).then(() => {
              this.$router.push({ name: "setting-alert-list"});
            }).catch(error => {
              console.log(error);
            })
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
        },
        measure_text () {
            if (!this.channel_outputs || !this.measures) return null 
            let output = this.channel_outputs.find(out => out.id == this.condition_form.channel_output_id)
            if (!output) return null 
            let measure = this.measures.find(measure => output.measure_id == measure.id)
            return measure.name
        }
    }
}
</script>
<style>
@import '../../../../../../node_modules/vue-touch-keyboard/dist/vue-touch-keyboard.css';
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