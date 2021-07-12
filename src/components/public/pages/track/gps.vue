
<template>
      <div id="init-div"> 
        <b-row no-gutters class="mt-5">
            <b-col class="text-center" v-if="gps.lat != false">
                <span class="max-letter">{{gps.lat}}</span> <span class="min-letter">Latitude</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
        </b-row>
        <b-row no-gutters class="mt-10">
            <b-col class="text-center" v-if="gps.lon != false">
                <span class="max-letter">{{gps.lon}} </span> <span class="min-letter">Longitude</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
        </b-row>
        <b-row no-gutters class="mt-10">
            <b-col class="text-center" v-if="gps.sat_numbers != false">
                <span class="max-letter">{{gps.sat_numbers}} </span> <span class="min-letter">Satelites</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center" v-if="gps.altitude != false">
                <span class="max-letter">{{gps.altitude}}</span> <span class="min-letter">({{gps.altitude_unit}}) Altitude </span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center" v-if="gps.lat_dir != false">
                <span class="max-letter">{{gps.lat_dir}}</span> <span class="min-letter">Latitude Dir</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center" v-if="gps.lon_dir != false">
                <span class="max-letter">{{gps.lon_dir}}</span> <span class="min-letter">Longitude Dir</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
        </b-row>
        <b-row no-gutters class="mt-10">
            <b-col class="text-center" v-if="gps.timestamp != false">
                <span class="max-letter">{{gps.speed}}</span> <span class="min-letter">Speed</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
            <b-col class="text-center" v-if="gps.timestamp != false">
                <span class="max-letter">{{gps.timestamp}}</span> <span class="min-letter">TimeStamp</span>
            </b-col>
            <b-col class="text-center  mt-12 normal-letter" v-else>
                <h1>- -</h1>
            </b-col>
        </b-row>
    </div>
</template>
<script>
	export default {
		components: {
		},
		data () {
			return {
                gps: {lat: false, lat_dir: false, lon: false, lon_dir: false, altitude: false, altitude_long: false, sat_numbers: false}
			}
		},
		mounted () {
			this.set_data()	
		},
		methods: {
			set_data(){
				this.sockets.subscribe('gps', (data) => {
					this.gps = data;
				})
			},
		},
	}
</script>

<style>
.normal-letter{
  font-size: 20px;
}
.max-letter {
  font-size: 40px;
}
.min-letter {
  font-size: 15px;
}
</style>