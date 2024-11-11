import sys
import threading

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
        self.main_dict = {"калибролвка отключена": 0, 'начать калибровку': 1, "сохранить калибровку": 2,
                          "вернуть заводскую калибровку": 3, "задать термокомпенсацию(-)": 4,
                          "задать термокомпенсацию(+)": 5}
        self.ui.pushButton.clicked.connect(self.connection)
        self.ui.pushButton_2.clicked.connect(self.ask)

    def potok(self, a):
        for i in range(3):
            b = PySide6.QtWidgets.QTableWidgetItem(str(a[i+1]))
            self.ui.tableWidget_2.setItem(self.counter - 1, i, b)
        t1 = threading.Thread(target=self.revizor_vivod, args=(), daemon=True)
        t1.start()
        # t1.join()
    def ask(self):
        vaalue = self.ui.comboBox.currentText()
        self.client.write_register(10030, vaalue)
#        result = self.client.read_holding_registers(10031, 1)
#        print(result)

    def connection(self):
        self.client = ModbusTcpClient('192.168.55.79')
        button = self.ui.pushButton
        try:
            self.client.connect()

            button.setStyleSheet(
                'QPushButton {background-color: rgba(0,255,0,30);width: 230px; height: 50 px; color: white;}')
        except:
            button.setStyleSheet(
                'QPushButton {background-color: rgba(255,0,0,30);width: 230px; height: 50 px; color: white;}')
            print("ошибка подключения")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Modbus()
    window.show()
    sys.exit(app.exec())



