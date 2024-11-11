import sys
import threading
import time

import PySide6
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from pymodbus.client import ModbusTcpClient

from main_window import Ui_MainWindow


class Modbus(QMainWindow):
    def __init__(self):
        super(Modbus, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.client = None
        #словарь для отправки значений
        self.main_dict = {"калибролвка отключена": 1, 'начать калибровку': 2, "сохранить калибровку": 3,
                          "вернуть заводскую калибровку": 4, "задать термокомпенсацию(-)": 5,
                          "задать термокомпенсацию(+)": 6}
        #кнопка подключения
        self.ui.pushButton.clicked.connect(self.connection)
        #кнопка для передачи значения в "действия при калибровке"
        self.ui.pushButton_2.clicked.connect(self.ask)
    #при отправке значения запускается поток
    def potok(self):
        monitoring_thread = threading.Thread(target=self.surveillance())
        monitoring_thread.daemon = True  # Закрыть поток при завершении программы
        monitoring_thread.start()
    def surveillance(self):
        while True:
            time.sleep(10)
            result = self.client.read_holding_registers(10031, 1)
            print(result)



    #функция для отправки значения в 10030 индекс
    def ask(self):
        vaalue = self.ui.comboBox_2.currentText()
        print(vaalue)
        print(self.main_dict[vaalue])
        #отправка выбранной команды
        self.client.write_register(10030, self.main_dict[vaalue])
        self.potok()
#
    #подключение к ModbusTcp
    def connection(self):
        self.client = ModbusTcpClient('192.168.55.79')
        button = self.ui.pushButton
        #значение при подключении (True/False)
        a = self.client.connect()
        #есть подключение - кнопка зеленая, нет подключения - кнопка красная
        if a:
            button.setStyleSheet(
                'QPushButton {background-color: rgba(0,255,0,30);width: 230px; height: 50 px; color: white;}')
        else:
            button.setStyleSheet(
                'QPushButton {background-color: rgba(255,0,0,30);width: 230px; height: 50 px; color: white;}')
            print("ошибка подключения")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Modbus()
    window.show()
    sys.exit(app.exec())



