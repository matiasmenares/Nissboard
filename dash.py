from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
import os
import time
import math
import serial
from threading import Lock
import datetime
import socketio
import struct
#Serial
# PORT = serial.Serial('/dev/tty.usbserial-A103NKGZ', 9600, timeout=None)
PORT = serial.Serial('/dev/ttys005', 9600, timeout=None)
#WebServer
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SGOPWEBZWB'
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
            thread = socketio.start_background_task(background_thread)
class ReadStream():

    def __init__(self):
        self.MPH_Value = 0
        self.RPM_Value = 0
        self.TEMP_Value = 0
        self.BATT_Value = 0
        self.MAF_Value = 0
        self.AAC_Value = 0
        self.INJ_Value = 0
        self.TIM_Value = 0
        self.Header = 255
        self.returnBytes = 16
            
    def consume_data(self, command):
	    #echo -e -n '\x04\x78\x00\x4f\x00\xff\x04\x78\x00\x4f\00' > /dev/ttys006
        read_thread = True
        byte_request = (len(command) - 1) / 2
        while read_thread:
            incomingData = PORT.read(11)
            dataList = self.handleData(incomingData, byte_request)
            self.logToFile(incomingData, "Skyline_data")
            if dataList != None:
              TEMP_Value = self.convertToTemp(int(dataList[0]))
              MPH_Value  = self.convertToMPH(int(dataList[3]))
              KMH_Value  = self.convertToKMH(int(dataList[3]))
              RPM_Value  = self.convertToRev(int(dataList[1]), int(dataList[2]))
#             BATT_Value = self.convertToBattery(float(dataList[1]))
#             AAC_Value  = self.convertToAAC(int(dataList[8]))
#             MAF_Value  = self.convertToMAF(int(dataList[5]))
#             print({'rpm': RPM_Value, 'kmh': KMH_Value, 'mph': MPH_Value, 'temp': TEMP_Value, 'battery': BATT_Value, 'aac': AAC_Value, 'maf': MAF_Value})

#             socketio.emit('ecuData', {'rpm': RPM_Value, 'kmh': KMH_Value, 'mph': MPH_Value, 'temp': TEMP_Value, 'battery': BATT_Value, 'aac': AAC_Value, 'maf': MAF_Value})
              socketio.emit('ecuData', {'rpm': RPM_Value, 'kmh': KMH_Value, 'mph': MPH_Value, 'temp': TEMP_Value})
              print({'rpm': RPM_Value, 'kmh': KMH_Value, 'mph': MPH_Value, 'temp': TEMP_Value})
              time.sleep(0.002)

    def run(self):
#         command = '\x5A\x0B\x5A\x01\x5A\x08\x5A\x0C\x5A\x0D\x5A\x03\x5A\x05\x5A\x09\x5A\x13\x5A\x16\x5A\x17\x5A\x1A\x5A\x1C\x5A\x21\xF0'
        command = [0x5A,0x08,0x5A,0x00,0x5A,0x01,0x5A,0x0b,0xF0]
        PORT.write(command)
        self.consume_data(command)

    def handleData(self, data, byteExpected):
        frameStarted = False
#         print("".join(hex(ord(n)) for n in data))
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
    def convertToMPH(self,inputData):
        return int(round ((inputData * 2.11) * 0.621371192237334))

    def convertToKMH(self,inputData):
        return int(round(inputData * 2.11))

    def convertToRev(self, mostSignificantBit, leastSignificantBit):
        return round(((mostSignificantBit << 8) + leastSignificantBit) * 12.5)

    def convertToTemp(self,inputData):
        return inputData - 50

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

    def logToFile(self,data,fileName):
        with open(fileName + '.hex', 'a+') as logFile:
            logFile.write(data)

def background_thread():
	READ_THREAD = False
        while READ_THREAD == False:
             #Send echo -e -n '\x10' > /dev/ttys006
             PORT.flushInput()
             PORT.write('\xFF\xFF\xEF')
             time.sleep(2)
             print("Intentando Conexion con Nissan Consult")
             Connected = PORT.read(1)
             print "Data Response: ".join(hex(ord(n)) for n in Connected)
             if Connected == '\x10':
                 print("Data Aceptada")
                 READ_THREAD = True
                 read = ReadStream()
                 read.run()
#                     PORT.open()
		    
        while READ_THREAD == True:
              print("true") 

if __name__ == '__main__':
    socketio.run(app)