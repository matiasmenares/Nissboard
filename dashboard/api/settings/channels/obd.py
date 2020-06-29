from flask_restful import Resource
from flask import request, jsonify
from model.models import db, Obd, ObdSchema , ObdInput, ObdInputSchema, ChannelInput

class OBDChannel(Resource):
 
    def get(self):
        obd = Obd.query.all()
        obd_schema = ObdSchema(many=True)
        return {'obd': obd_schema.dump(obd)}

    def post(self):
        try: 
            params  = request.json['obd']
            obd_input = ObdInput(name=params['name'], obd=Obd.query.get(params['obd_id']))
            channel_input = ChannelInput(obd_input=obd_input)
            db.session.add(obd_input)
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
