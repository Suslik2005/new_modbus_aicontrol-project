from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from threading import Thread
import time
import random

# Создаем функцию для изменения значения
def update_values(context, interval=5):
    """
    Функция обновляет значение в ячейке 10030 каждые interval секунд.
    """
    address = 10030 - 1  # Преобразование в индекс массива (Modbus адреса начинаются с 1)
    while True:
        # Генерация значения от 1 до 5
        value = random.randint(1, 5)
        # Запись значения в контекст
        context[0].setValues(3, address, [value])
        print(f"Updated address 10030 with value: {value}")
        time.sleep(interval)

# Создаем Modbus Slave Context
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*10000),  # Дискретные входы
    co=ModbusSequentialDataBlock(0, [0]*10000),  # Коилы
    hr=ModbusSequentialDataBlock(0, [0]*10000),  # Холдинговые регистры
    ir=ModbusSequentialDataBlock(0, [0]*10000),  # Входные регистры
)

# Создаем серверный контекст
context = ModbusServerContext(slaves=store, single=True)

# Настраиваем идентификацию устройства
identity = ModbusDeviceIdentification()
identity.VendorName = 'TestServer'
identity.ProductCode = 'TS'
identity.VendorUrl = 'http://example.com'
identity.ProductName = 'Modbus Test Server'
identity.ModelName = 'Modbus Server'
identity.MajorMinorRevision = '1.0'

# Запускаем поток для обновления значений
thread = Thread(target=update_values, args=(store,))
thread.daemon = True
thread.start()

# Запускаем сервер
print("Starting Modbus TCP Server...")
StartTcpServer(context, identity=identity, address=("0.0.0.0", 502))
