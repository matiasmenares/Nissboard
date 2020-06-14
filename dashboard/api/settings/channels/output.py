from flask_restful import Resource
from flask import request, jsonify
from model.models import ChannelOutput, ChannelInput, ChannelOutputSchema, Measure, MeasureSchema, db

class OutputChannel(Resource):

	def get(self):
		channels = ChannelOutput.query.all()
		channel_schema = ChannelOutputSchema(many=True)
		measures = Measure.query.all()
		measure_schema = MeasureSchema(many=True)
		return {'channels': channel_schema.dump(channels), 'measures': measure_schema.dump(measures)}

	def post(self):
		try: 
			params = request.json['channel']
			out = ChannelOutput(name=params['name'], input_min_val=params['input_min_val'], input_max_val=params['input_max_val'], output_min_val=params['output_min_val'], output_max_val=params['output_max_val'], measure=Measure.query.get(params['measure_id']),channel_input=ChannelInput.query.get(params['channel_inputs_id']))
			db.session.add(out)
			db.session.commit()
			return {'response': True}
		except:
			return {'response': False}, 500


