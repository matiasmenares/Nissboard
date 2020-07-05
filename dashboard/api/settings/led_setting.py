from flask_restful import Resource
from flask import request, jsonify
from model.models import db, Color, ColorSchema, Led, LedSchema, LedOutput, LedSchema

class LedSetting(Resource):

    def get(self):
        led = Led.query.all()
        led_schema = LedSchema(many=True)
        color = Led.query.all()
        color_schema = LedSchema(many=True)
        return {'leds': led_schema.dump(led), 'colors': color_schema.dump(color) }

    def post(self):
        params = request.json['led']
        led = Led(name=params['name'], brightness=params['brightness'], channel_output_id=params['channel_output_id'],priority=params['priority'])
        db.session.add(led)
        db.session.commit()
        for led_output in request.json['led_outputs']:
            print(led_output)
            output = LedOutput(led=led, led_start=led_output['led_start'], led_end=led_output['led_end'], value_start=led_output["value_start"], value_end=led_output["value_end"], color_start=Color.query.get(led_output['color_start_id']), color_end=Color.query.get(led_output['color_end_id']))
            db.session.add(output)
            db.session.commit()
        return True