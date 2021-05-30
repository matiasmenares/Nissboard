import time
from datetime import datetime
from core.serial import PortSerial
from core.database import Database

class Ecu():

	def __init__(self, devise_pah, socketio, enviroment, serial_class):
		self.PORT = None
		self.running = False
		self.devise_pah = devise_pah
		self.serial_class = serial_class
		self.port_serial = PortSerial(devise_pah, serial_class)
		self.socketio = socketio
		self.enviroment = enviroment if enviroment != None else "production"
		self.MPH_Value = 0
		self.RPM_Value = 0
		self.TEMP_Value = 0
		self.BATT_Value = 0.0
		self.MAF_Value = 0
		self.AAC_Value = 0
		self.INJ_Value = 0
		self.TIM_Value = 0
		self.TURBO_Value = 0
		# self.command_live_sensors = [0x5A,0x08,0x5A,0x00,0x5A,0x01,0x5A,0x0b,0x5A,0x0c,0x5A,0x16,0x5A,0x0d,0x5A,0x17,0x5A,0x09,0x5A,0x1a,0x5A,0x14,0x5A,0x15,0xF0]
		self.command_live_sensors = [0x5A,0x08,0x5A,0x00,0x5A,0x01,0x5A,0x0d,0xF0]
		self.command_stop = 0x30

	def consume_data_test(self):
		return {'rpm': 1000, 'speed': 10, 'mph': 10, 'temp': 70, 'batt': 10, 'tps': 50, 'timming': 10, 'aac': 10, 'O2': 10, 'af': 40, 'injector': 50}

	def consume_data(self):
		read_thread = True
		byte_request = (len(self.command_live_sensors) - 1) / 2
		x = 0
		incomingData = self.PORT.read(20)
		dataList = self.handleData(incomingData, int(byte_request))
		if dataList != None:
			self.RPM_Value   = self.convertToRev(int(dataList[1]), int(dataList[2]))
			self.TEMP_Value  = self.convertToTemp(int(dataList[0]))
			self.TPS_Value   = self.convertToMPH(int(dataList[3]))
			print({'rpm': self.RPM_Value, 'temp': self.TEMP_Value, 'tps': self.TPS_Value})
			return {'rpm': self.RPM_Value, 'temp': self.TEMP_Value, 'tps': self.TPS_Value}

			# self.TEMP_Value  = self.convertToTemp(int(dataList[0]))
			# self.MPH_Value   = self.convertToMPH(int(dataList[3]))
			# self.KMH_Value   = self.convertToKMH(int(dataList[3]))
			# self.RPM_Value   = self.convertToRev(int(dataList[1]), int(dataList[2]))
			# self.BATT_Value  = self.convertToBattery(float(dataList[4]))
			# self.TIM_Value   = self.convertToTiming(int(dataList[5]))
			# self.TPS_Value   = self.convertToTps(int(dataList[6]))
			# self.AAC_Value   = self.convertToAAC(int(dataList[7]))
			# self.O2_Value    = self.convertToO2(dataList[8])
			# self.AF_Value    = dataList[9]
			# self.INJ_Value   = self.convertToInj(int(dataList[10]), int(dataList[11]))

			# print({'rpm': self.RPM_Value, 'speed': self.KMH_Value, 'mph': self.MPH_Value, 'temp': self.TEMP_Value, 'batt': self.BATT_Value, 'tps': self.TPS_Value, 'timming': self.TIM_Value, 'aac': self.AAC_Value, 'O2': self.O2_Value, 'af': self.AF_Value, 'injector': self.INJ_Value})
			# return {'rpm': self.RPM_Value, 'speed': self.KMH_Value, 'mph': self.MPH_Value, 'temp': self.TEMP_Value, 'batt': self.BATT_Value, 'tps': self.TPS_Value, 'timming': self.TIM_Value, 'aac': self.AAC_Value, 'O2': self.O2_Value, 'af': self.AF_Value, 'injector': self.INJ_Value}
		else:
			None

	def run(self, command=True):
		if command:
			self.running = True
			print("Run command nissan consult")
			self.socketio.emit('ecuConnection', {'status': True})
			self.PORT.write(self.command_live_sensors)

	def handleData(self, data, byteExpected):
		try:
			current_data = []
			frameStarted = False
			for i in range(len(data)):
				char = data[i:i+1].hex()
				if(char == "ff"):
					frameStarted = True
					lengthByte = None
					current_data = []
				elif frameStarted:
					if not lengthByte:
						lengthByte = int(char, 16)
					else:
						current_data.append(int(char, 16))
			if len(current_data) == byteExpected:
				frameStarted = False
				return current_data
			# else:
			# 	print("-------------")
			# 	print(len(current_data))
			# 	print(byteExpected)
			# 	print(data)
			# 	print("-------------")

		except NameError as e:
			print(f"An exception occurred: {e} ")
			return None

	def convertToMPH(self,inputData):
		return int(round ((inputData * 2.11) * 0.621371192237334))

	def convertToKMH(self,inputData):
		return int(round(inputData * 2.11))
	
	def convertToTps(self, inputData):
		return int(round(inputData) * 20)

	def convertToTpsPercent(self, inputData):
		return int(round(inputData) * 20)

	def convertToRev(self, mostSignificantBit, leastSignificantBit):
		return int(round(((mostSignificantBit << 8) + leastSignificantBit) * 12.5))
	
	def convertToTemp(self,inputData):
		return inputData - 50
	
	def convertToTurbo(self, inputData):
		if inputData < 150:
			return round(((float(inputData) / 150.0) - 1.0),1)
		else:
			return round(((float(inputData) - 150.0) / 150.0),1)
# 		return inputData
	
	def convertToBattery(self,inputData):
		return round(((inputData * 80) / 1000),1)
	
	def convertToMAF(self,inputData):
		return inputData * 5
	
	def convertToAAC(self,inputData):
		return inputData / 2
	
	def convertToTiming(self,inputData):
		return 110 - inputData
		
	def convertToO2(self,inputData):
		return inputData * 10

	def convertToInj(self, mostSignificantBit, leastSignificantBit):
		return round(((mostSignificantBit << 8) + leastSignificantBit) / 100.0)
	
	def logToFile(self, data, fileName):
		with open(fileName + '.hex', 'a+') as logFile:
			logFile.write(data)

	def printHex(self, data):
		print("".join(hex(ord(n)) for n in data))

	def development(self, x):
		test_file = open("test.hex")
		all_lines = test_file.readlines()
		return all_lines[4]

	def start_test(self):
		self.running = True

	def start(self, socketio, new_port_instance=False):
		if self.running:
			pass
		else:
			self.socketio = socketio
			self.PORT = None
			if self.enviroment == "production":
				self.initProduction(new_port_instance)
			else:
				self.start_development()

	def initProduction(self, new_port_instance):
		if new_port_instance:
			self.port_serial.close()
			self.port_serial = PortSerial(self.devise_pah, self.serial_class)
		while self.port_serial.set_port():
			print("[Consult] No Devise connected in "+self.devise_pah)
			self.socketio.emit('ecu_conection', {'status': False})
			time.sleep(2)
		self.PORT = self.port_serial.PORT
		self.start_production()		
	
	def start_production(self):
		READ_THREAD = False
		try:
			while READ_THREAD == False and self.running == False:
				#Send echo -e -n '\x10' > /dev/ttys006
				print("Try connection with Nissan Consult")
				self.PORT.flushInput()
				self.PORT.write([0xFF, 0xFF, 0xEF])
				time.sleep(2)
				response = self.PORT.read(1)
				if response.hex() == "10":
					READ_THREAD = True
					print("Consult datastream Accepted")
					self.run()
				else:
					print(f"[Failed] Consult datastream response {str(response.hex())}")
					if response.hex() != "00":
						self.stop_data_stream()
				
		except NameError as e:
			print(f"Failed to connect {str(e)}")
			time.sleep(2)
			self.socketio.emit('ecuConnection', {'status': False})

	def start_development(self):
		self.socketio = socketio
		READ_THREAD = False
		while READ_THREAD == False:
			print("Start Development")
			self.run() 

	def stop_data_stream(self):
		print("Send Stop Command")
		self.PORT.write(self.command_stop)
		acknowledgment = True
		while acknowledgment:
			response = self.PORT.read(1)
			if response.hex() == 'fe':
				print("Command Stopped")
				acknowledgment = False
				self.start_production()

