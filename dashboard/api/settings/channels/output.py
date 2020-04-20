from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class OutputChannel(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM channel_outputs INNER JOIN analog_channels ON analog_channels.id = channel_outputs.analog_channel_id")
		return {'channels': cursor.fetchall()}