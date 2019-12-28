import traceback

class PortSerial():

	def __init__(self, devise_path, serial_class):
		self.devise_path = devise_path
		self.PORT = None
		self.serial = serial_class

	def set_port(self):
		try:
			self.PORT = self.serial.Serial(self.devise_path, 9600, timeout=None)
			return False
		except:
# 			traceback.print_exc()
			self.PORT = None
			return True
		return False

	def close(self):
		self.PORT.close()
		



