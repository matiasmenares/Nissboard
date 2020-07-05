from obd import OBDStatus
import obd
import time

class ObdEcu:

    def __init__(self, socketoi):
        self.connection = None
        self.socketio = socketoi
        self.initial_conn()

    def initial_conn(self):
        try:
            self.connection = obd.OBD("192.168.1.92", 35000, fast=False)
        except:
            time.sleep(1)
            self.initial_conn()

    def send(self, command):
        try:
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                cmd = obd.commands[command]
                response = self.connection.query(cmd)
                self.socketio.emit('ecuConnection', {'status': True})
                return response.value.magnitude
            else:
                self.socketio.emit('ecuConnection', {'status': False})
                return 0
        except:
            self.socketio.emit('ecuConnection', {'status': False})
            self.connection = None
            self.initial_conn()
            return 0
