import time

class Ecu():

	def __init__(self, port, socketio, enviroment):
		self.PORT = port
		self.socketio = socketio
		self.enviroment = enviroment if enviroment != None else "production"
		self.MPH_Value = 0
		self.RPM_Value = 0
		self.TEMP_Value = 0
		self.BATT_Value = 0
		self.MAF_Value = 0
		self.AAC_Value = 0
		self.INJ_Value = 0
		self.TIM_Value = 0
		self.TURBO_Value = 0
		self.Header = 255
		self.returnBytes = 16

	def consume_data(self, command):
		#echo -e -n '\x04\x78\x00\x4f\x00\xff\x04\x78\x00\x4f\00' > /dev/ttys006
		read_thread = True
		byte_request = (len(command) - 1) / 2
		x = 0
		while read_thread:
			incomingData = self.PORT.read(17) if self.enviroment == "production" else self.development(x)
			dataList = self.handleData(incomingData, byte_request)
			self.logToFile(incomingData, "Skyline_data2")
			if dataList != None:
				TEMP_Value = self.convertToTemp(int(dataList[0]))
				MPH_Value  = self.convertToMPH(int(dataList[3]))
				KMH_Value  = self.convertToKMH(int(dataList[3]))
				RPM_Value  = self.convertToRev(int(dataList[1]), int(dataList[2]))
				BATT_Value = self.convertToBattery(float(dataList[4]))
				TIM_Value = self.convertToTiming(int(dataList[5]))
				TPS_Value = self.convertToTps(int(dataList[6]))
				TURBO_Value = self.convertToTurbo(int(dataList[7]))

# 				INTAKE_Value = self.convertToTemp(int(dataList[7]))
# 				print({'rpm': RPM_Value, 'speed': KMH_Value, 'mph': MPH_Value, 'temp': TEMP_Value, 'batt': BATT_Value, 'turbo': TURBO_Value, 'tps': TPS_Value})
				self.socketio.emit('ecuData', {'rpm': RPM_Value, 'speed': KMH_Value, 'mph': MPH_Value, 'temp': TEMP_Value, 'batt': BATT_Value, 'turbo': TURBO_Value, 'tps': TPS_Value, 'timming': TIM_Value})
				time.sleep(0.002)

	def run(self):
		#         command = '\x5A\x0B\x5A\x01\x5A\x08\x5A\x0C\x5A\x0D\x5A\x03\x5A\x05\x5A\x09\x5A\x13\x5A\x16\x5A\x17\x5A\x1A\x5A\x1C\x5A\x21\xF0'
		command = [0x5A,0x08,0x5A,0x00,0x5A,0x01,0x5A,0x0b,0x5A,0x0c,0x5A,0x16,0x5A,0x0d,0x5A,0x29,0xF0]
		self.PORT.write(command)
		self.consume_data(command)

	def handleData(self, data, byteExpected):
		try:
			frameStarted = False
			print("".join(hex(ord(n)) for n in data))
			for i in xrange(len(data)):
				char = "".join(hex(ord(n)) for n in data[i])
				if(char == "0xff" and frameStarted == False):
					frameStarted = True
					lengthByte = None
					current_data = []
				elif frameStarted:
					if lengthByte == None:
						lengthByte = int(char, 16)
					else:
						current_data.append(int(char, 16))
			if len(current_data) == byteExpected:
				frameStarted = False
				return current_data
		except:
			print("An exception occurred With this HEX: ")	
			print("".join(hex(ord(n)) for n in data))

	def convertToMPH(self,inputData):
		return int(round ((inputData * 2.11) * 0.621371192237334))

	def convertToKMH(self,inputData):
		return int(round(inputData * 2.11))
	
	def convertToTps(self, inputData):
		return int(round(inputData) * 20)
	
	def convertToRev(self, mostSignificantBit, leastSignificantBit):
		return round(((mostSignificantBit << 8) + leastSignificantBit) * 12.5)
	
	def convertToTemp(self,inputData):
		return inputData - 50
	
	def convertToTurbo(self, inputData):
		if inputData < 150:
			return (inputData / 150) - 1.0
		else:
			return (inputData - 150) / 150
	
	def convertToBattery(self,inputData):
		return round(((inputData * 80) / 1000),1)
	
	def convertToMAF(self,inputData):
		return inputData * 5
	
	def convertToAAC(self,inputData):
		return inputData / 2
	
	def convertToInjection(self,inputData):
		return inputData / 100
	
	def convertToTiming(self,inputData):
		return 110 - inputData

	def logToFile(self, data, fileName):
		with open(fileName + '.hex', 'a+') as logFile:
			logFile.write(data)

	def development(self, x):
		test_file = open("test.hex")
		all_lines = test_file.readlines()
		return all_lines[4]
				
	def start(self, socketio):
		if self.enviroment == "production":
			self.start_production(socketio)
		else:
			self.start_development(socketio)

	def start_production(self, socketio):
		self.socketio = socketio
		READ_THREAD = False
		while READ_THREAD == False:
			#Send echo -e -n '\x10' > /dev/ttys006
			self.PORT.flushInput()
			self.PORT.write('\xFF\xFF\xEF')
			time.sleep(2)
			print("Intentando Conexion con Nissan Consult")
			Connected = self.PORT.read(1)
			print "Data Response: ".join(hex(ord(n)) for n in Connected)
			if Connected == '\x10':
				print("Data Aceptada")
				READ_THREAD = True
				self.run()
			else:
				self.PORT.write('\x30')
		
		while READ_THREAD == True:
			print("true") 

	def start_development(self, socketio):
		self.socketio = socketio
		READ_THREAD = False
		while READ_THREAD == False:
			print("Start Development")
			self.run() 

