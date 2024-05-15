# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Loggin.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(474, 351)
        Dialog.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"border: 1px solid rgb(44, 49, 58);\n"
"padding-left: 0px;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalWidget = QWidget(Dialog)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setStyleSheet(u"border-radius: 4px;\n"
"border: 4px solid black;\n"
"border-color: rgb(207, 162, 9);\n"
"")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.verticalWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:None;")

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.verticalWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border:None;")

        self.verticalLayout.addWidget(self.label_4)

        self.box_Admin = QComboBox(self.verticalWidget)
        self.box_Admin.setObjectName(u"box_Admin")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.box_Admin.sizePolicy().hasHeightForWidth())
        self.box_Admin.setSizePolicy(sizePolicy)
        self.box_Admin.setMinimumSize(QSize(0, 38))
        self.box_Admin.setStyleSheet(u"background-color: rgba(162, 162, 162,80);\n"
"border:None;\n"
" font-size:18pt; \n"
"font-weight:700;\n"
" color:#fcc101;")

        self.verticalLayout.addWidget(self.box_Admin)

        self.label_2 = QLabel(self.verticalWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border:None;")

        self.verticalLayout.addWidget(self.label_2)

        self.txt_User = QTextEdit(self.verticalWidget)
        self.txt_User.setObjectName(u"txt_User")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_User.sizePolicy().hasHeightForWidth())
        self.txt_User.setSizePolicy(sizePolicy1)
        self.txt_User.setMaximumSize(QSize(16777215, 38))
        self.txt_User.setStyleSheet(u"border:None;\n"
"background-color: rgba(162, 162, 162,80);\n"
" font-size:18pt; \n"
"font-weight:700;\n"
" color:#fcc101;")
        self.txt_User.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.txt_User)

        self.label_3 = QLabel(self.verticalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border:None;")

        self.verticalLayout.addWidget(self.label_3)

        self.line_contra = QLineEdit(self.verticalWidget)
        self.line_contra.setObjectName(u"line_contra")
        self.line_contra.setMaximumSize(QSize(16777215, 38))
        self.line_contra.setStyleSheet(u"background-color: rgba(162, 162, 162,80);\n"
"border:None;\n"
" font-size:18pt; \n"
"font-weight:700;\n"
" color:#fcc101;")

        self.verticalLayout.addWidget(self.line_contra)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_iniciarSesion = QPushButton(self.verticalWidget)
        self.btn_iniciarSesion.setObjectName(u"btn_iniciarSesion")
        self.btn_iniciarSesion.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font:15pt \"Segoe UI\";\n"
"border-radius: 4px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_iniciarSesion)

        self.btn_cancelar = QPushButton(self.verticalWidget)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 85, 127, 150);\n"
"background-color: rgba(218, 0, 0,150);\n"
"font:15pt \"Segoe UI\";\n"
"border-radius: 4px;\n"
"border: 4px solid black;\n"
"border-color:  rgb(218, 0, 0);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:  rgba(218, 0, 0,200);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_cancelar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.verticalWidget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#ffc400;\">Iniciar Sesion</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">Modo:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">Usuario:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">Contrase\u00f1a:</span></p></body></html>", None))
        self.btn_iniciarSesion.setText(QCoreApplication.translate("Dialog", u"Iniciar Sesion", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

