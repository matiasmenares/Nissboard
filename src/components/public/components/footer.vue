<template>
    <v-footer absolute class="font-weight-medium">
            <v-bottom-sheet v-model="sheet">
                <template v-slot:activator="{ on }">
                    <v-btn class="ma-2" color="red" dark v-on="on">
                        <v-icon dark>mdi-chevron-up</v-icon>
                    </v-btn>
                </template>
                <v-sheet dark class="px-3" height="200px">
                    <v-btn class="mt-6" dark color="red" @click="sheet = !sheet"><v-icon>mdi-chevron-down</v-icon></v-btn>
                    <div>
                        <b-row>
                            <b-col>
                                <v-btn @click="send_to('dashboard-cuga')"><v-icon>mdi-alpha-c-box-outline</v-icon> Dashboard Cuga</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to('dashboard-kinek')"><v-icon>mdi-alpha-k-box-outline</v-icon> Dashboard Kinek</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to('dashboard-rocket')"><v-icon>mdi-alpha-k-box-outline</v-icon> Dashboard Rocket</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to('dashboard-blume')"><v-icon>mdi-alpha-k-box-outline</v-icon> Dashboard Blume</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to('graph-rpm')"><v-icon>mdi-chart-line</v-icon> Gráficos</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to()"><v-icon>mdi-tune</v-icon> Alertas</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to('setting-main')"><v-icon>mdi-tune</v-icon> Configuración</v-btn>
                            </b-col>
                        </b-row>
                    </div>
                </v-sheet>
            </v-bottom-sheet>
            <v-spacer></v-spacer>
            Nissboard V 0.3 BETA
        </v-footer>
</template>
<script>
import Menu from "./menu";
export default {
    name: "Footer",
    data(){
        return{
            sheet: false,
        }
    },
    component:{
        'v-menu': Menu,
    },
    methods:{
        send_to(name){
            this.sheet = false
            this.$router.push({ name: name, params: {}});
        }
    }
}
</script>