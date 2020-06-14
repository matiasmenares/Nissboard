import time
from core.analog import Analog
from core.database import Database
from model.models import ChannelOutput
from core.alarm import Alarm
import threading

class Output:
    def __init__(self, socketoi, serial, analog_path):
        self.socketio = socketoi
        self.analog = Analog(socketoi, analog_path, serial)
        self.analog_data = {'A0': None, 'A1': None, 'A2': None, 'A3': None, 'A4': None}
        self.output = ChannelOutput
        self.alarm = Alarm(socketoi)

    def start(self):
        while True:
            self.set_analog()
            response = []
            for output in self.output.query.all():
                if output.channel_input.analog_input_id != None:
                    self.set_analog_output(output, response)
            self.socketio.emit('channelOutput', response)
            t = threading.Thread(target=self.alarm.send, args=(response,), daemon=True)
            t.start()
            time.sleep(0.01)
    def set_analog_output(self, output, response):
        return response.append({'id': output.id, 'name': output.name, 'measure': output.measure.name, 'value': self.set_analog_value(output)})

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
            self.analog_data = {'A0': None, 'A1': None, 'A2': None, 'A3': None, 'A4': None}  