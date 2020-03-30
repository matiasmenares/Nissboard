import time
from datetime import datetime
from core.serial import PortSerial
from core.database import Database
import board
import busio
import adafruit_adxl34x

class Accelerometer():

	def __init__(self, socketio):
		self.start = False
		try:
			self.socketio = socketio
			i2c = busio.I2C(board.SCL, board.SDA)
			ad = adafruit_adxl34x
			self.accelerometer = ad.ADXL345(i2c)
			self.accelerometer.data_rate = ad.DataRate.RATE_12_5_HZ
			self.accelerometer.range = ad.Range.RANGE_4_G
			self.start = True
		except:
			self.start = False
			print("No Accelerometer is finded")
	def start():
		if self.start:
			while True:
				xoff, YOFF, zoff = self.accelerometer.acceleration
				if zoff < 1.5 and YOFF < 1.0:
					time.sleep(1)
					break
			while True:
				x,y,z = self.accelerometer.acceleration
				latG = round(((YOFF - y) * (1 / 9.80655)), 1)
				accG = round(((zoff - z) * (1 / 9.80655)), 1)
				self.socketio.emit('accelerometer', {"lateral": {"ms": (YOFF - y), "g": latG}, "acceleration": {"ms": (zoff - z), "g": accG} })
				#self.socketio.emit('accelerometer', {"lateral": {"ms": (-0.078453), "g": 1.0}, "acceleration": {"ms": (0.627626), "g": 1.0} })
				time.sleep(0.05)