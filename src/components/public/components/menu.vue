<template>
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
                        <v-icon class="mr-2">fas fa-tachometer-alt</v-icon>Dashboard
                        <v-icon class="mr-2">mdi-history</v-icon>Graficos
                        <v-icon class="mr-2">mdi-history</v-icon>Configuración
                    </b-col>
                </b-row>
            </div>
        </v-sheet>
    </v-bottom-sheet>
</template>
<script>
  export default {
    name: 'Menu',
    data(){
        return{
            sheet: false,
        }
    },
    methods:{
        send_to_chart_rpm(){
            this.$router.push({ name: 'vehicles-financing-success', params: {customer: this.solicitude, simulation: this.simulation}});
        }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
