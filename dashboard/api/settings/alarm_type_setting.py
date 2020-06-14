from flask_restful import Resource
from flask import request, jsonify
from model.models import AlarmType, AlarmTypeSchema

class AlarmTypeSetting(Resource):

	def get(self):
		alarm_types = AlarmType.query.all()
		alarm_types_schema = AlarmTypeSchema(many=True)
		return {'alarm_types': alarm_types_schema.dump(alarm_types)}


