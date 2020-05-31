from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class MeasureGroup(Resource):

	def __init__(self):
		self.database = Database()
	
	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM measure_group")
		return {'data': cursor.fetchall()}

	def post(self):
		val = request.json['measure_groups_id']
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM measure_group WHERE name = ?", (val,))
		return {'data': cursor.fetchone()}	

