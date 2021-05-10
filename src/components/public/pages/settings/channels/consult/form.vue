<template>
  <div>
  <v-card>
    <v-tabs color="accent-4" left>
      <v-tab>Nissan Consult Inputs</v-tab>
      <v-tab-item >
        <v-container fluid>
          <v-row>
            <v-col cols="12">
                <v-container class="py-0 mt-0">
                  <v-row align="center">
                    <v-col cols="12">
                      <v-form ref="form" v-model="valid"  >
                          <v-text-field  v-model="form.name" :counter="10" :rules="nameRules"  label="Name" required  @focus="show" data-layout="normal" />
                          <v-select v-model="form.obd_id" :items="obd_values" item-text="name" item-value="id" :rules="[v => !!v || 'OBD value type is required']" label="OBD Input" @focus="hide" required />
                      </v-form>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="12" v-if="this.obd_description">
                      <p><b>Input Description:</b> {{this.obd_description}}</p>
                    </v-col>
                    <v-col>
                      <v-btn color="success" @click="save"> Save</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
    </v-tabs>
  </v-card>
    <div class="mt-10" style="cursor: default;">
        <vue-touch-keyboard id="keyboard" :options="options" v-if="visible" :layout="layout" :cancel="hide" :accept="accept" :input="input" />
    </div >
  </div>
</template>
<script>
export default {
    name: "inputs",
    props:{
      analog: { pin: null, input: null, name: null, id: null }
    },
    data(){
        return{
            visible: false,
            layout: "normal",
            options: { useKbEvents: false, preventClickEvent: false},
            valid: true,
            nameRules: [
              v => !!v || 'Name is required',
              v => (v && v.length <= 20) || 'Name must be less than 20 characters',
            ],
            form: { obd: null, name: null, id: null },
            obd_values: []
        }
    },
    components:{
    },
    mounted(){
      this.set_obd_channels()
      if (this.analog)
        this.form = this.analog;
    },
    methods:{
        set_obd_channels(){
            this.axios.get("/settings/channels/input/obd").then(result => {
              this.obd_values = result.data.obd
            }).catch(error =>{
              console.log(error)
            })
        },
        accept() {
          this.hide()
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
          if(this.analog){
            this.axios.patch("/settings/channels/input/obd",{ obd: this.form }).then(result => {
              console.log(result);
              this.$router.push({ name: "setting-channel-list"});
            }).catch(error => {
              console.log(error);
            })
          }else{
            this.axios.post("/settings/channels/input/obd",{ obd: this.form }).then(result => {
              console.log(result);
              this.$router.push({ name: "setting-channel-list"});
            }).catch(error => {
              console.log(error);
            })
          }
        }
    },
    computed:{
      obd_description(){
        let desc = this.obd_values.find(obd => this.form.obd_id == obd.id)
        return desc ? desc.description : ''
      }
    },
    watch: {
        "analog": {
            handler: function(){
              console.log(this.analog);
              this.form = this.analog;
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