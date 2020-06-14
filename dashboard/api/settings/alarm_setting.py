from flask_restful import Resource
from flask import request, jsonify
from model.models import db, Alarm, AlarmSchema, AlarmType, AlarmTypeSchema, AlarmOutput, ChannelOutput, Condition

class AlarmSetting(Resource):

    def get(self):
        alarm = Alarm.query.all()
        alarm_schema = AlarmSchema(many=True)
        alarm_types = AlarmType.query.all()
        alarm_types_schema = AlarmTypeSchema(many=True)
        return {'alarm_types': alarm_types_schema.dump(alarm_types), 'alarms': alarm_schema.dump(alarm) }
    def post(self):
        params = request.json['alarm']
        alarm = Alarm(name=params['name'], description=params['description'], life_second=params['life_second'],alarm_type=AlarmType.query.get(params['alarm_type_id']))
        db.session.add(alarm)
        db.session.commit()
        for condition in request.json['conditions']:
            print(condition)
            output = AlarmOutput(channel_output=ChannelOutput.query.get(condition['channel_output_id']), condition=Condition.query.get(condition['condition_id']), value=condition['value'], alarm=alarm)
            db.session.add(output)
            db.session.commit()
        return True