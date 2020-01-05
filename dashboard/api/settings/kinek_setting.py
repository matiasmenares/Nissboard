from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class KinekSetting(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM dashboards WHERE name = 'KINEK'")
		return {'kinkek': cursor.fetchone()}

	def post(self):
		red_line        = request.json['red_line']
		yellow_line     = request.json['yellow_line']
		red_line_rpm    = request.json['red_line_rpm']
		yellow_line_rpm = request.json['yellow_line_rpm']

		cursor = self.database.con.cursor()
		cursor.execute("UPDATE dashboards SET red_line = ?, yellow_line = ?, red_line_rpm = ?, yellow_line_rpm = ? WHERE name = 'KINEK'", (red_line, yellow_line, red_line_rpm, yellow_line_rpm))
		self.database.con.commit()
		return {'response': True}