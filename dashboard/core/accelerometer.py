import time
import math
from datetime import datetime, timedelta
from model.models import VarConfig as VarConfigModel, VarConfigSchema, db
import random

try:
	import FaBo9Axis_MPU9250
	rasp = True
except:
	rasp = False

class Accelerometer():

	def __init__(self, socketio):
		self.runit = False
		self.socketio = socketio
		self.xoff = None
		self.zoff = None
		self.yoff = None
		self.timer = datetime.now()

		if rasp:
			try:
				self.mpu9250 = FaBo9Axis_MPU9250.MPU9250()
				self.accelerometer = self.mpu9250.readAccel()
				self.gyro = self.mpu9250.readGyro()
				self.mag = self.mpu9250.readMagnet()
				self.runit = True
			except:
				self.runit = False
				print("[Accelerometer] No Accelerometer is finded")
		else:
			print("[Accelerometer] No Accelerometer")

	def start(self):
		if self.runit:
			self.start_production()
		else:
			self.start_development()

	def update(self):
		self.accelerometer = self.mpu9250.readAccel()
		# self.gyro = self.mpu9250.readGyro()
		# self.mag = self.mpu9250.readMagnet()

	def start_development(self):
		list = [0.0, 0.1, -0.1, 0.05, -0.05, 0.01, -0.01, -0.2, 0.2]
		x = 0.0
		z = 0.0
		while True:
			x += random.choice(list) 
			z += random.choice(list)
			if abs(round(x)) >= 2.0 or abs(round(z)) >= 2.0:
				x = 0.0
				z = 0.0
			self.need_reset()
			self.socketio.emit('accelerometer', {"lateral": {"ms": round(x, 1), "g": round(x, 1)}, "acceleration": {"ms": round(z, 1), "g": round(z, 1)} })
			time.sleep(0.05)

	def start_production(self):
		self.reset_offset()
		while True:
			self.update()
			x = self.accelerometer['x']
			y = self.accelerometer['y']
			z = self.accelerometer['z']

			latG = round((x - self.xoff), 1)
			accG = round((self.zoff - z), 1)
			self.socketio.emit('accelerometer', {"lateral": {"ms": (self.xoff - x), "g": latG}, "acceleration": {"ms": (self.zoff - z), "g": accG} })
			self.need_reset()
			time.sleep(0.05)

	def reset_offset(self):
		while True:
			self.update()
			self.xoff = self.accelerometer['x']
			self.yoff = self.accelerometer['y']
			self.zoff = self.accelerometer['z']
			if self.xoff < 1.5 and self.yoff < 1.0:
				time.sleep(0.5)
				break

	def need_reset(self):
		if(datetime.now() > (self.timer + timedelta(seconds=3))):
			self.timer = datetime.now()
			v_config = VarConfigModel.query.get(1)
			if v_config.var_value == "1":
				if self.runit:
					self.reset_offset()
				v_config.var_value = False
				db.session.commit()			

	def compass(self):
		while True:
			self.update()
			mag = self.mag
			declinacion =  -4.14
			angulo = math.atan2(mag['z'], mag['x'])
			angulo = angulo * (180 / math.pi)
			angulo = angulo - declinacion
			if angulo != 4.14:
				if angulo < 0.0:
					angulo = angulo + 360
				return round(angulo)
