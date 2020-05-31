from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class InputChannel(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM channel_input INNER JOIN analog_input ON analog_input.id = channel_input.analog_input_id")
		return {'channels': cursor.fetchall()}