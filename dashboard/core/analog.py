import pynmea2
import time
import json
import os, fnmatch
from termcolor import colored
from core.serial import PortSerial

class Analog():

	def __init__(self, socketio, analog_path, serial_class):
		self.socketio = socketio
		self.serial_class = serial_class
		self.port_serial = PortSerial(analog_path, serial_class)
		self.PORT = None
		self.analog_path = analog_path
		self.connected = False

	def get_data(self):
		if self.connected == False:
			if self.port_serial.set_port():
				self.search_port("cu.usbmodem14*" , "/dev")
				print(colored("No Analog Devise connected in "+self.analog_path))
				self.socketio.emit('analogConnection', {'status': False})
				self.connected = False
				return {'response': False, 'msg': "No devise connected in Analog"}
			else:
				self.PORT = self.port_serial.PORT
				return self.set_data()
		else:
			return self.set_data()

	def set_data(self):
		try:
			return self.return_data()
		except Exception as ex:
			self.connected = False
			self.port_serial.close()
			return {'response': False, 'msg': ex}

	def search_port(self, patt, path):
		result = []
		for root, dirs, files in os.walk(path):
			for name in files:
				if fnmatch.fnmatch(name, patt):
					result.append(os.path.join(root, name))
		if result:
			self.port_serial = PortSerial(result[0], self.serial_class)

	def parse_analog(self):
		ard = self.PORT.readline().decode().replace("\r\n","")
		analog = eval(ard)
		self.connected = True
		self.socketio.emit('analogConnection', {'status': True})
		self.socketio.emit("analog", {'turbo': {'psi': { 'value': analog['psi'], 'peak': analog['peak'], 'raw': analog['raw'], 'voltage': analog['voltage'], 'boostmar': analog['boostmar'] }, 'bar': {'value': round((analog['psi'] * 0.0689475729317831), 2), 'peak': round((analog['peak'] * 0.0689475729317831), 2), 'voltage': analog['voltage'] } }})

	def return_data(self):
		ard = self.PORT.readline().decode().replace("\r\n","")
		analog = eval(ard)
		self.connected = True
		self.socketio.emit('analogConnection', {'status': True})
		self.socketio.emit("analog", { 'cero': analog['A0'], 'one': analog['A1'], 'two': analog['A2'], 'tree': analog['A3'], 'four': analog['A4'], 'five': analog['A5'], 'six': analog['A6']})
		return {'response': True, 'data': { 'A0': analog['A0'], 'A1': analog['A1'], 'A2': analog['A2'], 'A3': analog['A3'], 'A4': analog['A4'], 'A5': analog['A5'], 'A6': analog['A6'], 'A7': analog['A7']}}
