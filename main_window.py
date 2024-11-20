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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(491, 227)
        MainWindow.setStyleSheet(u"background-color:  rgba(160,160,160, 130);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"main_window", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ip", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435  \u0438\u0441\u043f ip", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430 \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0430", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0447\u0430\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u0437\u0430\u0432\u043e\u0434\u0441\u043a\u0443\u044e \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0434\u0430\u0442\u044c \u0442\u0435\u0440\u043c\u043e\u043a\u043e\u043c\u043f\u0435\u043d\u0441\u0430\u0446\u0438\u044e(-)", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0434\u0430\u0442\u044c \u0442\u0435\u0440\u043c\u043e\u043a\u043e\u043c\u043f\u0435\u043d\u0441\u0430\u0446\u0438\u044e(+)", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0430\u0434\u0438\u044f \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u043e\u043a", None))
    # retranslateUi

