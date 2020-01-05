#/bin/python
#Author: Matias Menares @matiasmenares

#Modules
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
from flask_restful import Api
from wifi import Cell, Scheme
from threading import Lock
#Core
from core.ecu import Ecu
from core.database import Database
#API
from api.system import System
from api.settings.kinek_setting import KinekSetting
from api.settings.water_setting import WaterSetting

import urllib2
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
args = parser.parse_args()
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
api.add_resource(KinekSetting, '/settings/kinek') 
api.add_resource(WaterSetting, '/settings/water')

#database
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
			thread = socketio.start_background_task(set_ecu)
			thread_2 = socketio.start_background_task(internet_on)

def set_ecu():
	ecu.start(socketio)
	
def internet_on():
	while True:
		try:
			urllib2.urlopen('http://216.58.192.142', timeout=1)
			socketio.emit('InternetConnection', {'status': True})
			time.sleep(3)
		except: 
			socketio.emit('InternetConnection', {'status': False})
			time.sleep(3)
#Init 1
def main(params):
	socketio.run(app)
		
if __name__ == '__main__':
	ecu = Ecu(params.d, socketio, params.e, serial)

try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')