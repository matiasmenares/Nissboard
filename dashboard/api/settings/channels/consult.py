from flask_restful import Resource
from flask import request, jsonify
from model.models import db, Consult, ConsultSchema , NissanInput, NissanInputSchema, ChannelInput

class ConsultChannel(Resource):
 
    def get(self):
        consult = Consult.query.all()
        consult_schema = ConsultSchema(many=True)
        return {'consults': consult_schema.dump(consult)}

    def post(self):
        try: 
            params  = request.json['consult']
            consult_input = NissanInput(name=params['name'], consult=Consult.query.get(params['consult_id']))
            channel_input = ChannelInput(nissan_input=consult_input)
            db.session.add(consult_input)
            db.session.add(channel_input)
            db.session.commit()
            return {'response': True}
        except: 
        	return {'response': False}, 500

    def patch(self):
        try:
            analog  = request.json['analog']
            cursor = self.database.con.cursor()
            input = 1 if analog["input"] == "Voltage" else 0
            cursor.execute("UPDATE analog_channels SET name = ?, pin = ?, voltage_resistance = ? WHERE id = ? ", (analog["name"], analog["pin"], input, str(analog["id"])))
            self.database.con.commit()
            return {'response': True}
        except: 
            return {'response': False}
