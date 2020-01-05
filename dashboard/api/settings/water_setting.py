from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class WaterSetting(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM sensors WHERE name = 'Water'")
		return {'Water': cursor.fetchone()}

	def post(self):
		alert  = request.json['alert']
		alert_value  = request.json['alert_value']

		cursor = self.database.con.cursor()
		cursor.execute("UPDATE sensors SET alert = ?, alert_value = ? WHERE name = 'Water'", (alert, alert_value))
		self.database.con.commit()
		return {'response': True}