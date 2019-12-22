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
            <div class=" text-center">
                <v-icon class="text-color-success">mdi-access-point-network</v-icon><v-icon class="text-color-warning">mdi-satellite-variant</v-icon>
            </div>
            <v-spacer></v-spacer>
            <span class="min-letter">Nissboard V 0.3</span>
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