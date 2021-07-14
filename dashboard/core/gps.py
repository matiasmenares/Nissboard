import pynmea2
import time
from termcolor import colored
from core.serial import PortSerial
import io

class Gps():

	def __init__(self, socketio, gps_path, serial_class):
		self.socketio = socketio
		self.gps_path = gps_path
		self.port_serial = PortSerial(gps_path, serial_class)
		self.PORT = None
		self.GPRMC = None
		self.GPGGA = None

	def start(self):
		print("[GPS] Start GPS")
		while self.port_serial.set_port():
			print(f"[GPS] No GPS Devise connected in {self.gps_path}")
			self.socketio.emit('gpsConnection', {'status': False})
			time.sleep(2)
		self.PORT = self.port_serial.PORT
		try:
			while True:
				self.set_gps_data()
				self.parse_gps()
		except Exception as e:
			self.port_serial.close()
			self.socketio.emit('gpsConnection', {'status': False})
			print(f"[GPS] Error in GPS parse: {e}")
			self.start()
			time.sleep(2)

	def set_gps_data(self):
		try:
			gps = self.PORT.readline().decode()
			if '$GPRMC' in gps:
				self.GPRMC =  pynmea2.parse(gps)
			elif '$GPGGA' in gps:
				self.GPGGA =  pynmea2.parse(gps)
		except Exception as e:
			print(f"[GPS] Error in GPS parse: {e}")
			return None

	def parse_gps(self):
		if self.GPRMC != None and self.GPGGA != None:
			self.socketio.emit('gpsConnection', {'status': True, "signal": self.signal(self.GPGGA.lat, self.GPGGA.lon) })
			self.socketio.emit("gps", {"speed_knots": self.GPRMC.spd_over_grnd,"speed_kph": self.convert_distance(self.GPRMC.spd_over_grnd)["km"] ,"speed_miles": self.convert_distance(self.GPRMC.spd_over_grnd)["miles"], "timestamp": str(self.GPGGA.timestamp),"lat": self.GPGGA.latitude, "lat_dir": self.GPGGA.lat_dir, "lon": self.GPGGA.longitude, "lon_dir": self.GPGGA.lon_dir, "altitude": self.GPGGA.altitude, "altitude_unit": self.GPGGA.altitude_units, "sat_numbers": self.GPGGA.num_sats})
			self.GPRMC = None
			self.GPGGA = None

	def parse_gps_old(self):
		try:
			gps = self.PORT.readline().decode()
			if gps.find('GGA') > 0:
				msg = pynmea2.parse(gps)
				print(gps)
				print("-----")
				self.socketio.emit('gpsConnection', {'status': True, "signal": self.signal(msg.lat, msg.lon) })
				self.socketio.emit("gps", {"timestamp": str(msg.timestamp),"lat": msg.latitude, "lat_dir": msg.lat_dir, "lon": msg.longitude, "lon_dir": msg.lon_dir, "altitude": msg.altitude, "altitude_unit": msg.altitude_units, "sat_numbers": msg.num_sats})
				# print ("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s " % (msg.timestamp, msg.latitude, msg.lat_dir, msg.longitude, msg.lon_dir,msg.altitude, msg.altitude_units, msg.num_sats))
		except:
			print("Error")
			raise TypeError("[GPS] Error parsing gps data")


	def signal(self, lat, lon):
		if lat == "" or lon == "":
			return False
		else:
			return True

	def convert_distance(self, knots):
		km = knots * 1.8520
		miles = knots *  1.151
		return {"km": round(km), "miles": round(miles)}
			
