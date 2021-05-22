from obd import OBDStatus
import obd
import time

class ObdEcu:

    def __init__(self, socketoi):
        self.connection = None
        self.socketio = socketoi
        self.initial_conn()
        self.obd = obd

    def initial_conn(self):
        self.connection = obd.OBD("/dev/ttys004", fast=False)

    def send(self, command):
        try:
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                cmd = obd.commands[command]
                response = self.connection.query(cmd)
                return response.value.magnitude
            else:
                self.initial_conn()
                return 0
        except:
            self.socketio.emit('ecuConnection', {'status': False})
            self.connection = None
            print("No Obd2")
            self.initial_conn()
            return 0
