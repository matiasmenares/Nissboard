import obd
import time
from os import system, name 

connection = obd.OBD("192.168.1.92", 35000, fast=False)

while True:
	rpm = connection.query(obd.commands['RPM']) # send the command, and parse the response
	speed = connection.query(obd.commands.SPEED) # send the command, and parse the response
	fuel = connection.query(obd.commands.FUEL_LEVEL) # send the command, and parse the response
	throttle = connection.query(obd.commands.THROTTLE_POS) # send the command, and parse the response
	intake_t = connection.query(obd.commands.INTAKE_TEMP) # send the command, and parse the response

	print(rpm.value) # returns unit-bearing values thanks to Pint
	print(speed.value) # returns unit-bearing values thanks to Pint
	print(fuel.value) # returns unit-bearing values thanks to Pint
	print(throttle.value) # returns unit-bearing values thanks to Pint
	print(intake_t.value) # returns unit-bearing values thanks to Pint

	system('clear')

# def new_value(response):
# 	print(response)
# 
# # keep track of the car's RPM
# connection.watch(obd.commands.RPM, callback=new_value)
# connection.start()
# time.sleep(5) # do other work in the main thread
