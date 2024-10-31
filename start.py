from PyQt5.QtWidgets import QMainWindow
from pymodbus.client import ModbusTcpClient


class Modbus(QMainWindow):
    def __init__(self):
        super(Modbus, self).__init__()
        self.client = None
        self.main_dict = {"калибролвка отключена": 0, 'начать калибровку': 1, "сохранить калибровку": 2,
                          "вернуть заводскую калибровку": 3, "задать термокомпенсацию(-)": 4, "задать термокомпенсацию(+)": 5}

    def connection(self):
        self.client = ModbusTcpClient('192.168.55.79')
        try:
            self.client.connect()
        except:
            pass


client.write_register(10030, 2)
result = client.read_holding_registers(10031, 1)
print(result)
client.close()
