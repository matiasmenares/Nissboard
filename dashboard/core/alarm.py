import time
from termcolor import colored
from model.models import db, Alarm as AlarmModel, AlarmSchema, AlarmOutput
from datetime import datetime, timedelta
import threading

class Alarm(threading.Thread):

    def __init__(self, socketio):
        threading.Thread.__init__(self)
        self.socketio = socketio
        self.second = None
        self.timer = None
        self.current_alarm_type_id = None

    def send(self, responses):
        for alarm in AlarmModel.query.all():
            alart_outputs = AlarmOutput.query.filter_by(alarm_id=alarm.id)
            if self.validate_outputs(alart_outputs, responses):
                self.set_hierarchy(alarm, alart_outputs, responses)
    
    def set_hierarchy(self, alarm, alart_outputs, responses):
        if self.current_alarm_type_id == None:
            self.emit(alarm, alart_outputs, responses)
        else:
            if alarm.alarm_type_id > self.current_alarm_type_id:
                self.emit(alarm, alart_outputs, responses)
            else:
                if(datetime.now() > (self.timer + timedelta(seconds=self.second))):
                    self.emit(alarm, alart_outputs, responses)
        
    def emit(self, alarm, alart_outputs, responses):
        self.socketio.emit("alert", {'id': alarm.id, 'name': alarm.name, 'description': self.set_alarm_description(alarm.description, alart_outputs, responses), 'alarm_type_id': alarm.alarm_type_id})
        self.second = alarm.life_second
        self.timer = datetime.now()
        self.current_alarm_type_id = alarm.alarm_type_id

    def validate_outputs(self, conditions, responses):
        for condition in conditions:
            output = self.find_output(condition, responses)
            if self.validate_condition(condition, output) == False:
                return False
        return True

    def find_output(self, condition, responses):
        for response in  responses:
            if response['id'] == condition.channel_output_id:
                return response

    def validate_condition(self, condition, output):
        if condition.condition_id == 1:
            return self.greater_than(condition, output)
        elif condition.condition_id == 2:
            return self.greater_than_or_equal_to(condition, output)
        elif condition.condition_id == 3:
            return self.equal_to(condition, output)
        elif condition.condition_id == 4:
            return self.less_than_or_equal_to(condition, output)
        elif condition.condition_id == 5:
            return self.greater_than_or_equal_to(condition, output)
        else:
            return False
    def set_alarm_description(self, description, outputs, responses):
        datas = description.split("#")
        if len(datas) == 1: return description
        datas.pop(0)
        for word in datas:
            value = self.search_output_description(word[0], responses)
            description = description.replace("#"+word[0], str(value))
        return description

    def search_output_description(self, id, responses):
        for response in responses:
            if response['id'] == int(id): return response['value']

    def greater_than(self, condition, output):
        if output['value'] > int(condition.value):
            return True
        else:
            return False

    def greater_than_or_equal_to(self, condition, output):
        if output['value'] >= int(condition.value):
            return True
        else:
            return False

    def equal_to(self, condition, output):
        if output['value'] == int(condition.value):
            return True
        else:
            return False

    def less_than_or_equal_to(self, condition, output):
        if output['value'] <= int(condition.value):
            return True
        else:
            return False

    def less_than(self, condition, output):
        if output['value'] < int(condition.value):
            return True
        else:
            return False