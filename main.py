from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import threading
import time

class ModbusServer:
    def __init__(self, host="0.0.0.0", port=502):
        # Настройка хранилища данных
        self.store = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0] * 10000),
            co=ModbusSequentialDataBlock(0, [0] * 10000),
            hr=ModbusSequentialDataBlock(0, [0] * 10000),
            ir=ModbusSequentialDataBlock(0, [0] * 10000)
        )
        self.context = ModbusServerContext(slaves=self.store, single=True)
        self.host = host
        self.port = port
        self.identity = ModbusDeviceIdentification()
        self.identity.VendorName = 'ExampleVendor'
        self.identity.ProductCode = 'EM'
        self.identity.VendorUrl = 'http://example.com'
        self.identity.ProductName = 'ModbusServer'
        self.identity.ModelName = 'Modbus Server Example'
        self.identity.MajorMinorRevision = '1.0'

    def start_register_update_thread(self):
        def update_register():
            value = 1
            while True:
                # Обновляем значение регистра
                self.store.setValues(3, 10030, [value])
                print(f"Значение регистра 10030 изменено на: {value}")
                value = value % 8 + 1  # Переключение значений от 1 до 8
                time.sleep(5)

        update_thread = threading.Thread(target=update_register, daemon=True)
        update_thread.start()

    def run(self):
        self.start_register_update_thread()
        print(f"Сервер Modbus запущен на {self.host}:{self.port}")
        # Вызов сервера TCP
        StartTcpServer(self.context, identity=self.identity, address=(self.host, self.port))

if __name__ == "__main__":
    server = ModbusServer()
    server.run()
#pip install pymodbus==2.5.3
