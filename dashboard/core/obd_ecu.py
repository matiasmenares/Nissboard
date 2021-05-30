from obd import OBDStatus
import obd
import time

class ObdEcu:

    def __init__(self, socketoi):
        self.connection = None
        self.socketio = socketoi
        self.running = False
        self.initial_conn()
        self.obd = obd

    def initial_conn(self):
        if not self.running:
            print("[OBD2] Connection Init")
            self.connection = obd.OBD("/dev/ttys005", fast=False)
            self.running = True
            self.socketio.emit('ecuConnection', {'status': True})

    def send(self, command):
        try:
            if self.connection.status() == OBDStatus.CAR_CONNECTED:
                cmd = obd.commands[command]
                response = self.connection.query(cmd)
                if not self.running:
                    self.socketio.emit('ecuConnection', {'status': True})
                return response.value.magnitude
            else:
                self.running = False
                self.initial_conn()
                return 0
        except Exception as ex:
            self.socketio.emit('ecuConnection', {'status': False})
            self.connection = None
            self.running = False
            print(f"[OBD2] No Obd2 Error: {ex}")
            self.initial_conn()
            return 0
