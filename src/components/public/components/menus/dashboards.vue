<template>
    <div>
        <b-row>
            <b-col>
                <v-btn class="mr-4" @click="send_to('dashboard-kinek')"><v-icon>mdi-alpha-k-box-outline</v-icon> Kinek</v-btn>

                <v-btn class="mr-4" @click="send_to('dashboard-dust')"><v-icon>mdi-alpha-k-box-outline</v-icon>  Dust</v-btn>

                <v-btn class="mr-4" @click="send_to('dashboard-init')"><v-icon>mdi-alpha-c-box-outline</v-icon> Init</v-btn>

                <v-btn class="mr-4" @click="send_to('dashboard-rocket')"><v-icon>mdi-alpha-k-box-outline</v-icon> Rocket</v-btn>

                <v-btn class="mr-4" @click="send_to('dashboard-blume')"><v-icon>mdi-alpha-k-box-outline</v-icon> Blume</v-btn>

                <v-btn class="mr-4" @click="send_to('dashboard-cuga')"><v-icon>mdi-alpha-c-box-outline</v-icon> Cuga</v-btn>
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <v-btn class="mr-4" @click="send_to('dashboard-proton')"><v-icon>mdi-alpha-c-box-outline</v-icon> Proton</v-btn>

                <v-btn class="mr-4" @click="send_to('dashboard-nebula')"><v-icon>mdi-alpha-c-box-outline</v-icon> Nebula</v-btn>
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
            this.$store.commit('hideMenu');
            this.menu = "Main"
            this.$router.push({ name: name, params: {}});
        },

    },
}
</script>