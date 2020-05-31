from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class Measure(Resource):

	def __init__(self):
		self.database = Database()
		
	def get(self):
		value = request.args
		cursor = self.database.con.cursor()
		if value:
			cursor.execute("SELECT * FROM measure WHERE measure_group_id = ?", value["group_id"] )
			return {'data': cursor.fetchall()}
		else:
			cursor.execute("SELECT * FROM measure")
			return {'data': cursor.fetchall()}
	def post(self):
		val = request.json['id']
		print(val)
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM measure WHERE id = ?", (val,))
		return {'data': cursor.fetchone()}	

