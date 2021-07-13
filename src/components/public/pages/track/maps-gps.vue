<template>
	<MglMap class="map-box-track" :accessToken="accessToken" :mapStyle.sync="mapStyle" :center="center" :zoom="0" :geojson="geojson">
		<MglMarker :coordinates="coord" color="green">
			<v-icon slot="marker">mdi-map-marker</v-icon>
		</MglMarker>
		<MglNavigationControl position="top-right" />
		<MglGeojsonLayer
		type="geojson"
		:sourceId="geojson.id"
		:layerId="layers.id"
		:source="geojson"
		:layer="layers"/>

	</MglMap>
</template>

<script>
import { MglMap, MglGeojsonLayer, MglNavigationControl, MglMarker } from "vue-mapbox";
export default {
	components: {
		MglMap,
		MglGeojsonLayer,
		MglNavigationControl,
		MglMarker,
	},
	data() {
		return {
            gps: null,
            center: [-39.24604166666666, -71.84461666666667],
			accessToken: "pk.eyJ1Ijoibmlzc2JvYXJkIiwiYSI6ImNrOGF0dWEyeTAxcmkzZXFjYzN4Yzl0NXoifQ.DVP6cTca7lufsyIiAw1N0g",
			mapStyle: 'mapbox://styles/mapbox/satellite-v9',
			coord: [-39.24604166666666, -71.84461666666667],
			geojson: {
				'type': 'FeatureCollection',
				'id': 'geoID'
			},
			layers: {
				type: 'circle',
				id: 'circle',
			}
		}
	},
    mounted () {
        this.set_data()
    },
    methods: {
        set_data(){
            this.sockets.subscribe('gps', (data) => {
                this.gps = data
                this.center = [this.gps.lon, this.gps.lat]
                this.coord = [this.gps.lon, this.gps.lat]
            })
        },
    }
};
</script>


<style type="text/css">
.map-box-track{
	height: 436px;
}
.mapboxgl-canvas {
	width: 100%;
	height: 436px;
	position: absolute;
	margin:0;
}
</style>