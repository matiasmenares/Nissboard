import traceback

class PortSerial():

	def __init__(self, devise_path, serial_class, baudrate=9600):
		self.devise_path = devise_path
		self.PORT 		 = None
		self.serial		 = serial_class
		self.baudrate	 = baudrate

	def set_port(self):
		try:
			self.PORT = self.serial.Serial(self.devise_path, self.baudrate, timeout=0.25)
			return False
		except:
			self.PORT = None
			return True
		return False

	def close(self):
		self.PORT.close()
		



