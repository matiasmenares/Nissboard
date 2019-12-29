from flask_restful import Resource
from core.database import Database
import os

class System(Resource):

	def __init__(self):
		self.database = Database()
	
	def get(self):
		cursor = self.database.con.cursor()
		cursor.execute("SELECT * FROM records")
		return {'records': [i[0] for i in cursor.fetchall()]}

	def delete(self):
		#shutdown system
		os.system('sudo shutdown now')
		return {"status": True}

