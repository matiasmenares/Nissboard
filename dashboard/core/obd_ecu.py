from obd import OBDStatus
import obd
class ObdEcu:

    def __init__(self, socketoi):
        self.connection = obd.OBD("192.168.1.92", 35000, fast=False)
        self.socketio = socketoi
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
            return 0
