from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class InputChannel(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM channel_inputs INNER JOIN analog_channels ON analog_channels.id = channel_inputs.analog_channel_id")
		return {'channels': cursor.fetchall()}