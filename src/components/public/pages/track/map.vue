<template>
	<b-row>
		<b-col cols="12">
			<MglMap class="map-box-track" :accessToken="accessToken" :mapStyle="mapStyle" :center="coordinates" :zoom="12" :geojson="geojson">
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
	import { MglMap, MglGeojsonLayer, MglNavigationControl } from "vue-mapbox";
	export default {
		components: {
			MglMap,
			MglGeojsonLayer,
			MglNavigationControl
		},
		data() {
			return {
				accessToken: "pk.eyJ1Ijoibmlzc2JvYXJkIiwiYSI6ImNrOGF0dWEyeTAxcmkzZXFjYzN4Yzl0NXoifQ.DVP6cTca7lufsyIiAw1N0g",
				mapStyle: 'mapbox://styles/mapbox/light-v10',
				// coordinates: [-70.6338175, -34.0369462],
				coordinates:  [-77.035, 38.875],
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
									[-77.044211, 38.852924],
									[-77.045659, 38.860158],
									[-77.044232, 38.862326],
									[-77.040879, 38.865454],
									[-77.039936, 38.867698],
									[-77.040338, 38.86943],
									[-77.04264, 38.872528],
									[-77.03696, 38.878424],
									[-77.032309, 38.87937],
									[-77.030056, 38.880945],
									[-77.027645, 38.881779],
									[-77.026946, 38.882645],
									[-77.026942, 38.885502],
									[-77.028054, 38.887449],
									[-77.02806, 38.892088],
									[-77.03364, 38.892108],
									[-77.033643, 38.899926]
								]
							}
						}
					},
					paint: {
						'line-color': 'red',
						'line-width': 14,
						// 'line-gradient' must be specified using an expression
						// with the special 'line-progress' property		
						'line-gradient': [
							'interpolate',
							['linear'],
							['line-progress'],
							0,
							'blue',
							0.1,
							'royalblue',
							0.3,
							'cyan',
							0.5,
							'lime',
							0.7,
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
	.map-box-track{ position: absolute;
		top: 0;
		bottom: 0;
		width: 100%;
	}
</style>