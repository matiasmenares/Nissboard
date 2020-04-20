from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class AnalogChannel(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM analog_channels")
		return {'analogs': cursor.fetchall()}

	def post(self):
		try: 
			analog  = request.json['analog']
			input = 1 if analog["input"] == "Voltage" else 0
			cursor = self.database.con.cursor()
			cursor.execute("INSERT INTO analog_channels VALUES(NULL ,?, ?, ?)", (analog["name"], analog["pin"], input))
			cursor.execute("INSERT INTO channel_inputs VALUES(NULL, ?)", (str(cursor.lastrowid),))
			self.database.con.commit()
			return {'response': True}
		except: 
			return {'response': False}

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
