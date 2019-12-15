from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
from core.ecu import Ecu
import serial
import random
import os
import math
from threading import Lock
import datetime
import socketio
import struct
import argparse
#Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-e", help="Enviroments")
parser.add_argument("-d", help="ECU USB Devise")
args = parser.parse_args()
params = parser.parse_args()
#Serial
PORT = serial.Serial(params.d, 9600, timeout=None)
# PORT = serial.Serial('/dev/tty.usbserial-A103NKGZ', 9600, timeout=None)
#WebServer
app = Flask(__name__)
app.config['SECRET_KEY'] = random.getrandbits(128)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app, cors_allowed_origins="*",async_mode='threading')
#Threads
thread = None
thread_lock = Lock()

@socketio.on('connect')
def test_connect():
	print("Websocket Conectado")
	global thread
	with thread_lock:
		if thread is None:
			thread = socketio.start_background_task(set_ecu)
def set_ecu():
	ecu.start(socketio)

#Init 1
def main(params):
	socketio.run(app)
		
if __name__ == '__main__':
	ecu = Ecu(PORT, socketio, params.e)

try:
    main(params)
except (KeyboardInterrupt, EOFError):
    log.info('Exiting.')