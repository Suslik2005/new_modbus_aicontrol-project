import sys
import threading
import time
import os

import PySide6
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from pymodbus.client import ModbusTcpClient

from main_window import Ui_MainWindow

DB_NAME = "ip.db"
class Modbus(QMainWindow):
    def __init__(self):
        super(Modbus, self).__init__()
        #создание txt файла с последними ip
        self.FILE_NAME = "ips.txt"
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w") as file:
                pass  # Просто создаём пустой файл
        #до сюда
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.client = None
        self.control_result = 0
        self.ui.pushButton_2.setEnabled(False)
        self.stop_thread = False
        # словарь для отправки значений
        self.main_dict = {"калибролвка отключена": 1, 'начать калибровку': 2, "сохранить калибровку": 3,
                          "вернуть заводскую калибровку": 4, "задать термокомпенсацию(-)": 5,
                          "задать термокомпенсацию(+)": 6}
        self.stadiya_colibrovki = {1: "калибровка отключена", 2: "подайте 4мА (1 В)", 3: "подайте 20мА (5 В)",
                                   4: "сохранить калибровку?", 5: "подайте 8мА (2 В)", 6: "подайте 12мА (3 В)",
                                   7: "подайте 16мА (4 В)", 8: "ожидание стабилизации сигнала", 9: "калиброка"}
        self.refresh_ips()
        # кнопка подключения
        self.ui.pushButton.clicked.connect(self.connection)
        # кнопка для передачи значения в "действия при калибровке"
        self.ui.pushButton_2.clicked.connect(self.ask)
        self.ui.pushButton_3.clicked.connect(self.nonconnection)

    # при отправке значения запускается поток
    def nonconnection(self):
        self.stop_thread = True
        self.ui.comboBox.clear()
        self.ui.pushButton.setEnabled(True)
        self.client.close()
    def write_ip_to_file(self, ip):
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{ip}\n")
        print(f"IP '{ip}' записан в файл.")
    def potok(self):
        monitoring_thread = threading.Thread(target=self.surveillance)
        monitoring_thread.daemon = True  # Закрыть поток при завершении программы
        monitoring_thread.start()

    def surveillance(self):
        label = self.ui.label
        while not self.stop_thread:
            time.sleep(10)
            result = self.client.read_holding_registers(10031, 1)
            print(result)
            if self.control_result != self.stadiya_colibrovki[result]:
                self.control_result = self.stadiya_colibrovki[int(result)]
                label.clear()  # Очищаем текст в QLabel
                label.setText(self.control_result)

    # Функция для чтения IP из файла в обратном порядке
    def read_ips_from_file(self):
        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()
        return [line.strip() for line in reversed(lines)]  # Удаляем лишние символы
    # функция для отправки значения в 10030 индекс
    def ask(self):
        vaalue = self.ui.comboBox_2.currentText()
        print(vaalue)
        print(self.main_dict[vaalue])
        # отправка выбранной команды
        self.client.write_register(10030, self.main_dict[vaalue])
        self.potok()

    def refresh_ips(self):
        self.ui.comboBox.clear()
        ips = self.read_ips_from_file()
        self.ui.comboBox.addItems(ips)
        print("IP-адреса обновлены в comboBox.")

    # подключение к ModbusTcp
    def connection(self):
        text = self.ui.comboBox.currentText()
        self.client = ModbusTcpClient(text)
        button = self.ui.pushButton
        # значение при подключении (True/False)
        a = self.client.connect()
        # есть подключение - кнопка зеленая, нет подключения - кнопка красная
        if a:
            button.setEnabled(False)
            button.setStyleSheet("""
                QPushButton:disabled {
                    background-color: rgba(0,255,0,30);
                    width: 230px; 
                    height: 50 px;
                    color: white;
                }
            """)
            self.ui.pushButton_2.setEnabled(True)
            self.write_ip_to_file(text)
            self.refresh_ips()

        else:
            button.setStyleSheet(
                'QPushButton {background-color: rgba(255,0,0,30);width: 230px; height: 50 px; color: white;}')
            print("ошибка подключения")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Modbus()
    window.show()
    sys.exit(app.exec())
