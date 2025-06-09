# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(486, 371)
        MainWindow.setStyleSheet(u" QMessageBox {\n"
"            background: white;  /* Fondo blanco */\n"
"            border: 2px solid #CCCCCC;  /* Borde gris claro */\n"
"            border-radius: 10px;  /* Esquinas redondeadas */\n"
"            padding: 10px;\n"
"        }\n"
"\n"
"        QMessageBox QLabel {\n"
"            background: transparent;\n"
"            color: #333333;  /* Texto oscuro elegante */\n"
"            font-size: 14px;\n"
"            font-weight: bold;\n"
"        }\n"
"\n"
"        QMessageBox QLabel[objectName=\"qt_msgbox_label\"] {\n"
"            background: transparent;\n"
"        }\n"
"\n"
"        /* Botones con dise\u00f1o moderno */\n"
"        QMessageBox QPushButton {\n"
"            background-color: #0078D7;  /* Azul profesional (similar a Windows) */\n"
"            color: white;\n"
"            border: 1px solid #005A9E;\n"
"            padding: 8px 16px;\n"
"            font-size: 13px;\n"
"            font-weight: bold;\n"
"            border-radius: 5px;\n"
"            min-width: 80px;\n"
"  "
                        "      }\n"
"\n"
"        QMessageBox QPushButton:hover {\n"
"            background-color: #005A9E;\n"
"        }\n"
"\n"
"        QMessageBox QPushButton:pressed {\n"
"            background-color: #004680;\n"
"        }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgba(0, 0, 0, 180);")
        self.lbl_video = QLabel(self.widget)
        self.lbl_video.setObjectName(u"lbl_video")
        self.lbl_video.setGeometry(QRect(-4, -6, 485, 375))
        self.verticalWidget = QWidget(self.widget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setGeometry(QRect(22, 24, 423, 315))
        self.verticalWidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 130);")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_titulo = QLabel(self.verticalWidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.verticalLayout_2.addWidget(self.lbl_titulo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_Station = QLabel(self.verticalWidget)
        self.lbl_Station.setObjectName(u"lbl_Station")
        self.lbl_Station.setStyleSheet(u"background-color: none;")

        self.verticalLayout_3.addWidget(self.lbl_Station)

        self.box_station = QComboBox(self.verticalWidget)
        self.box_station.addItem("")
        self.box_station.addItem("")
        self.box_station.addItem("")
        self.box_station.setObjectName(u"box_station")
        self.box_station.setStyleSheet(u"background-color: rgba(52, 152, 219, 180); /* Color semi-transparente */\n"
"            color: white;\n"
"            font-size: 16px;\n"
"            padding: 5px;\n"
"            border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.box_station)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_COM = QLabel(self.verticalWidget)
        self.lbl_COM.setObjectName(u"lbl_COM")
        self.lbl_COM.setStyleSheet(u"background-color: none;")

        self.verticalLayout_4.addWidget(self.lbl_COM)

        self.box_com = QComboBox(self.verticalWidget)
        self.box_com.setObjectName(u"box_com")
        self.box_com.setStyleSheet(u"background-color: rgba(52, 152, 219, 180); /* Color semi-transparente */\n"
"            color: white;\n"
"            font-size: 16px;\n"
"            padding: 5px;\n"
"            border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.box_com)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_Label = QLabel(self.verticalWidget)
        self.lbl_Label.setObjectName(u"lbl_Label")
        self.lbl_Label.setStyleSheet(u"background-color: none;")

        self.verticalLayout_5.addWidget(self.lbl_Label)

        self.box_label = QComboBox(self.verticalWidget)
        self.box_label.addItem("")
        self.box_label.addItem("")
        self.box_label.setObjectName(u"box_label")
        self.box_label.setStyleSheet(u"background-color: rgba(52, 152, 219, 180); /* Color semi-transparente */\n"
"            color: white;\n"
"            font-size: 16px;\n"
"            padding: 5px;\n"
"            border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.box_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_aceptar = QPushButton(self.verticalWidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setStyleSheet(u"\n"
"            \n"
"\n"
"QPushButton {\n"
"    background-color: rgba(39, 174, 96, 0.7); /* Verde con transparencia */\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgba(39, 174, 96, 1); /* verde opaco */\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_aceptar)

        self.btn_cancelar = QPushButton(self.verticalWidget)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(231, 76, 60, 0.7); /* Rojo con transparencia */\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    padding: 10px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgba(231, 76, 60, 1); /* Rojo opaco */\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_cancelar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_video.setText("")
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#c8c8c8;\">CONFIGURACION</span></p></body></html>", None))
        self.lbl_Station.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#b4b4b4;\">ESTACION</span></p></body></html>", None))
        self.box_station.setItemText(0, QCoreApplication.translate("MainWindow", u"Estacion 3", None))
        self.box_station.setItemText(1, QCoreApplication.translate("MainWindow", u"Estacion 4", None))
        self.box_station.setItemText(2, QCoreApplication.translate("MainWindow", u"Estacion 5", None))

        self.lbl_COM.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#b4b4b4;\">COM</span></p></body></html>", None))
        self.lbl_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; color:#b4b4b4;\">ETIQUETA</span></p></body></html>", None))
        self.box_label.setItemText(0, QCoreApplication.translate("MainWindow", u"DMC", None))
        self.box_label.setItemText(1, QCoreApplication.translate("MainWindow", u"CODIGO BARRAS", None))

        self.btn_aceptar.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
    # retranslateUi

