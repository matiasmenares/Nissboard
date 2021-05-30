import sqlite3
from sqlite3 import Error

class Database():

	def __init__(self):
		self.con = None
		self.cursorObj = None
		self.open_con()

	def open_con(self):
		try:
			self.con = sqlite3.connect('Database.db')
# 			print("Connection is established: Database is created")
		except Error:
			print(Error)
# 		finally:
# 			self.con.close()
	def close(self):
		self.con.close()
	def make_dicts(self, cursor, row):
		return dict((cursor.description[idx][0], value)
			for idx, value in enumerate(row))
	def init(self):
		cursorObj = self.con.cursor()
		cursorObj.execute("CREATE TABLE if not exists records(id integer PRIMARY KEY AUTOINCREMENT, date_record datetime)")
		cursorObj.execute("CREATE TABLE if not exists record_has_sensor(id integer PRIMARY KEY AUTOINCREMENT, date_record datetime)")
		cursorObj.execute("CREATE TABLE if not exists sensors(id integer PRIMARY KEY, name text, command text, medition_text text, alert integer, alert_value integer)")
		cursorObj.execute("CREATE TABLE if not exists backgrounds(id integer PRIMARY KEY, name text, url text)")
		cursorObj.execute("CREATE TABLE if not exists analog_channels (id integer PRIMARY KEY, name text not null, pin not null, voltage_resistance integer not null )")

		self.con.commit()
		self.set_seed()
		self.close()
		
	def set_seed(self):
		self.set_dashboards_seed()

	def set_dashboards_seed(self):
		cursorObj = self.con.cursor()
		if len(cursorObj.execute('SELECT * FROM obd').fetchall()) == 0:
			cursorObj.execute("INSERT INTO obd VALUES(NULL, 'Coolant Temp', 'COOLANT_TEMP', 'Engine Coolant Temperature', NULL )")
			cursorObj.execute("INSERT INTO obd VALUES(NULL, 'Throttle Position', 'THROTTLE_POS', 'Throttle Position Sensor', NULL )")
			cursorObj.execute("INSERT INTO obd VALUES(NULL, 'Fuel Level', 'FUEL_LEVEL', 'Fuel Leven', NULL )")
			cursorObj.execute("INSERT INTO obd VALUES(NULL, 'Rpm', 'RPM', 'Engine RPM', NULL)")
			cursorObj.execute("INSERT INTO obd VALUES(NULL, 'Speed', 'SPEED', 'Vehicle Speed', NULL )")
			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM dashboard').fetchall()) == 0:
			cursorObj.execute("INSERT INTO dashboard VALUES(1, 'KINEK', '0', '0')")
			cursorObj.execute("INSERT INTO dashboard VALUES(2, 'DUST', '0', '0')")
			cursorObj.execute("INSERT INTO dashboard VALUES(3, 'INIT', '0', '0')")
			cursorObj.execute("INSERT INTO dashboard VALUES(4, 'BLUME', '0', '0')")

			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM dashboard_output').fetchall()) == 0:
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'RPM', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 1', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 2', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 3', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 4', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 5', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 6', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 7', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 8', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 9', '1', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 10', '1', NULL)")

			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'RPM', '2', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Speed ', '2', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Turbo', '2', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Coolant', '2', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'TPS', '2', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Battery', '2', NULL)")

			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 1', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 2', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 3', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 4', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 5', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 6', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 7', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 8', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 9', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 10', '3', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Slot 11', '3', NULL)")

			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Speed', '4', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'RPM', '4', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Coolant', '4', NULL)")
			cursorObj.execute("INSERT INTO dashboard_output VALUES(NULL, 'Battery', '4', NULL)")

			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM sensors').fetchall()) == 0:
			cursorObj.execute("INSERT INTO sensors VALUES(1, 'Water', '0', 'Celcius', '0', '0')")
			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM measure_group').fetchall()) == 0:
			cursorObj.execute("INSERT INTO measure_group VALUES(1, 'Pressure (Boost)')")
			cursorObj.execute("INSERT INTO measure_group VALUES(2, 'Pressure')")
			cursorObj.execute("INSERT INTO measure_group VALUES(3, 'Temperature')")
			cursorObj.execute("INSERT INTO measure_group VALUES(4, 'RPM')")
			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM condition').fetchall()) == 0:
			cursorObj.execute("INSERT INTO condition VALUES(1, 'Greater Than', '>')")
			cursorObj.execute("INSERT INTO condition VALUES(2, 'Greater Than or Equal to', '>=')")
			cursorObj.execute("INSERT INTO condition VALUES(3, 'Equal to', '==')")
			cursorObj.execute("INSERT INTO condition VALUES(4, 'Less Than or Equal to', '<=')")
			cursorObj.execute("INSERT INTO condition VALUES(5, 'Less Than', '<')")

		if len(cursorObj.execute('SELECT * FROM alarm_type').fetchall()) == 0:
			cursorObj.execute("INSERT INTO alarm_type VALUES(1, 'warning')")
			cursorObj.execute("INSERT INTO alarm_type VALUES(2, 'danger')")
			cursorObj.execute("INSERT INTO alarm_type VALUES(3, 'invasive danger')")
		if len(cursorObj.execute('SELECT * FROM measure').fetchall()) == 0:
			#Boost
			cursorObj.execute("INSERT INTO measure VALUES(1, 'Psi', ' * 0.001) * 14 ) - 14)', ' - 14 ) / 14.504)', 'This sensor substract 14 PSI to pressure', 1)")
			cursorObj.execute("INSERT INTO measure VALUES(2, 'Bar', ' * 0.001) - 1.0 ))', ' - 1.0 )', 'This sensor substract 1.0 Bar to pressure', 1)")
			cursorObj.execute("INSERT INTO measure VALUES(3, 'Kilopascal', ' * 0.001) -1.0 ) * 100)', ' - 1.0 )', 'This sensor substract 100 Kilopascal to pressure', 1)")
			cursorObj.execute("INSERT INTO measure VALUES(4, 'Pascale', ' * 0.001) - 1.0) * 100000)', ' - 1.0 )', 'This sensor substract 100000 pascal to pressure', 1)")
			#Pressure
			cursorObj.execute("INSERT INTO measure VALUES(5, 'Psi', ' * 0.001) * 14 ))', ' - 14 ) / 14.504)', 'This sensor measure absolute pressure', 2)")
			cursorObj.execute("INSERT INTO measure VALUES(6, 'Bar', ' * 0.001)))', ' - 1.0 )', 'This measure read absolute pressure', 2)")
			cursorObj.execute("INSERT INTO measure VALUES(7, 'Kilopascal', ' * 0.001)) * 100)', ' - 1.0 )', 'This measure read absolute pressure', 2)")
			cursorObj.execute("INSERT INTO measure VALUES(8, 'Pascale', ' * 0.001))* 100000)', ' - 1.0 )', 'This measure read absolute pressure', 2)")
			#Temperature
			cursorObj.execute("INSERT INTO measure VALUES(9, 'Celcius', ' * 0.001) * 14 ))', ' - 14 ) / 14.504)', 'This sensor Measure Absolute Pressure', 3)")
			cursorObj.execute("INSERT INTO measure VALUES(10, 'Fahrenheit', ' * 0.001) * 14 ))', ' - 14 ) / 14.504)', 'This sensor Measure Absolute Pressure', 3)")
			#RPM
			cursorObj.execute("INSERT INTO measure VALUES(NULL, 'Revol. Per. Min.', '))', '))', 'This sensor measure RPM', 4)")

		if len(cursorObj.execute('SELECT * FROM color').fetchall()) == 0:
			cursorObj.execute("INSERT INTO color VALUES(NULL, 'Red', '2345', '255,0,0')")
			cursorObj.execute("INSERT INTO color VALUES(NULL, 'Blue', '2345', '0,0,255')")
			cursorObj.execute("INSERT INTO color VALUES(NULL, 'Green', '2345', '0,255,0')")
			cursorObj.execute("INSERT INTO color VALUES(NULL, 'Yellow', '2345', '255,255,0')")
			self.con.commit()

		if len(cursorObj.execute('SELECT * FROM consult').fetchall()) == 0:
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'Temp', '0x08', 'Colant/Water Temperature')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'MPH', '0x0b', 'Speed in Miles per hours')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'KPH', '0x0b', 'Speed in kilometers per hours')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'RPM', '0x00,0x01', 'Rev. Per Minutes')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'Batery', '0x0c', 'Batery Voltage')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'Timming', '0x16', 'Timming')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'TPS', '0x0d', 'Thottle position')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'AAC', '0x17', '-')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, '02', '0x09', 'Oxigen')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'AF', '0x1a', 'Air Flow')")
			cursorObj.execute("INSERT INTO consult VALUES(NULL, 'Injectors', '0x14', 'Injector Timming')")
		self.con.commit()



