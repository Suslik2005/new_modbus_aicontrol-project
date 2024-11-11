# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(False)
        MainWindow.resize(230, 452)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255),\n"
"rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setEnabled(False)
        self.balance_frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.balance_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.comboBox = QComboBox(self.balance_frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.label = QLabel(self.balance_frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.balance_frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.balance_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.balance_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"modbus", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b\u0438\u0431\u0440\u043e\u043b\u0432\u043a\u0430 \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0430", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0437\u0430\u0432\u043e\u0434\u0441\u043a\u0443\u044e \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0434\u0430\u0442\u044c \u0442\u0435\u0440\u043c\u043e\u043a\u043e\u043c\u043f\u0435\u043d\u0441\u0430\u0446\u0438\u044e(-)", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0434\u0430\u0442\u044c \u0442\u0435\u0440\u043c\u043e\u043a\u043e\u043c\u043f\u0435\u043d\u0441\u0430\u0446\u0438\u044e(+)", None))

        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u043d\u044f\u0442\u044c", None))
    # retranslateUi

