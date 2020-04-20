from flask_restful import Resource
from flask import request, jsonify
from core.database import Database

class Measure(Resource):

	def __init__(self):
		self.database = Database()
	
	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM measures")
		return {'data': cursor.fetchall()}

	def post(self):
		val = request.json['id']
		print(val)
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM measures WHERE id = ?", (val,))
		return {'data': cursor.fetchone()}	

