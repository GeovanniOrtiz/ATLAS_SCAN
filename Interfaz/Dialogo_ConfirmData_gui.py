# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialogo_ConfirmData.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(474, 351)
        Dialog.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"border: 6px solid;\n"
"border-color: #e12807;\n"
"border-color: rgb(0, 0, 0);\n"
"padding-left: 0px;\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"\n"
"border: None;\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PartNo = QLabel(Dialog)
        self.PartNo.setObjectName(u"PartNo")
        self.PartNo.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout.addWidget(self.PartNo)

        self.lbl_PartNo = QLabel(Dialog)
        self.lbl_PartNo.setObjectName(u"lbl_PartNo")
        self.lbl_PartNo.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout.addWidget(self.lbl_PartNo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Cantidad = QLabel(Dialog)
        self.Cantidad.setObjectName(u"Cantidad")
        self.Cantidad.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_2.addWidget(self.Cantidad)

        self.lbl_Cantidad = QLabel(Dialog)
        self.lbl_Cantidad.setObjectName(u"lbl_Cantidad")
        self.lbl_Cantidad.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_2.addWidget(self.lbl_Cantidad)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Proveddor = QLabel(Dialog)
        self.Proveddor.setObjectName(u"Proveddor")
        self.Proveddor.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_3.addWidget(self.Proveddor)

        self.lbl_Proveedor = QLabel(Dialog)
        self.lbl_Proveedor.setObjectName(u"lbl_Proveedor")
        self.lbl_Proveedor.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_3.addWidget(self.lbl_Proveedor)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Serial = QLabel(Dialog)
        self.Serial.setObjectName(u"Serial")
        self.Serial.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_4.addWidget(self.Serial)

        self.lbl_Serial = QLabel(Dialog)
        self.lbl_Serial.setObjectName(u"lbl_Serial")
        self.lbl_Serial.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_4.addWidget(self.lbl_Serial)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.OT = QLabel(Dialog)
        self.OT.setObjectName(u"OT")
        self.OT.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_5.addWidget(self.OT)

        self.lbl_OT = QLabel(Dialog)
        self.lbl_OT.setObjectName(u"lbl_OT")
        self.lbl_OT.setStyleSheet(u"border: None;\n"
"")

        self.horizontalLayout_5.addWidget(self.lbl_OT)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_Accept = QPushButton(Dialog)
        self.btn_Accept.setObjectName(u"btn_Accept")
        self.btn_Accept.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font:15pt \"Segoe UI\";\n"
"border-radius: 7px;\n"
"border: 3px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_Accept)

        self.btn_Reject = QPushButton(Dialog)
        self.btn_Reject.setObjectName(u"btn_Reject")
        self.btn_Reject.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 85, 127, 150);\n"
"background-color: rgba(218, 0, 0,150);\n"
"font:15pt \"Segoe UI\";\n"
"border-radius: 7px;\n"
"border: 3px solid black;\n"
"border-color:  rgb(218, 0, 0);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:  rgba(218, 0, 0,200);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_Reject)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">Confirmar Datos</span></p></body></html>", None))
        self.PartNo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#d1d1d1;\">Numero de Parte:</span></p></body></html>", None))
        self.lbl_PartNo.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">3QF121251E</span></p></body></html>", None))
        self.Cantidad.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#d1d1d1;\">Cantidad:</span></p></body></html>", None))
        self.lbl_Cantidad.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">10</span></p></body></html>", None))
        self.Proveddor.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#d1d1d1;\">Proveedor:</span></p></body></html>", None))
        self.lbl_Proveedor.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">6001003941</span></p></body></html>", None))
        self.Serial.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#d1d1d1;\">Serial:</span></p></body></html>", None))
        self.lbl_Serial.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">180215052024091755</span></p></body></html>", None))
        self.OT.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#d1d1d1;\">O.T:</span></p></body></html>", None))
        self.lbl_OT.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">256975</span></p></body></html>", None))
        self.btn_Accept.setText(QCoreApplication.translate("Dialog", u"ACEPTAR", None))
        self.btn_Reject.setText(QCoreApplication.translate("Dialog", u"CANCELAR", None))
    # retranslateUi

