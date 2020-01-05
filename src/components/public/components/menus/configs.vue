<template>
    <div>
        <b-row>
            <b-col>
                <v-btn class="mr-2" @click="send_to('setting-alert')"><v-icon>mdi-alert-outline</v-icon> Alertas</v-btn>

                <v-btn class="mr-2" @click="send_to('setting-dashboard')"><v-icon>mdi-view-dashboard-variant</v-icon> Dashboards</v-btn>

                <v-btn class="mr-2" @click="send_to('dashboard-kinek')"><v-icon>mdi-wifi</v-icon> Wifi</v-btn>

                <v-btn class="mr-2" @click="send_to('dashboard-blume')"><v-icon>mdi-account</v-icon> Account</v-btn>

                <v-btn class="mr-2" @click="shutdown()"><v-icon>mdi-power</v-icon> Shutdown</v-btn>
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
        shutdown(){
            this.axios.delete("system").then(result => {
                console.log(result)
            }).catch(error => {
                console.log(error);
            }) 
        }
    },
}
</script>