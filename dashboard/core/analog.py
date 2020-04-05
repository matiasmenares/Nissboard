import pynmea2
import time
import json
from termcolor import colored
from core.serial import PortSerial

class Analog():

	def __init__(self, socketio, arduino_path, serial_class):
		self.socketio = socketio
		self.port_serial = PortSerial(arduino_path, serial_class)
		self.PORT = None

	def start(self):
		while self.port_serial.set_port():
			print(colored("No Analog Devise connected in "+self.gps_path))
			self.socketio.emit('gpsConnection', {'status': False})
			time.sleep(2)
		self.PORT = self.port_serial.PORT
# 		try:
		while True:
			self.parse_analog()
# 		except:
# 			self.port_serial.close()
# 			self.start()

	def parse_analog(self):
		ard = self.PORT.readline().decode().replace("\r\n","")
		analog = eval(ard)
		self.socketio.emit('analogConnection', {'status': True})
		self.socketio.emit("analog", {'turbo': {'psi': { 'value': analog['psi'], 'peak': analog['peak'], 'raw': analog['raw'] }, 'bar': {'value': round((analog['psi'] * 0.0689475729317831), 2), 'peak': round((analog['peak'] * 0.0689475729317831), 2) } }})
		time.sleep(0.001)
