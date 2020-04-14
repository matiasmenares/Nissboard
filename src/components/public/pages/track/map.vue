<template>
	<b-row>
		<b-col cols="12">
			<MglMap class="map-box-track" :accessToken="accessToken" :mapStyle.sync="mapStyle" :center="center" :zoom="15" :geojson="geojson">
				<MglMarker :coordinates="coord" color="green">
					<v-icon slot="marker">mdi-map-marker</v-icon>
				</MglMarker>
				<MglNavigationControl position="top-right" />
				<MglGeojsonLayer
				type="geojson"
				:sourceId="geojson.id"
				:layerId="layers.id"
				:source="geojson"
				:layer="layers"
				/>

			</MglMap>
		</b-col>
	</b-row>
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
		props:{
			center: {default: null}
		},
		data() {
			return {
				accessToken: "pk.eyJ1Ijoibmlzc2JvYXJkIiwiYSI6ImNrOGF0dWEyeTAxcmkzZXFjYzN4Yzl0NXoifQ.DVP6cTca7lufsyIiAw1N0g",
				mapStyle: 'mapbox://styles/mapbox/satellite-v9',
				coord: [-70.632402, -34.036850],
				geojson: {
					'type': 'FeatureCollection',
					'id': 'geoID'
				},
				layers: {
					type: 'line',
					id: 'line',
					source: {
						type: 'geojson',
						lineMetrics: true,
						data: {
							type: 'Feature',
							properties: {},
							geometry: {
								type: 'LineString',
								coordinates: [
									[-70.632402, -34.036850],
									[-70.630672, -34.037105],
									[-70.628530, -34.037495],
									[-70.628122, -34.037700],
									[-70.628052, -34.038000],
									[-70.627998, -34.038125],
									[-70.627660, -34.038219],
									[-70.627188, -34.038263],
									[-70.626952, -34.038285],
									[-70.626421, -34.038116],
									[-70.625170, -34.037725],
									[-70.624962, -34.037434],
									[-70.625005, -34.037063],
									[-70.625153, -34.036956],
									[-70.625475, -34.036829],
									[-70.625813, -34.036760],
									[-70.626300, -34.036687],
									[-70.626673, -34.036683],
									[-70.627419, -34.036930],
									[-70.627907, -34.036974],
									[-70.628159, -34.036910],
									[-70.628457, -34.036754]
								]
							}
						}
					},
					paint: {
						'line-color': 'red',
						'line-width': 5,
						// 'line-gradient' must be specified using an expression
						// with the special 'line-progress' property		
						'line-gradient': [
							'interpolate',
							['linear'],
							['line-progress'],
							0,
							'lime',
							0.1,
							'lime',
							0.3,
							'lime',
							0.35,
							'yellow',
							0.4,
							'red',
							0.5,
							'lime',
							0.65,
							'lime',
							0.7,
							'lime',
							0.9,
							'yellow',
							1,
							'red'
						]		
					},
					layout: {
						'line-cap': 'round',
						'line-join': 'round'
					}
				}
			}
		},
	};
</script>
<style>

</style>