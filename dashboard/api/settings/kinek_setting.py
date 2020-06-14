from flask_restful import Resource
from flask import request, jsonify
from core.database import Database
from model.models import Dashboard, DashboardSchema, db, ChannelOutput, ChannelOutputSchema, DashboardOutput, DashboardOutputSchema 

class KinekSetting(Resource):

	def __init__(self):
		self.database = Database()

	def get(self):
		dashboards = Dashboard.query.all()
		dashboard_schema = DashboardSchema(many=True)
		channels = ChannelOutput.query.all()
		channel_schema = ChannelOutputSchema(many=True)
		dashboard_outputs = DashboardOutput.query.all()
		dashboard_output_schema = DashboardOutputSchema(many=True)
		return {'dashboards': dashboard_schema.dump(dashboards), 'outputs': channel_schema.dump(channels), 'dashboard_outputs': dashboard_output_schema.dump(dashboard_outputs) }

	def post(self):
		kinek = request.json['kinek']
		for dash_output in kinek['dashboard_outputs']:
			out = DashboardOutput.query.get(dash_output['id'])
			out.channel_output_id = dash_output['channel_output_id']
			db.session.add(out)
			db.session.commit()
		return {'response': True}