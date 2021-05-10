import time
import threading
from core.analog import Analog
from core.database import Database
from model.models import ChannelOutput, Alarm as AlarmModel, Led as LedModel
from core.alarm import Alarm
# from core.led import Led
from core.obd_ecu import ObdEcu 
from datetime import datetime, timedelta

class Output:
    def __init__(self, socketoi, serial, analog_path):
        self.socketio = socketoi
        self.analog = Analog(socketoi, analog_path, serial)
        self.analog_data = {'A0': None, 'A1': None, 'A2': None, 'A3': None, 'A4': None}
        self.output = ChannelOutput
        self.alarm = Alarm(socketoi)
        self.obd = ObdEcu(socketoi)
        self.alart_model = AlarmModel
#         self.led = Led()
        self.output_obs = None
        self.timer = None

    def start(self):
        self.output_obs = self.output.query.all()
        self.alarm.alarm_obj = self.alart_model.query.all()
#         self.led.leds = LedModel.query.all()
        self.timer = datetime.now()
        while True:
            self.set_analog()
            self.refresh_data()
            self.emit_response()
            time.sleep(0.03)

    def emit_response(self):
        response = []
        for output in self.output_obs:
            if output.channel_input.analog_input_id != None:
                self.set_analog_output(output, response)
            if output.channel_input.obd_input_id != None:
                self.set_obd_output(output, response)
            if output.channel_input.nissan_input_id != None:
                self.set_obd_output(output, response)
        self.externs(response)
        self.socketio.emit('channelOutput', response)

    def refresh_data(self):
        if(datetime.now() > (self.timer + timedelta(seconds=3))):
            self.timer = datetime.now()
            self.output_obs = self.output.query.all()
            self.alarm.alarm_obj = self.alart_model.query.all()
#             self.led.leds = LedModel.query.all()

    def externs(self, response):
            alarm = threading.Thread(target=self.alarm.send, args=(response,), daemon=True)
            alarm.start()
            # led = threading.Thread(target=self.led.start, args=(response,), daemon=True)
            # led.start()
#ANALOG
    def set_analog_output(self, output, response):
        return response.append({'id': output.id, 'name': output.name, 'measure': output.measure.name, 'value': self.set_analog_value(output), 'max_output': output.output_max_val, 'min_output': output.output_min_val})

    def set_analog_value(self, output):
        for pin in range(0, 7):
            if output.channel_input.analog_input.pin == f'A{pin}':
                return self.conver_analog_value(output, f'A{pin}')

    def conver_analog_value(self, output, pin):
        if self.analog_data[pin] != None:
            value = self.linear_function(self.analog_data[pin], self.linear_function(output.input_min_val, 0, 5000, 0, 1023) , self.linear_function(output.input_max_val, 0, 5000, 0, 1023), output.output_min_val, output.output_max_val)
            return round(eval("((("+ str(value) + output.measure.formula), 2)
        else:
            return 0.0

    def linear_function(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def set_analog(self):
        response = self.analog.get_data()
        if response['response']:
            self.analog_data = response['data']
        else:
            self.analog_data = {'A0': None, 'A1': None, 'A2': None, 'A3': None, 'A4': None, 'A5': None, 'A6': None, 'A7': None}
#OBD
    def set_obd_output(self, output, response):
        return response.append({'id': output.id, 'name': output.name, 'measure': output.measure.name, 'value': self.set_obd_value(output), 'max_output': output.output_max_val, 'min_output': output.output_min_val})

    def set_obd_value(self, output):
        response = self.obd.send(output.channel_input.obd_input.obd.command)
        return response
