<template>
  <div>
  <v-card>
    <v-tabs color="accent-4" left>
        <v-tab @click="hide">Básic</v-tab>
        <v-tab @click="hide">Conditions</v-tab>
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
                                        <v-select v-model="form.alarm_type_id" :items="alarm_types" item-text="name" item-value="id" :rules="[v => !!v || 'Alert Type is required']" label="Alert Type" @focus="hide" required autocomplete="off" />
                                    </v-col>
                                    <v-col cols="4">
                                        <v-text-field v-model="form.life_second" :counter="10" :rules="nameRules"  label="Life Second" required  @focus="show" data-layout="numeric" autocomplete="off"/>
                                    </v-col>
                                </v-row>
                                <v-row align="center">
                                    <v-col cols="12">
                                        <v-text-field v-model="form.description" :counter="10" :rules="nameRules"  label="Alarm Text" required  @focus="show" data-layout="normal" autocomplete="off" />
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
                                <v-select v-model="condition_form.channel_output_id" :items="channel_outputs" item-text="name" item-value="id" :rules="[v => !!v || 'Alert Type is required']" label="Output Channel" @focus="hide" required autocomplete="off" />
                            </v-col>
                            <v-col>
                                <v-select v-model="condition_form.condition_id" :items="conditions" :item-text="with_measure" item-value="id"  :rules="[v => !!v || 'Alert Type is required']" label="Condition" @focus="hide" required autocomplete="off" />
                            </v-col>
                            <v-col>
                                <v-text-field v-model="condition_form.value" :label="measure_text ? measure_text : 'Value'" required  @focus="show"  data-layout="numeric" />
                            </v-col>
                            <v-col>
                                <v-btn class="mr-4" @click="add_condition()" ><v-icon>mdi-plus-thick</v-icon>  Add</v-btn>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-col>
                <hr>
            </v-row>
            <v-row>
                <v-col>
                    <v-data-table :headers="headers" :items="conditions_table" :items-per-page="5" class="elevation-1" ></v-data-table>
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
    name: "inputs",
    props:{
        alarm: {default: null},
        alarm_outputs: {default: null}
    },
    data(){
        return{
            headers: [
                {
                    text: 'Output Channel',
                    align: 'start',
                    sortable: false,
                    value: 'output',
                },
                { text: 'Condition', value: 'condition' },
                { text: 'Value', value: 'value' }
            ],
            condition_form: {value: null, channel_output_id: null, condition_id: null},
            channel_outputs: [],
            alarm_types: [],
            conditions: [],
            measures: [],
            conditions_data: [],
            conditions_table: [],
            visible: false,
            layout: "normal",
            options: { useKbEvents: false, preventClickEvent: false},
            valid: true,
            output: 0,
            voltage: 0.0,
            nameRules: [
              v => !!v || 'Input is required',
              v => (v && v.length <= 100) || 'Input must be less than 100 characters',
            ],
            input: null,
            form: {
            },
        }
    },
    components:{
    },
    beforeMount(){
        this.set_outputs()
        this.set_conditions()
        this.set_alarm_types()
    },
    methods:{
        set_props(){
            if(this.alarm){
                this.form = this.alarm
                this.alarm_outputs.map(alarm_output => {
                    var output = this.channel_outputs.find(out => out.id == alarm_output.channel_output_id)
                    var condition = this.conditions.find(con => con.id == alarm_output.condition_id)
                    var measure = this.measures.find(mes => mes.id == output.measure_id)
                    this.conditions_table.push({output: output.name, condition: condition.name+" ("+condition.condition+")", value: alarm_output.value+" ("+measure.name+")" })
                })
            }
        },
        add_condition(){
            this.visible = false
            this.conditions_data.push(this.condition_form)
            let output = this.channel_outputs.find(out => out.id == this.condition_form.channel_output_id)
            let condition = this.conditions.find(con => con.id == this.condition_form.condition_id)
            this.conditions_table.push({output: output.name, condition: condition.name+" ("+condition.condition+")", value: this.condition_form.value+" ("+this.measure_text+")" })
        },
        with_measure(item){
            return item.name + " (" +item.condition+")"
        },
        set_outputs(){
            this.axios.get("/settings/channels/output").then(result => {
                this.channel_outputs = result.data.channels
                this.measures = result.data.measures
                this.set_props()
            }).catch(error => {
                console.log(error);
            })
        },
        set_conditions(){
            this.axios.get("/settings/conditions").then(result => {
                this.conditions = result.data.conditions
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
            this.axios.post("/settings/alarms",{ alarm: this.form, conditions: this.conditions_data}).then(() => {
              this.$router.push({ name: "setting-alert-list"});
            }).catch(error => {
              console.log(error);
            })
        }
    },
    watch:{
    
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