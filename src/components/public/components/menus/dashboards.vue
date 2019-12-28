<template>
    <div>
        <b-row>
            <b-col>
                <v-btn @click="send_to('dashboard-cuga')"><v-icon>mdi-alpha-c-box-outline</v-icon> Cuga</v-btn>
            </b-col>
            <b-col>
                <v-btn @click="send_to('dashboard-kinek')"><v-icon>mdi-alpha-k-box-outline</v-icon> Kinek</v-btn>
            </b-col>
            <b-col>
                <v-btn @click="send_to('dashboard-rocket')"><v-icon>mdi-alpha-k-box-outline</v-icon> Rocket</v-btn>
            </b-col>
            <b-col>
                <v-btn @click="send_to('dashboard-blume')"><v-icon>mdi-alpha-k-box-outline</v-icon> Blume</v-btn>
            </b-col>
            <b-col>
                <v-btn @click="send_to('dashboard-dust')"><v-icon>mdi-alpha-k-box-outline</v-icon>  Dust</v-btn>
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

    },
}
</script>