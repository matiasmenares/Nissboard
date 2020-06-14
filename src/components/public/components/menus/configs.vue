<template>
    <div>
        <b-row>
            <b-col>
                <v-btn class="mr-2" @click="send_to('setting-alert-list')"><v-icon>mdi-alert-outline</v-icon> Alerts</v-btn>

                <v-btn class="mr-2" @click="send_to('setting-dashboard')"><v-icon>mdi-speedometer-slow</v-icon> Dash</v-btn>

                <v-btn class="mr-2" @click="send_to('setting-channel-list')"><v-icon>mdi-current-ac</v-icon> Channel Input</v-btn>

                <v-btn class="mr-2" @click="send_to('setting-channel-output-list')"><v-icon>mdi-current-ac</v-icon> Channel Output</v-btn>

                <v-btn class="mr-2" @click="send_to('dashboard-kinek')"><v-icon>mdi-wifi</v-icon> Wifi</v-btn>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <v-btn class="mr-2" @click="send_to('setting-screen')"><v-icon>mdi-overscan</v-icon> Screen</v-btn>

                <v-btn class="mr-2" @click="send_to('dashboard-blume')"><v-icon>mdi-account</v-icon> Account</v-btn>

                <v-btn class="mr-2" @click="off('shutdown')"><v-icon>mdi-power</v-icon> Shutdown</v-btn>

                <v-btn class="mr-2" @click="off('reboot')"><v-icon>mdi-power</v-icon> Reboot</v-btn>
            </b-col>
        </b-row>
    </div>
</template>
<script>
export default {
    name: "dashboards",
    data(){
        return{
            sheet: false,
        }
    },
    props:{
        menu: {type: String}
    },
    components:{
    },
    mounted(){
    },
    methods:{
        send_to(name){
            this.sheet = false
            this.menu = "Main"
            this.$router.push({ name: name, params: {}});
        },
        off(action){
            this.axios.delete("system",{action: action}).then(() => {
            }).catch(error => {
                console.log(error);
            }) 
        },
    },
}
</script>