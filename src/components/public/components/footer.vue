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
                    <v-btn v-if="this.menu != 'Main'" class="mt-6 ml-3" dark color="red" @click="define_menu('Main')"><v-icon>mdi-chevron-left</v-icon></v-btn>
                    <div v-if="this.menu =='Main'">
                        <b-row>
                            <b-col>
                                <v-btn class="mr-2" @click="define_menu('Dashboard')"><v-icon>mdi-view-dashboard-variant</v-icon> Dash</v-btn>
                                <v-btn class="mr-2" @click="send_to('graph-rpm')"><v-icon>mdi-chart-line</v-icon> Gráficos</v-btn>
                                <v-btn class="mr-2" @click="send_to()"><v-icon>mdi-alert-outline</v-icon> Alertas</v-btn>
                                <v-btn class="mr-2" @click="send_to()"><v-icon>mdi-racing-helmet</v-icon> Race</v-btn>
                                <v-btn class="mr-2" @click="send_to('g-force-gforce')"><v-icon>mdi-rotate-orbit</v-icon> G-force</v-btn>
                                <v-btn @click="send_to()" class="mr-2"><v-icon>mdi-go-kart-track</v-icon> Track</v-btn>
                            </b-col>
                        </b-row>
                        <b-row>
                            <b-col>
                                <v-btn @click="define_menu('Config')"><v-icon>mdi-settings-outline</v-icon> Configuración</v-btn>
                            </b-col>
                        </b-row>
                    </div>
                    <menu-dashboards v-if="menu == 'Dashboard'" :menu="menu"></menu-dashboards>
                    <menu-configs v-if="menu == 'Config'" :menu="menu"></menu-configs>
                </v-sheet>
            </v-bottom-sheet>
            <v-spacer></v-spacer>
            <div class="mx-12 text-center">
                <v-icon :class="icons.ecu.color">mdi-access-point-network</v-icon>
                <v-icon :class="icons.gps.color">mdi-satellite-variant</v-icon>
                <v-icon :class="icons.internet.color">{{icons.internet.icon}}</v-icon>
            </div>
            <span class="min-letter">Nissboard <small>v 0.4</small></span>
        </v-footer>
</template>
<script>
import MenuDashboard from "./menus/dashboards";
import MenuConfig from "./menus/configs";

export default {
    name: "Footer",
    data(){
        return{
            menu: "Main",
            sheet: false,
            icons: { ecu: {color: "text-color-warning"}, gps: {color: "text-color-warning"}, internet: {color: "text-color-warning", icon: "mdi-wifi-strength-outline"}},
            ecu_connection: {status: false},
            internet_connection: {status: false}
        }
    },
    components:{
        'menu-dashboards': MenuDashboard,
        'menu-configs': MenuConfig
    },
    mounted(){
        this.connections()
    },
    methods:{
        send_to(name){
            this.sheet = false
            this.$router.push({ name: name, params: {}});
        },
        define_menu(menu){
            this.menu = menu;
        },
        connections(){
            this.sockets.subscribe('ecuConnection', (data) => {
                this.ecu_connection = data;
            })
            this.sockets.subscribe('InternetConnection', (data) => {
                this.internet_connection = data;
            })
        }

    },
    watch:{
        "ecu_connection": {
            handler: function() {
                if (this.ecu_connection.status){
                    this.icons.ecu.color =  "text-color-success"
                }else{
                    this.icons.ecu.color =  "text-color-warning"
                }
            }
        },
        "internet_connection": {
            handler: function() {
                if (this.internet_connection.status){
                    this.icons.internet.icon = "mdi-wifi"
                    this.icons.internet.color =  "text-color-success"
                }else{
                    this.icons.internet.icon = "mdi-wifi-strength-outline"
                    this.icons.internet.color =  "text-color-warning"
                }
            }
        },
    }
}
</script>
<style scoped>
.text-color-warning{
    color: rgba(255, 255, 0, 0.753);
}
.text-color-success{
    color: rgb(0, 170, 0);
}
.min-letter {
  font-size: 15px;
}
</style>