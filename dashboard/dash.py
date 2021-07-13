#/bin/python
#Author: Matias Menares @matiasmenares
#Modules
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
from flask_restful import Api
from wifi import Cell, Scheme
from threading import Lock
import threading
import os 
import random
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
from api.var_config import VarConfig

from api.measure_group import MeasureGroup
from api.settings.kinek_setting import KinekSetting
from api.settings.screen_setting import ScreenSetting
from api.settings.water_setting import WaterSetting
from api.settings.alarm_type_setting import AlarmTypeSetting
from api.settings.channels.input import InputChannel
from api.settings.channels.obd import OBDChannel
from api.settings.channels.consult import ConsultChannel
from api.settings.channels.analog import AnalogChannel
from api.settings.channels.output import OutputChannel
from api.settings.condition_setting import ConditionSetting
from api.settings.alarm_setting import AlarmSetting
from api.settings.led_setting import LedSetting

from urllib.request import urlopen
import serial
import random
import socketio
import struct
import time
import argparse

#Async

async_mode = None
if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

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
socketio = SocketIO(app, cors_allowed_origins="*", async_mode=async_mode)

#API
api = Api(app)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api.add_resource(System, '/system')
api.add_resource(VarConfig, '/var_config')
api.add_resource(Dashboard, '/dashboards') 
api.add_resource(KinekSetting, '/settings/kinek')
api.add_resource(AlarmSetting, '/settings/alarms') 
api.add_resource(LedSetting, '/settings/leds') 
api.add_resource(ConditionSetting, '/settings/conditions')
api.add_resource(AlarmTypeSetting, '/settings/alarm_types')
api.add_resource(ScreenSetting, '/settings/screen') 
api.add_resource(WaterSetting, '/settings/water')
api.add_resource(AnalogChannel, '/settings/channels/input/analog')
api.add_resource(OBDChannel, '/settings/channels/input/obd')
api.add_resource(ConsultChannel, '/settings/channels/input/consult')
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
			internet = threading.Thread(target=internet_on, daemon=True)
			internet.start()
			internet = socketio.start_background_task(internet_on)
			output = threading.Thread(target=set_output, daemon=True)
			output.start()
			output = socketio.start_background_task(set_output)
			accelerometer = socketio.start_background_task(set_accelerometer)
			gps = socketio.start_background_task(set_gps)

def set_output():
	out.start()

def set_accelerometer():
	acc.start()

def set_gps():
	gps.start()

def internet_on():
	while True:
		list = ['http://apptec.cl', 'https://google.com', 'https://facebook.com', 'https://reddit.com', 'https://twitter.com']
		try:
			urlopen(random.choice(list), timeout=3)
			socketio.emit('InternetConnection', {'status': True})
			time.sleep(3)
		except: 
			socketio.emit('InternetConnection', {'status': False})
			time.sleep(2)
#Init 1
def main(params):
	socketio.run(app, host= '0.0.0.0', debug=True)

if __name__ == '__main__':
	acc = Accelerometer(socketio)
	gps = Gps(socketio, params.g, serial)
	out = Output(socketio, serial, params.a, params.d, params.e)

try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')