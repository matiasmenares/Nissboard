from flask_restful import Resource
from flask import request, jsonify
from core.database import Database
from model.models import db, AnalogInput, AnalogInputSchema,ChannelInput, ChannelInputSchema, AnalogInput, AnalogInputSchema, ObdInput, ObdInputSchema, Obd, ObdSchema

class InputChannel(Resource):

	def get(self):
		channel_input = ChannelInput.query.all()
		channel_input_schema = ChannelInputSchema(many=True)
		obd_input = ObdInput.query.all()
		obd_input_schema = ObdInputSchema(many=True)
		obd = Obd.query.all()
		obd_schema = ObdSchema(many=True)
		analog_input = AnalogInput.query.all()
		analog_input_schema = AnalogInputSchema(many=True)
		return {'channels': channel_input_schema.dump(channel_input), 'obd_inputs': obd_input_schema.dump(obd_input), 'obds': obd_schema.dump(obd), 'analog_inputs': analog_input_schema.dump(analog_input)}