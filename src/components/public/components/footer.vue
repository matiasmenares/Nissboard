<template>
    <v-footer absolute class="font-weight-medium">
        <v-spacer></v-spacer>
            <v-bottom-sheet v-model="sheet">
                <template v-slot:activator="{ on }">
                    <v-btn class="ma-2" color="red" dark v-on="on">
                        <v-icon dark>mdi-wrench</v-icon>
                    </v-btn>
                </template>
                <v-sheet dark class="text-center" height="200px">
                    <v-btn class="mt-6" text color="red" @click="sheet = !sheet">Cerrar</v-btn>
                    <div>
                        <b-row>
                            <b-col>
                                <v-btn @click="send_to_dashboard('dashboard-cuga')"><v-icon>fas fa-tachometer-alt</v-icon>Dashboard Cuga</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to_dashboard('dashboard-kinek')"><v-icon>fas fa-tachometer-alt</v-icon>Dashboard Kinek</v-btn>
                            </b-col>
                            <b-col>
                                <v-btn @click="send_to_chart_rpm()"><v-icon>fas fa-tachometer-alt</v-icon>Gráficos</v-btn>
                            </b-col>
                            <b-col>
                                <v-icon>mdi-history</v-icon>Configuración
                            </b-col>
                        </b-row>
                    </div>
                </v-sheet>
            </v-bottom-sheet>
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
        send_to_chart_rpm(){
            this.sheet = false
            this.$router.push({ name: 'graph-rpm', params: {}});
        },
        send_to_dashboard(dash_name){
            this.sheet = false
            this.$router.push({ name: dash_name, params: {}});
        }
    }
}
</script>