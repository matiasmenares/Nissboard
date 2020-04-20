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

	def init(self):
		cursorObj = self.con.cursor()
		cursorObj.execute("CREATE TABLE if not exists records(id integer PRIMARY KEY AUTOINCREMENT, date_record datetime)")
		cursorObj.execute("CREATE TABLE if not exists record_has_sensor(id integer PRIMARY KEY AUTOINCREMENT, date_record datetime)")
		cursorObj.execute("CREATE TABLE if not exists sensors(id integer PRIMARY KEY, name text, command text, medition_text text, alert integer, alert_value integer)")
		cursorObj.execute("CREATE TABLE if not exists backgrounds(id integer PRIMARY KEY, name text, url text)")
		cursorObj.execute("CREATE TABLE if not exists dashboards(id integer PRIMARY KEY, name text, red_line integer, yellow_line integer, red_line_rpm integer, yellow_line_rpm integer)")
		cursorObj.execute("CREATE TABLE if not exists analog_channels (id integer PRIMARY KEY, name text not null, pin not null, voltage_resistance integer not null )")
		cursorObj.execute("CREATE TABLE if not exists channel_inputs (id integer PRIMARY KEY, analog_channel_id integer, foreign key(analog_channel_id) references analog_channels(id))")
		cursorObj.execute("CREATE TABLE if not exists channel_outputs (id integer PRIMARY KEY, channel_input_id integer, foreign key(channel_input_id) references channel_inputs(id))")

		cursorObj.execute("CREATE TABLE if not exists measure_groups (id integer PRIMARY KEY, name)")
		cursorObj.execute("CREATE TABLE if not exists measures (id integer PRIMARY KEY, name, formula text, undo_formula text, explanation text, measure_group_id integer, foreign key(measure_group_id) references measure_groups(id))")

		self.con.commit()
		self.set_seed()
		self.close()
		
	def set_seed(self):
		self.set_dashboards_seed()

	def set_dashboards_seed(self):
		cursorObj = self.con.cursor()
		if len(cursorObj.execute('SELECT * FROM dashboards').fetchall()) == 0:
			cursorObj.execute("INSERT INTO dashboards VALUES(1, 'KINEK', '0', '0', '0','0')")
			cursorObj.execute("INSERT INTO dashboards VALUES(2, 'DUST', '0', '0', '0','0')")
			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM sensors').fetchall()) == 0:
			cursorObj.execute("INSERT INTO sensors VALUES(1, 'Water', '0', 'Celcius', '0', '0')")
			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM measure_groups').fetchall()) == 0:
			cursorObj.execute("INSERT INTO measure_groups VALUES(1, 'Pressure (Boost)')")
			cursorObj.execute("INSERT INTO measure_groups VALUES(2, 'Pressure')")
			cursorObj.execute("INSERT INTO measure_groups VALUES(3, 'Temperature')")
			self.con.commit()
		if len(cursorObj.execute('SELECT * FROM measures').fetchall()) == 0:
			#Boost
			cursorObj.execute("INSERT INTO measures VALUES(1, 'Psi', ' * 0.001) * 14 ) - 14)', ' - 14 ) / 14.504)', 'This sensor substract 14 PSI to pressure', 1)")
			cursorObj.execute("INSERT INTO measures VALUES(2, 'Bar', ' * 0.001) - 1.0 ))', ' - 1.0 )', 'This sensor substract 1.0 Bar to pressure', 1)")
			cursorObj.execute("INSERT INTO measures VALUES(3, 'Kilopascal', ' * 0.001) -1.0 ) * 100)', ' - 1.0 )', 'This sensor substract 100 Kilopascal to pressure', 1)")
			cursorObj.execute("INSERT INTO measures VALUES(4, 'Pascale', ' * 0.001) - 1.0) * 100000)', ' - 1.0 )', 'This sensor substract 100000 pascal to pressure', 1)")
			#Pressure
			cursorObj.execute("INSERT INTO measures VALUES(5, 'Psi', ' * 0.001) * 14 ))', ' - 14 ) / 14.504)', 'This sensor measure absolute pressure', 2)")
			cursorObj.execute("INSERT INTO measures VALUES(6, 'Bar', ' * 0.001)))', ' - 1.0 )', 'This measure read absolute pressure', 2)")
			cursorObj.execute("INSERT INTO measures VALUES(7, 'Kilopascal', ' * 0.001)) * 100)', ' - 1.0 )', 'This measure read absolute pressure', 2)")
			cursorObj.execute("INSERT INTO measures VALUES(8, 'Pascale', ' * 0.001))* 100000)', ' - 1.0 )', 'This measure read absolute pressure', 2)")
			#Temperature
			cursorObj.execute("INSERT INTO measures VALUES(9, 'Celcius', ' * 0.001) * 14 ))', ' - 14 ) / 14.504)', 'This sensor Measure Absolute Pressure', 3)")
			cursorObj.execute("INSERT INTO measures VALUES(10, 'Fahrenheit', ' * 0.001) * 14 ))', ' - 14 ) / 14.504)', 'This sensor Measure Absolute Pressure', 3)")
			self.con.commit()


