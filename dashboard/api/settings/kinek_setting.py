from flask_restful import Resource
from flask import request, jsonify
from core.database import Database
from model.models import Dashboard, DashboardSchema, db, ChannelOutput, ChannelOutputSchema, DashboardOutput, DashboardOutputSchema, DashboardHasOutput, DashboardHasOutputSchema

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
		dashboard_has_outputs = DashboardHasOutput.query.all()
		dashboard_has_output_schema = DashboardHasOutputSchema(many=True)
		return {'dashboards': dashboard_schema.dump(dashboards), 'outputs': channel_schema.dump(channels), 'dashboard_outputs': dashboard_output_schema.dump(dashboard_outputs), 'dashboard_has_outputs': dashboard_has_output_schema.dump(dashboard_has_outputs) }

	def post(self):
		kinek = request.json['kinek']
		for idx, dash_output in enumerate(kinek['dashboard_outputs']):
			if DashboardHasOutput.query.join(DashboardOutput,ChannelOutput).filter(DashboardOutput.id == dash_output['id'], ChannelOutput.id == kinek['outputs'][idx]).first() == None:
				out = DashboardHasOutput(dashboard_output=DashboardOutput.query.get(dash_output['id']), channel_output=ChannelOutput.query.get(kinek['outputs'][idx]))
				db.session.add(out)
				db.session.commit()
		return {'response': True}