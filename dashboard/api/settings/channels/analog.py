from flask_restful import Resource
from flask import request, jsonify
from core.database import Database
from model.models import AnalogInput
from model.models import ChannelInput
from model.models import db

class AnalogChannel(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM analog_channel")
		return {'analogs': cursor.fetchall()}

	def post(self):
		try: 
			params  = request.json['analog']
			input_voltage = True if params["input"] == "Voltage" else False
			analog_input = AnalogInput(name=params['name'], pin=params['pin'], voltage_resistance=input_voltage)
			channel_input = ChannelInput(analog_input=analog_input)
			db.session.add(analog_input)
			db.session.add(channel_input)
			db.session.commit()
			return {'response': True}
		except: 
			return {'response': False}, 500

	def patch(self):
		try:
			analog  = request.json['analog']
			cursor = self.database.con.cursor()
			input = 1 if analog["input"] == "Voltage" else 0
			cursor.execute("UPDATE analog_channels SET name = ?, pin = ?, voltage_resistance = ? WHERE id = ? ", (analog["name"], analog["pin"], input, str(analog["id"])))
			self.database.con.commit()
			return {'response': True}
		except: 
			return {'response': False}
