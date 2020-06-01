#/bin/python
#Author: Matias Menares @matiasmenares
#Modules
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
from flask_restful import Api
from wifi import Cell, Scheme
from threading import Lock
import os 
#Core
from core.ecu import Ecu
from core.database import Database
from core.accelerometer import Accelerometer
from core.gps import Gps
from core.analog import Analog
from core.output import Output
#API
from api.dashboard import Dashboard
from api.system import System
from api.measure import Measure
from api.measure_group import MeasureGroup
from api.settings.kinek_setting import KinekSetting
from api.settings.screen_setting import ScreenSetting

from api.settings.water_setting import WaterSetting
from api.settings.channels.input import InputChannel
from api.settings.channels.analog import AnalogChannel
from api.settings.channels.output import OutputChannel

from urllib.request import urlopen
import serial
import random
import socketio
import struct
import time
import argparse
#Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-e", help="Enviroments")
parser.add_argument("-d", help="ECU USB Devise")
parser.add_argument("-g", help="GPS USB Devise")
parser.add_argument("-a", help="Analog USB Devise")
params = parser.parse_args()
#WebServer
app = Flask(__name__)
app.config['SECRET_KEY'] = random.getrandbits(128)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app, cors_allowed_origins="*",async_mode='threading')

#API
api = Api(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api.add_resource(System, '/system')
api.add_resource(Dashboard, '/dashboards') 
api.add_resource(KinekSetting, '/settings/kinek') 
api.add_resource(ScreenSetting, '/settings/screen') 
api.add_resource(WaterSetting, '/settings/water')
api.add_resource(AnalogChannel, '/settings/channels/input/analog')
api.add_resource(InputChannel, '/settings/channels/input')
api.add_resource(OutputChannel, '/settings/channels/output')
api.add_resource(Measure, '/measures')
api.add_resource(MeasureGroup, '/measure_groups')
#Database
d = Database()
d.init()
#Threads
thread = None
thread_lock = Lock()

@socketio.on('connect')
def test_connect():
	print("Websocket Connected")
	global thread
	with thread_lock:
		if thread is None:
			output = socketio.start_background_task(set_output)
			# ecu = socketio.start_background_task(set_ecu)
			# internet = socketio.start_background_task(internet_on)
# 			accelerometer = socketio.start_background_task(set_accelerometer)
			gps = socketio.start_background_task(set_gps)

def set_output():
	out.start()

def set_ecu():
	ecu.start(socketio)

def set_accelerometer():
	acc.start()

def set_gps():
	gps.start()

def internet_on():
	while True:
		try:
			urlopen('http://apptec.cl', timeout=1)
			socketio.emit('InternetConnection', {'status': True})
			time.sleep(2)
		except: 
			socketio.emit('InternetConnection', {'status': False})
			time.sleep(1)
#Init 1
def main(params):
	socketio.run(app, host= '0.0.0.0')

if __name__ == '__main__':
	ecu = Ecu(params.d, socketio, params.e, serial)
	acc = Accelerometer(socketio)
	gps = Gps(socketio, params.g, serial)
	out = Output(socketio, serial, params.a)
try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')