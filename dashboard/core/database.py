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

