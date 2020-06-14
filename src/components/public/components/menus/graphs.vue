<template>
    <div>
        <b-row>
            <b-col>
                <v-btn class="mr-4" @click="send_to('graph-rpm')"><v-icon>mdi-speedometer-slow</v-icon> Rpm</v-btn>
                <v-btn class="mr-4" @click="send_to('graph-gforce')"><v-icon>mdi-circle-expand</v-icon> G-force</v-btn>
                <v-btn class="mr-4" @click="send_to('graph-channel')"><v-icon>mdi-current-ac</v-icon> Channels</v-btn>

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