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
		if request.json['form_type'] == 1:
			return self.save_analog(request.json['channel'])
		elif request.json['form_type'] == 2:
			return self.save_obd(request.json['channel'])

	def save_analog(self, params):
		try: 
			out = ChannelOutput(name=params['name'], input_min_val=params['input_min_val'], input_max_val=params['input_max_val'], output_min_val=params['output_min_val'], output_max_val=params['output_max_val'], measure=Measure.query.get(params['measure_id']),channel_input=ChannelInput.query.get(params['channel_inputs_id']))
			db.session.add(out)
			db.session.commit()
			return {'response': True}
		except:
			return {'response': False}, 500

	def save_obd(self, params):
		try: 
			out = ChannelOutput(name=params['name'], output_min_val=params['output_min_val'], output_max_val=params['output_max_val'], measure=Measure.query.get(params['measure_id']),channel_input=ChannelInput.query.get(params['channel_inputs_id']))
			db.session.add(out)
			db.session.commit()
			return {'response': True}
		except:
			return {'response': False}, 500



