import time
from datetime import datetime
from core.serial import PortSerial
from core.database import Database

class Ecu():

	def __init__(self, devise_pah, socketio, enviroment, serial_class):
		self.PORT = None
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
		self.command_live_sensors = [0x5A,0x08,0x5A,0x00,0x5A,0x01,0x5A,0x0b,0x5A,0x0c,0x5A,0x16,0x5A,0x0d,0x5A,0x29,0x5A,0x17,0x5A,0x09,0x5A,0x1a,0x5A,0x14,0x5A,0x15,0xF0]
		self.command_stop = 0x30

	def consume_data(self):
		read_thread = True
		record_id = self.setRecord()
		byte_request = (len(self.command_live_sensors) - 1) / 2
		x = 0
		while read_thread:
			try:
				incomingData = self.PORT.read(17) if self.enviroment == "production" else self.development(x)
				dataList = self.handleData(incomingData, byte_request)
				self.logToFile(incomingData, "Skyline_data2")
				if dataList != None:
					self.TEMP_Value  = self.convertToTemp(int(dataList[0]))
					self.MPH_Value   = self.convertToMPH(int(dataList[3]))
					self.KMH_Value   = self.convertToKMH(int(dataList[3]))
					self.RPM_Value   = self.convertToRev(int(dataList[1]), int(dataList[2]))
					self.BATT_Value  = self.convertToBattery(float(dataList[4]))
					self.TIM_Value   = self.convertToTiming(int(dataList[5]))
					self.TPS_Value   = self.convertToTps(int(dataList[6]))
					self.TURBO_Value = self.convertToTurbo(int(dataList[7]))
					self.AAC_Value   = self.convertToAAC(int(dataList[8]))
					self.O2_Value    = self.convertToO2(dataList[9])
					self.AF_Value    = dataList[10]
					self.INJ_Value   = self.convertToInj(int(dataList[11]), int(dataList[12]))

# 					print({'rpm': RPM_Value, 'speed': KMH_Value, 'mph': MPH_Value, 'temp': TEMP_Value, 'batt': BATT_Value, 'turbo': TURBO_Value, 'tps': TPS_Value, 'timming': TIM_Value, 'aac': AAC_Value, '02': O2_Value, 'af': AF_Value, 'injector': INJ_Value})

					self.socketio.emit('ecuData', {'rpm': self.RPM_Value, 'speed': self.KMH_Value, 'mph': self.MPH_Value, 'temp': self.TEMP_Value, 'batt': self.BATT_Value, 'turbo': self.TURBO_Value, 'tps': self.TPS_Value, 'timming': self.TIM_Value, 'aac': self.AAC_Value, 'O2': self.O2_Value, 'af': self.AF_Value, 'injector': self.INJ_Value})
					self.socketio.emit('ecuConnection', {'status': True})
					self.setAlerts()
					time.sleep(0.001)
			except:
				self.socketio.emit('ecuConnection', {'status': False})
				self.start(self.socketio, True)

	def run(self):
		self.PORT.write(self.command_live_sensors)
		self.consume_data()

	def handleData(self, data, byteExpected):
		try:
			frameStarted = False
# 			self.printHex(data)
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
# 			self.printHex(data)

	def setAlerts(self):
		database = Database()
		cursor = database.con.cursor()
		row = cursor.execute('SELECT * FROM sensors WHERE name = "Water" and alert > 0 ')
		row = row.fetchone()
		if row != None:
			if self.TEMP_Value > row[4]:
				self.socketio.emit('Alerts',{'type': "error", 'text': "Temperatura alta"} )
		database.close()
		return True

	def setRecord(self):
		database = Database()
		cursor = database.con.cursor()
		now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		cursor.execute("INSERT INTO records (id, date_record) VALUES (?,?)", (None, now))
		database.con.commit()

	def convertToMPH(self,inputData):
		return int(round ((inputData * 2.11) * 0.621371192237334))

	def convertToKMH(self,inputData):
		return int(round(inputData * 2.11))
	
	def convertToTps(self, inputData):
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
				
	def start(self, socketio, new_port_instance=False):
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
			print("No Devise connected in "+self.devise_pah)
			self.socketio.emit('ecu_conection', {'status': False})
			time.sleep(2)
		self.PORT = self.port_serial.PORT
		self.start_production()		
	
	def start_production(self):
		READ_THREAD = False
		try:
			while READ_THREAD == False:
				#Send echo -e -n '\x10' > /dev/ttys006
				print("Try connection with Nissan Consult")
				self.PORT.flushInput()
				self.PORT.write('\xFF\xFF\xEF')
				time.sleep(2)
				response = self.PORT.read(1)
				if response == '\x10':
					READ_THREAD = True
					print("Consult datastream Accepted")
					self.run()
				else:
					if response != 0x0:
						self.stop_data_stream()
		except:
			self.socketio.emit('ecuConnection', {'status': False})
			self.start(self.socketio, True)

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
			print "".join(hex(ord(n)) for n in response)
			if response == '\xfe':
				print("Command Stoped")
				acknowledgment = False
				self.run()

