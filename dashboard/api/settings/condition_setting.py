from flask_restful import Resource
from flask import request, jsonify
from model.models import Condition, ConditionSchema

class ConditionSetting(Resource):

	def get(self):
		conditions = Condition.query.all()
		condition_schema = ConditionSchema(many=True)
		return {'conditions': condition_schema.dump(conditions)}


