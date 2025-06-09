# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Rugosimetro.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1032, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1366, 760))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        sizePolicy.setHeightForWidth(self.styleSheet.sizePolicy().hasHeightForWidth())
        self.styleSheet.setSizePolicy(sizePolicy)
        self.styleSheet.setMaximumSize(QSize(1366, 760))
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(255,196);\n"
"}\n"
"QPushButton:unchecked {\n"
"    background-color: rgb(33,37,43);\n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margi"
                        "n: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	padding-left: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/Cat_logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"/*Titulos de la app*/\n"
"#titleLeftApp { font:16pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 14pt \"Segoe UI \"; color: rgb(255, 233, 51 ); }\n"
"\n"
"/*Usuario*/\n"
"#user { font:16pt \"Segoe UI Semibold\"; }\n"
"#lbl_user { font: 16pt \"Segoe UI Semibold\"; color: rgb(255, 233, 51 ); }\n"
"\n"
"/*Modelo del HVAC*/\n"
"#model { font:16pt \"Segoe UI "
                        "Semibold\"; }\n"
"#lbl_model { font: 16pt \"Segoe UI Semibold\"; color: rgb(255, 233, 51 ); }\n"
"\n"
"/*Modelo del HVAC*/\n"
"#mSerial{ font:16pt \"Segoe UI Semibold\"; }\n"
"#lbl_Serial1 { font: 16pt \"Segoe UI Semibold\"; color: rgb(225, 40, 7);; }\n"
"\n"
"#lbl_nPiezas { font: 16pt \"Segoe UI Semibold\"; color: rgb(225, 40, 7); }\n"
"\n"
"\n"
"\n"
"\n"
"/* MENUS */\n"
"#leftMenuFramee .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 10px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#leftMenuFramee .QPushButton:hover {\n"
"	/*background-color: rgb(40, 44, 52);*/\n"
"	background-color: rgb(225, 40, 7);\n"
"}\n"
"#leftMenuFramee .QPushButton:pressed {	\n"
"	/*background-color: rgb(255, 233, 51 );*/\n"
"	background-color: rgb(225, 40, 7);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background"
                        "-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Estilos para el bot\u00f3n cuando est\u00e1 checkeado */\n"
"#settingsTopBtn.QPushButton:checked {\n"
"    background-color: rgb(255,196,0);\n"
"}\n"
"\n"
"/* Estilos para el bot\u00f3n cuando no est\u00e1 checkeado */\n"
"#settingsTopBtn.QPushButton:unchecked {\n"
"    background-color: rgb(33,37,43);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padd"
                        "ing-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Estilos para el bot\u00f3n cuando est\u00e1 checkeado */\n"
"#toggleButton.QPushButton:checked {\n"
"    /*background-color: rgb(255,196,0);*/\n"
"	background-color: rgb(225, 40, 7);\n"
"}\n"
"\n"
"/* Estilos para el bot\u00f3n cuando no est\u00e1 checkeado */\n"
"#toggleButton.QPushButton:unchecked {\n"
"    background-color: rgb(33,37,43);\n"
"}\n"
"\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	/*background-color: rgb(255,196,0)*/\n"
"	background-color: rgb(225, 40, 7);\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	backgroun"
                        "d-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"/*#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }*/\n"
"#extraCloseColumnBtn:pressed {background-color: rgb(255, 233, 51 ); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushB"
                        "utton:pressed {	\n"
"	background-color: rgb(255, 233, 51 );\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons_2 .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons_2 .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons_2.QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: transparent; /*rgb(44, 44, 52);*/ }\n"
"#themeSettingsTopDetail { background-color: rgb(255,196,0); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-si"
                        "ze: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(255, 233, 51 );\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Estilo para el checkbox personalizado cuando est\u00e1 marcado */\n"
"#CheckList_page.QCheckBox:checked {\n"
"    background-color: yellow; /* Cambia el color de fondo a amarillo solo cuando el checkbox est\u00e1 marcado */\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        sizePolicy.setHeightForWidth(self.bgApp.sizePolicy().hasHeightForWidth())
        self.bgApp.setSizePolicy(sizePolicy)
        self.bgApp.setMinimumSize(QSize(0, 0))
        self.bgApp.setMaximumSize(QSize(1366, 760))
        self.horizontalLayout = QHBoxLayout(self.bgApp)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        sizePolicy.setHeightForWidth(self.leftMenuBg.sizePolicy().hasHeightForWidth())
        self.leftMenuBg.setSizePolicy(sizePolicy)
        self.leftMenuBg.setMinimumSize(QSize(200, 0))
        self.leftMenuBg.setMaximumSize(QSize(84, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.HLine)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.leftMenuFramee = QFrame(self.leftMenuBg)
        self.leftMenuFramee.setObjectName(u"leftMenuFramee")
        sizePolicy.setHeightForWidth(self.leftMenuFramee.sizePolicy().hasHeightForWidth())
        self.leftMenuFramee.setSizePolicy(sizePolicy)
        self.leftMenuFrame = QVBoxLayout(self.leftMenuFramee)
        self.leftMenuFrame.setSpacing(8)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setContentsMargins(9, -1, 9, -1)
        self.topLogoInfo = QFrame(self.leftMenuFramee)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(50, 40))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 40))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(62, 12, 115, 35))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftApp.setWordWrap(False)
        self.label_4 = QLabel(self.topLogoInfo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(3, 0, 51, 41))
        self.label_4.setStyleSheet(u"")
        self.label_4.setTextFormat(Qt.TextFormat.PlainText)
        self.label_4.setPixmap(QPixmap(u":/images/images/logovw.png"))
        self.label_4.setScaledContents(True)
        self.titleLeftApp_2 = QLabel(self.topLogoInfo)
        self.titleLeftApp_2.setObjectName(u"titleLeftApp_2")
        self.titleLeftApp_2.setGeometry(QRect(72, -6, 93, 27))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.titleLeftApp_2.setFont(font1)
        self.titleLeftApp_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftApp_2.setWordWrap(False)

        self.leftMenuFrame.addWidget(self.topLogoInfo)

        self.toggleButton = QPushButton(self.leftMenuFramee)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setAutoFillBackground(False)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")
        self.toggleButton.setCheckable(True)

        self.leftMenuFrame.addWidget(self.toggleButton)

        self.btn_home = QPushButton(self.leftMenuFramee)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png);")

        self.leftMenuFrame.addWidget(self.btn_home)

        self.btn_printer = QPushButton(self.leftMenuFramee)
        self.btn_printer.setObjectName(u"btn_printer")
        self.btn_printer.setMinimumSize(QSize(45, 45))
        self.btn_printer.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-external-link.png);")

        self.leftMenuFrame.addWidget(self.btn_printer)

        self.btn_Report = QPushButton(self.leftMenuFramee)
        self.btn_Report.setObjectName(u"btn_Report")
        self.btn_Report.setMinimumSize(QSize(0, 45))
        self.btn_Report.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);\n"
"background-image: url(:/icons/images/icons/cil-code.png);")

        self.leftMenuFrame.addWidget(self.btn_Report)

        self.btn_Master = QPushButton(self.leftMenuFramee)
        self.btn_Master.setObjectName(u"btn_Master")
        self.btn_Master.setMinimumSize(QSize(0, 45))
        self.btn_Master.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-notes.png);")

        self.leftMenuFrame.addWidget(self.btn_Master)

        self.btn_DataMatrix = QPushButton(self.leftMenuFramee)
        self.btn_DataMatrix.setObjectName(u"btn_DataMatrix")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_DataMatrix.sizePolicy().hasHeightForWidth())
        self.btn_DataMatrix.setSizePolicy(sizePolicy1)
        self.btn_DataMatrix.setMinimumSize(QSize(0, 45))
        self.btn_DataMatrix.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-featured-playlist.png);")

        self.leftMenuFrame.addWidget(self.btn_DataMatrix)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftMenuFrame.addItem(self.verticalSpacer_3)

        self.widget_2 = QWidget(self.leftMenuFramee)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalSpacer = QSpacerItem(0, 134, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.lb_statePortCom = QLabel(self.widget_2)
        self.lb_statePortCom.setObjectName(u"lb_statePortCom")
        self.lb_statePortCom.setMidLineWidth(0)

        self.verticalLayout_7.addWidget(self.lb_statePortCom)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.leftMenuFrame.addWidget(self.widget_2)

        self.btn_configData = QPushButton(self.leftMenuFramee)
        self.btn_configData.setObjectName(u"btn_configData")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_configData.sizePolicy().hasHeightForWidth())
        self.btn_configData.setSizePolicy(sizePolicy2)
        self.btn_configData.setMinimumSize(QSize(0, 45))
        self.btn_configData.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x-circle.png);")
        self.btn_configData.setCheckable(True)

        self.leftMenuFrame.addWidget(self.btn_configData)


        self.verticalLayout_3.addWidget(self.leftMenuFramee)


        self.horizontalLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        sizePolicy.setHeightForWidth(self.contentBox.sizePolicy().hasHeightForWidth())
        self.contentBox.setSizePolicy(sizePolicy)
        self.contentBox.setMaximumSize(QSize(1366, 760))
        self.contentBox.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.contentBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        sizePolicy.setHeightForWidth(self.contentTopBg.sizePolicy().hasHeightForWidth())
        self.contentTopBg.setSizePolicy(sizePolicy)
        self.contentTopBg.setMaximumSize(QSize(1100, 16777215))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 9, 0, 0)
        self.label = QLabel(self.contentTopBg)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font:16pt \"Segoe UI Semibold\";")

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox_COM = QComboBox(self.contentTopBg)
        self.comboBox_COM.setObjectName(u"comboBox_COM")
        self.comboBox_COM.setMinimumSize(QSize(100, 0))
        self.comboBox_COM.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")

        self.horizontalLayout_2.addWidget(self.comboBox_COM)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.CutOff = QLabel(self.contentTopBg)
        self.CutOff.setObjectName(u"CutOff")
        self.CutOff.setStyleSheet(u"font:16pt \"Segoe UI Semibold\";")

        self.horizontalLayout_2.addWidget(self.CutOff)

        self.comboBox_cutOff = QComboBox(self.contentTopBg)
        self.comboBox_cutOff.addItem("")
        self.comboBox_cutOff.addItem("")
        self.comboBox_cutOff.addItem("")
        self.comboBox_cutOff.addItem("")
        self.comboBox_cutOff.setObjectName(u"comboBox_cutOff")
        self.comboBox_cutOff.setMinimumSize(QSize(100, 0))
        self.comboBox_cutOff.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")

        self.horizontalLayout_2.addWidget(self.comboBox_cutOff)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lbl_secciones = QLabel(self.contentTopBg)
        self.lbl_secciones.setObjectName(u"lbl_secciones")
        self.lbl_secciones.setStyleSheet(u"font:16pt \"Segoe UI Semibold\";")

        self.horizontalLayout_2.addWidget(self.lbl_secciones)

        self.comboBox_Secciones = QComboBox(self.contentTopBg)
        self.comboBox_Secciones.addItem("")
        self.comboBox_Secciones.addItem("")
        self.comboBox_Secciones.addItem("")
        self.comboBox_Secciones.addItem("")
        self.comboBox_Secciones.addItem("")
        self.comboBox_Secciones.setObjectName(u"comboBox_Secciones")
        self.comboBox_Secciones.setMinimumSize(QSize(100, 0))
        self.comboBox_Secciones.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")

        self.horizontalLayout_2.addWidget(self.comboBox_Secciones)

        self.espaciador_model = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.espaciador_model)

        self.label_2 = QLabel(self.contentTopBg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font:16pt \"Segoe UI Semibold\";")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.horizontalLayout_2.addLayout(self.horizontalLayout_12)

        self.rightButtons_2 = QFrame(self.contentTopBg)
        self.rightButtons_2.setObjectName(u"rightButtons_2")
        self.rightButtons = QHBoxLayout(self.rightButtons_2)
        self.rightButtons.setSpacing(5)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setContentsMargins(9, 0, 8, 0)
        self.radioButton = QRadioButton(self.rightButtons_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"        color: white;\n"
"        background-color: #3A3F44;\n"
"        border: 1px solid #5A5A5A;\n"
"        border-radius: 6px;\n"
"        padding: 5px 10px;\n"
"    }\n"
"    QRadioButton::indicator {\n"
"        width: 16px;\n"
"        height: 16px;\n"
"    }\n"
"    QRadioButton::indicator:checked {\n"
"        background-color: #00C853;\n"
"        border-radius: 8px;\n"
"    }\n"
"    QRadioButton::indicator:unchecked {\n"
"        background-color: #e12807;\n"
"        border-radius: 8px;\n"
"        border: 1px solid gray;\n"
"    }")

        self.rightButtons.addWidget(self.radioButton)


        self.horizontalLayout_2.addWidget(self.rightButtons_2)


        self.verticalLayout.addWidget(self.contentTopBg)

        self.pagesContainer = QFrame(self.contentBox)
        self.pagesContainer.setObjectName(u"pagesContainer")
        sizePolicy.setHeightForWidth(self.pagesContainer.sizePolicy().hasHeightForWidth())
        self.pagesContainer.setSizePolicy(sizePolicy)
        self.pagesContainer.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MenuPrincipal = QStackedWidget(self.pagesContainer)
        self.MenuPrincipal.setObjectName(u"MenuPrincipal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MenuPrincipal.sizePolicy().hasHeightForWidth())
        self.MenuPrincipal.setSizePolicy(sizePolicy3)
        self.MenuPrincipal.setMaximumSize(QSize(16777215, 16777215))
        self.MenuPrincipal.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.MenuPrincipal.setFrameShape(QFrame.Shape.NoFrame)
        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.Home_page.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.Home_page.setAutoFillBackground(False)
        self.Home_page.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.Home_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.Home_frame = QFrame(self.Home_page)
        self.Home_frame.setObjectName(u"Home_frame")
        self.Home_frame.setAutoFillBackground(False)
        self.Home_frame.setStyleSheet(u"")
        self.Home_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Home_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.Home_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_home = QVBoxLayout()
        self.verticalLayout_home.setObjectName(u"verticalLayout_home")

        self.verticalLayout_23.addLayout(self.verticalLayout_home)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.btn_Start = QPushButton(self.Home_frame)
        self.btn_Start.setObjectName(u"btn_Start")
        self.btn_Start.setStyleSheet(u"QPushButton{\n"
"color: rgba(234, 234, 234,180);\n"
"/*background-color: rgba(255, 196, 0,150);*/\n"
"background-color: rgba(225, 40, 7, 150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(225, 40, 7);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color:#e12807;\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_Start)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_23.addLayout(self.horizontalLayout_7)

        self.lbl_infoCurrentUser = QLabel(self.Home_frame)
        self.lbl_infoCurrentUser.setObjectName(u"lbl_infoCurrentUser")

        self.verticalLayout_23.addWidget(self.lbl_infoCurrentUser)


        self.verticalLayout_20.addWidget(self.Home_frame)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.MenuPrincipal.addWidget(self.Home_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_5.addWidget(self.widget)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.MenuPrincipal.addWidget(self.page)

        self.horizontalLayout_3.addWidget(self.MenuPrincipal)

        self.extraRightBox = QFrame(self.pagesContainer)
        self.extraRightBox.setObjectName(u"extraRightBox")
        sizePolicy.setHeightForWidth(self.extraRightBox.sizePolicy().hasHeightForWidth())
        self.extraRightBox.setSizePolicy(sizePolicy)
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        sizePolicy3.setHeightForWidth(self.themeSettingsTopDetail.sizePolicy().hasHeightForWidth())
        self.themeSettingsTopDetail.setSizePolicy(sizePolicy3)
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        sizePolicy.setHeightForWidth(self.contentSettings.sizePolicy().hasHeightForWidth())
        self.contentSettings.setSizePolicy(sizePolicy)
        self.contentSettings.setMinimumSize(QSize(0, 0))
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        sizePolicy.setHeightForWidth(self.topMenus.sizePolicy().hasHeightForWidth())
        self.topMenus.setSizePolicy(sizePolicy)
        self.topMenus.setMinimumSize(QSize(0, 0))
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        self.btn_message.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy4)
        self.btn_message.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_message.setFont(font2)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy4)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font2)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy4.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy4)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font2)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_4.addWidget(self.contentSettings)


        self.horizontalLayout_3.addWidget(self.extraRightBox)


        self.verticalLayout.addWidget(self.pagesContainer)


        self.horizontalLayout.addWidget(self.contentBox)


        self.verticalLayout_2.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.MenuPrincipal.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Rugosidad", None))
        self.label_4.setText("")
        self.titleLeftApp_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#e12807;\">GRAFICO</span></p></body></html>", None))
        self.toggleButton.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.btn_printer.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.btn_Report.setText(QCoreApplication.translate("MainWindow", u"Borrar Grafica", None))
        self.btn_Master.setText(QCoreApplication.translate("MainWindow", u"Guardar Datos", None))
        self.btn_DataMatrix.setText(QCoreApplication.translate("MainWindow", u"Cargar y Graficar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">DISPOSITIVO:</p></body></html>", None))
        self.lb_statePortCom.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#00aa00;\">CONECTADO</span></p></body></html>", None))
        self.btn_configData.setText(QCoreApplication.translate("MainWindow", u"Limpiar Grafica", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"COM:", None))
        self.CutOff.setText(QCoreApplication.translate("MainWindow", u"CutOff: ", None))
        self.comboBox_cutOff.setItemText(0, QCoreApplication.translate("MainWindow", u"0.25", None))
        self.comboBox_cutOff.setItemText(1, QCoreApplication.translate("MainWindow", u"2.5", None))
        self.comboBox_cutOff.setItemText(2, QCoreApplication.translate("MainWindow", u"0.08", None))
        self.comboBox_cutOff.setItemText(3, QCoreApplication.translate("MainWindow", u"0.8", None))

        self.lbl_secciones.setText(QCoreApplication.translate("MainWindow", u"Cuadros:", None))
        self.comboBox_Secciones.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_Secciones.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_Secciones.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_Secciones.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_Secciones.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Conexion:", None))
        self.radioButton.setText("")
        self.btn_Start.setText(QCoreApplication.translate("MainWindow", u"COMENZAR", None))
        self.lbl_infoCurrentUser.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:rgba(255,255,255,100);\">Iniciar sesion para comenzar la verificacion de Modulo</span></p></body></html>", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

