# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AtlasInterfaz.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 640)
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
        self.leftMenuBg.setMinimumSize(QSize(185, 0))
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
        self.titleLeftApp.setGeometry(QRect(60, 10, 71, 35))
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
        self.titleLeftApp_2.setGeometry(QRect(61, -3, 81, 21))
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
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.leftMenuFrame.addWidget(self.btn_home)

        self.btn_Report = QPushButton(self.leftMenuFramee)
        self.btn_Report.setObjectName(u"btn_Report")
        self.btn_Report.setMinimumSize(QSize(0, 45))
        self.btn_Report.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

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

        self.btn_printer = QPushButton(self.leftMenuFramee)
        self.btn_printer.setObjectName(u"btn_printer")
        self.btn_printer.setMinimumSize(QSize(45, 45))
        self.btn_printer.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.leftMenuFrame.addWidget(self.btn_printer)

        self.espaciador_settings = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.leftMenuFrame.addItem(self.espaciador_settings)

        self.btn_configData = QPushButton(self.leftMenuFramee)
        self.btn_configData.setObjectName(u"btn_configData")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_configData.sizePolicy().hasHeightForWidth())
        self.btn_configData.setSizePolicy(sizePolicy2)
        self.btn_configData.setMinimumSize(QSize(0, 45))
        self.btn_configData.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")
        self.btn_configData.setCheckable(True)

        self.leftMenuFrame.addWidget(self.btn_configData)


        self.verticalLayout_3.addWidget(self.leftMenuFramee)


        self.horizontalLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        sizePolicy.setHeightForWidth(self.extraLeftBox.sizePolicy().hasHeightForWidth())
        self.extraLeftBox.setSizePolicy(sizePolicy)
        self.extraLeftBox.setMinimumSize(QSize(240, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.extraLeftBox)
        self.verticalLayout_6.setSpacing(1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"background-color: gb(255,196,0);")
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.extraLabel.setStyleSheet(u"background-color: none\n"
"")
        self.extraLabel.setFrameShape(QFrame.Shape.NoFrame)

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.verticalLayout_6.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.extraContent.sizePolicy().hasHeightForWidth())
        self.extraContent.setSizePolicy(sizePolicy3)
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        sizePolicy3.setHeightForWidth(self.extraTopMenu.sizePolicy().hasHeightForWidth())
        self.extraTopMenu.setSizePolicy(sizePolicy3)
        self.extraTopMenu.setMinimumSize(QSize(0, 0))
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.verticalLayout_6.addWidget(self.extraContent)


        self.horizontalLayout.addWidget(self.extraLeftBox)

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
        self.user = QLabel(self.contentTopBg)
        self.user.setObjectName(u"user")

        self.horizontalLayout_2.addWidget(self.user)

        self.lbl_Nparte = QLabel(self.contentTopBg)
        self.lbl_Nparte.setObjectName(u"lbl_Nparte")
        self.lbl_Nparte.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\"; color: #e12807;")

        self.horizontalLayout_2.addWidget(self.lbl_Nparte)

        self.espaciador_user = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.espaciador_user)

        self.model = QLabel(self.contentTopBg)
        self.model.setObjectName(u"model")

        self.horizontalLayout_2.addWidget(self.model)

        self.lbl_nPiezas = QLabel(self.contentTopBg)
        self.lbl_nPiezas.setObjectName(u"lbl_nPiezas")
        self.lbl_nPiezas.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\"; color: #e12807;")

        self.horizontalLayout_2.addWidget(self.lbl_nPiezas)

        self.espaciador_model = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.espaciador_model)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.mSerial = QLabel(self.contentTopBg)
        self.mSerial.setObjectName(u"mSerial")

        self.horizontalLayout_10.addWidget(self.mSerial)

        self.lbl_Serial1 = QLabel(self.contentTopBg)
        self.lbl_Serial1.setObjectName(u"lbl_Serial1")

        self.horizontalLayout_10.addWidget(self.lbl_Serial1)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_20)

        self.label_5 = QLabel(self.contentTopBg)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(35, 16777215))
        self.label_5.setStyleSheet(u"font:16pt \"Segoe UI Semibold\"; \n"
"")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.lbl_OT = QLabel(self.contentTopBg)
        self.lbl_OT.setObjectName(u"lbl_OT")
        self.lbl_OT.setStyleSheet(u"font: 16pt \"Segoe UI Semibold\"; color: #e12807;")

        self.horizontalLayout_12.addWidget(self.lbl_OT)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_12)

        self.rightButtons_2 = QFrame(self.contentTopBg)
        self.rightButtons_2.setObjectName(u"rightButtons_2")
        self.rightButtons = QHBoxLayout(self.rightButtons_2)
        self.rightButtons.setSpacing(5)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setContentsMargins(9, 0, 8, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rightButtons.addItem(self.horizontalSpacer_8)

        self.minimizeAppBtn = QPushButton(self.rightButtons_2)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(30, 30))
        self.minimizeAppBtn.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)

        self.rightButtons.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons_2)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(30, 30))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)

        self.rightButtons.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons_2)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(30, 30))
        self.closeAppBtn.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)

        self.rightButtons.addWidget(self.closeAppBtn)


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
        self.Model_page = QWidget()
        self.Model_page.setObjectName(u"Model_page")
        self.verticalLayout_8 = QVBoxLayout(self.Model_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.vertical_model = QVBoxLayout()
        self.vertical_model.setObjectName(u"vertical_model")
        self.titulo_modelo = QLabel(self.Model_page)
        self.titulo_modelo.setObjectName(u"titulo_modelo")

        self.vertical_model.addWidget(self.titulo_modelo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vertical_model.addItem(self.verticalSpacer)

        self.horizontal_model = QHBoxLayout()
        self.horizontal_model.setObjectName(u"horizontal_model")
        self.btn_EditAction = QPushButton(self.Model_page)
        self.btn_EditAction.setObjectName(u"btn_EditAction")
        sizePolicy.setHeightForWidth(self.btn_EditAction.sizePolicy().hasHeightForWidth())
        self.btn_EditAction.setSizePolicy(sizePolicy)
        self.btn_EditAction.setMinimumSize(QSize(0, 100))
        self.btn_EditAction.setMaximumSize(QSize(250, 16777215))
        self.btn_EditAction.setStyleSheet(u"QPushButton{\n"
"/*background-color: rgba(255, 196, 0,150);*/\n"
"background-color: rgba(225, 40, 7,150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(225, 40, 7);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(225, 40, 7);\n"
"}")
        self.btn_EditAction.setIconSize(QSize(25, 25))

        self.horizontal_model.addWidget(self.btn_EditAction)

        self.btn_PrintAction = QPushButton(self.Model_page)
        self.btn_PrintAction.setObjectName(u"btn_PrintAction")
        sizePolicy.setHeightForWidth(self.btn_PrintAction.sizePolicy().hasHeightForWidth())
        self.btn_PrintAction.setSizePolicy(sizePolicy)
        self.btn_PrintAction.setMinimumSize(QSize(0, 100))
        self.btn_PrintAction.setMaximumSize(QSize(250, 16777215))
        self.btn_PrintAction.setSizeIncrement(QSize(20, 25))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(36)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_PrintAction.setFont(font2)
        self.btn_PrintAction.setStyleSheet(u"QPushButton{\n"
"/*background-color: rgba(255, 196, 0,150);*/\n"
"background-color: rgba(225, 40, 7,150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(225, 40, 7);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(225, 40, 7);\n"
"}")

        self.horizontal_model.addWidget(self.btn_PrintAction)

        self.btn_deleteRegister = QPushButton(self.Model_page)
        self.btn_deleteRegister.setObjectName(u"btn_deleteRegister")
        sizePolicy.setHeightForWidth(self.btn_deleteRegister.sizePolicy().hasHeightForWidth())
        self.btn_deleteRegister.setSizePolicy(sizePolicy)
        self.btn_deleteRegister.setMinimumSize(QSize(0, 100))
        self.btn_deleteRegister.setMaximumSize(QSize(250, 16777215))
        self.btn_deleteRegister.setStyleSheet(u"QPushButton{\n"
"/*background-color: rgba(255, 196, 0,150);*/\n"
"background-color: rgba(225, 40, 7,150);\n"
"font: 700 36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(225, 40, 7);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(225, 40, 7);\n"
"}")

        self.horizontal_model.addWidget(self.btn_deleteRegister)


        self.vertical_model.addLayout(self.horizontal_model)


        self.verticalLayout_8.addLayout(self.vertical_model)

        self.spacer_model = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.spacer_model)

        self.MenuPrincipal.addWidget(self.Model_page)
        self.CheckList_page = QWidget()
        self.CheckList_page.setObjectName(u"CheckList_page")
        sizePolicy.setHeightForWidth(self.CheckList_page.sizePolicy().hasHeightForWidth())
        self.CheckList_page.setSizePolicy(sizePolicy)
        self.CheckList_page.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.CheckList_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.MenuModel_CK = QStackedWidget(self.CheckList_page)
        self.MenuModel_CK.setObjectName(u"MenuModel_CK")
        sizePolicy.setHeightForWidth(self.MenuModel_CK.sizePolicy().hasHeightForWidth())
        self.MenuModel_CK.setSizePolicy(sizePolicy)
        self.MenuModel_CK.setMinimumSize(QSize(0, 0))
        self.MenuModel_CK.setMaximumSize(QSize(1350, 16777215))
        self.MenuModel_CK.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setMinimumSize(QSize(0, 50))
        self.page.setMaximumSize(QSize(1100, 550))
        self.verticalLayout_16 = QVBoxLayout(self.page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.MenuModel_CK.addWidget(self.page)

        self.verticalLayout_7.addWidget(self.MenuModel_CK)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.ControlSlider = QFrame(self.CheckList_page)
        self.ControlSlider.setObjectName(u"ControlSlider")
        sizePolicy.setHeightForWidth(self.ControlSlider.sizePolicy().hasHeightForWidth())
        self.ControlSlider.setSizePolicy(sizePolicy)
        self.ControlSlider.setMinimumSize(QSize(0, 0))
        self.ControlSlider.setMaximumSize(QSize(1350, 100))
        self.ControlSli = QHBoxLayout(self.ControlSlider)
        self.ControlSli.setObjectName(u"ControlSli")
        self.btn_backSlide = QPushButton(self.ControlSlider)
        self.btn_backSlide.setObjectName(u"btn_backSlide")
        sizePolicy3.setHeightForWidth(self.btn_backSlide.sizePolicy().hasHeightForWidth())
        self.btn_backSlide.setSizePolicy(sizePolicy3)
        self.btn_backSlide.setMinimumSize(QSize(0, 0))
        self.btn_backSlide.setMaximumSize(QSize(150, 16777215))
        self.btn_backSlide.setStyleSheet(u"QPushButton{background-color: rgba(207, 162, 9,150);\n"
"font:36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(207, 162, 9);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 233, 51 );\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/images/2x/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backSlide.setIcon(icon3)
        self.btn_backSlide.setIconSize(QSize(80, 80))
        self.btn_backSlide.setAutoRepeat(False)
        self.btn_backSlide.setAutoRepeatDelay(1000)
        self.btn_backSlide.setAutoRepeatInterval(1000)

        self.ControlSli.addWidget(self.btn_backSlide)

        self.progressBar = QProgressBar(self.ControlSlider)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setMinimumSize(QSize(0, 50))
        self.progressBar.setMaximumSize(QSize(16777215, 50))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u" QProgressBar {\n"
"                color: #ffffff;\n"
"                background-color: #3e3e3e; /* Cambia al color de fondo que desees */\n"
"                border: 1px solid #1c1c1c; /* Borde del ProgressBar */\n"
"				 font-size: 20px; /* Cambia el tama\u00f1o de la letra */\n"
"				 text-align: center; /* Centrar el texto */\n"
"            }\n"
"\n"
"            QProgressBar::chunk {\n"
"                background-color:rgba(0, 85, 127, 235); /*#ffc400; /* Cambia al color de la barra de progreso */\n"
"                border-radius: 8px; /* Bordes redondeados de la barra de progreso */\n"
"                text-align: center; /* Centrar el texto */\n"
"            }\n"
"\n"
"")
        self.progressBar.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.progressBar.setValue(85)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setInvertedAppearance(False)

        self.ControlSli.addWidget(self.progressBar)

        self.btn_nextSlide = QPushButton(self.ControlSlider)
        self.btn_nextSlide.setObjectName(u"btn_nextSlide")
        sizePolicy3.setHeightForWidth(self.btn_nextSlide.sizePolicy().hasHeightForWidth())
        self.btn_nextSlide.setSizePolicy(sizePolicy3)
        self.btn_nextSlide.setMinimumSize(QSize(0, 0))
        self.btn_nextSlide.setMaximumSize(QSize(150, 16777215))
        self.btn_nextSlide.setStyleSheet(u"QPushButton{background-color: rgba(207, 162, 9,150);\n"
"font:36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(207, 162, 9);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 233, 51 );\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/images/2x/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nextSlide.setIcon(icon4)
        self.btn_nextSlide.setIconSize(QSize(80, 80))
        self.btn_nextSlide.setAutoRepeat(False)
        self.btn_nextSlide.setAutoRepeatDelay(1000)
        self.btn_nextSlide.setAutoRepeatInterval(1000)

        self.ControlSli.addWidget(self.btn_nextSlide)

        self.btn_screenShoot = QPushButton(self.ControlSlider)
        self.btn_screenShoot.setObjectName(u"btn_screenShoot")
        sizePolicy3.setHeightForWidth(self.btn_screenShoot.sizePolicy().hasHeightForWidth())
        self.btn_screenShoot.setSizePolicy(sizePolicy3)
        self.btn_screenShoot.setMinimumSize(QSize(0, 0))
        self.btn_screenShoot.setMaximumSize(QSize(150, 16777215))
        self.btn_screenShoot.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font:36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/images/2x/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_screenShoot.setIcon(icon5)
        self.btn_screenShoot.setIconSize(QSize(80, 80))
        self.btn_screenShoot.setAutoRepeatDelay(1000)

        self.ControlSli.addWidget(self.btn_screenShoot)

        self.btn_saveModule = QPushButton(self.ControlSlider)
        self.btn_saveModule.setObjectName(u"btn_saveModule")
        sizePolicy3.setHeightForWidth(self.btn_saveModule.sizePolicy().hasHeightForWidth())
        self.btn_saveModule.setSizePolicy(sizePolicy3)
        self.btn_saveModule.setMinimumSize(QSize(0, 0))
        self.btn_saveModule.setMaximumSize(QSize(150, 16777215))
        self.btn_saveModule.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font:36pt \"Segoe UI\";\n"
"border-radius: 10px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/images/2x/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_saveModule.setIcon(icon6)
        self.btn_saveModule.setIconSize(QSize(80, 80))

        self.ControlSli.addWidget(self.btn_saveModule)


        self.verticalLayout_9.addWidget(self.ControlSlider)

        self.MenuPrincipal.addWidget(self.CheckList_page)
        self.Login_page = QWidget()
        self.Login_page.setObjectName(u"Login_page")
        sizePolicy3.setHeightForWidth(self.Login_page.sizePolicy().hasHeightForWidth())
        self.Login_page.setSizePolicy(sizePolicy3)
        self.Login_page.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.Login_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_7 = QLabel(self.Login_page)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_35.addWidget(self.label_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_3)

        self.laabel = QLabel(self.Login_page)
        self.laabel.setObjectName(u"laabel")

        self.verticalLayout_15.addWidget(self.laabel)

        self.initBox_PartNo = QComboBox(self.Login_page)
        self.initBox_PartNo.setObjectName(u"initBox_PartNo")
        self.initBox_PartNo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")

        self.verticalLayout_15.addWidget(self.initBox_PartNo)

        self.label_14 = QLabel(self.Login_page)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_15.addWidget(self.label_14)

        self.initBox_Cantidad = QComboBox(self.Login_page)
        self.initBox_Cantidad.setObjectName(u"initBox_Cantidad")
        self.initBox_Cantidad.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")

        self.verticalLayout_15.addWidget(self.initBox_Cantidad)

        self.label_16 = QLabel(self.Login_page)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_15.addWidget(self.label_16)

        self.initTxt_OT = QTextEdit(self.Login_page)
        self.initTxt_OT.setObjectName(u"initTxt_OT")
        self.initTxt_OT.setMaximumSize(QSize(16777215, 26))
        self.initTxt_OT.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")
        self.initTxt_OT.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_15.addWidget(self.initTxt_OT)

        self.label_15 = QLabel(self.Login_page)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_15.addWidget(self.label_15)

        self.initBox_Proveedor = QComboBox(self.Login_page)
        self.initBox_Proveedor.setObjectName(u"initBox_Proveedor")
        self.initBox_Proveedor.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: rgb(44, 49, 58);")

        self.verticalLayout_15.addWidget(self.initBox_Proveedor)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_initSave = QPushButton(self.Login_page)
        self.btn_initSave.setObjectName(u"btn_initSave")
        self.btn_initSave.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font:18pt \"Segoe UI\";\n"
"border-radius: 4px;\n"
"border: 2px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.btn_initSave)

        self.btn_initCancel = QPushButton(self.Login_page)
        self.btn_initCancel.setObjectName(u"btn_initCancel")
        self.btn_initCancel.setStyleSheet(u"QPushButton{\n"
"/*background-color: rgba(207, 162, 9,150);*/\n"
"background-color: rgba(225, 40, 7, 150);\n"
"font:18pt \"Segoe UI\";\n"
"border-radius: 4px;\n"
"border: 2px solid black;\n"
"border-color: rgb(225, 40, 7);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(225, 40, 7);\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_initCancel)


        self.verticalLayout_15.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout_35.addLayout(self.horizontalLayout_4)


        self.verticalLayout_17.addLayout(self.verticalLayout_35)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_3)

        self.MenuPrincipal.addWidget(self.Login_page)
        self.DataBase_page = QWidget()
        self.DataBase_page.setObjectName(u"DataBase_page")
        self.verticalLayout_19 = QVBoxLayout(self.DataBase_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(50, 0, 50, 50)
        self.label = QLabel(self.DataBase_page)
        self.label.setObjectName(u"label")

        self.verticalLayout_18.addWidget(self.label)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_18.addItem(self.verticalSpacer_12)

        self.DatabaseWidget = QWidget(self.DataBase_page)
        self.DatabaseWidget.setObjectName(u"DatabaseWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.DatabaseWidget.sizePolicy().hasHeightForWidth())
        self.DatabaseWidget.setSizePolicy(sizePolicy4)
        self.DatabaseWidget.setStyleSheet(u"background-color: rgba(225, 40, 7, 150);")

        self.verticalLayout_18.addWidget(self.DatabaseWidget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btn_printCurrIndex = QPushButton(self.DataBase_page)
        self.btn_printCurrIndex.setObjectName(u"btn_printCurrIndex")
        self.btn_printCurrIndex.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 85, 127, 150);\n"
"font: 700 18pt \"Segoe UI\";\n"
"border-radius: 4px;\n"
"border: 4px solid black;\n"
"border-color: rgb(0, 85, 127);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 85, 127);\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_printCurrIndex)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_18.addLayout(self.horizontalLayout_6)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.MenuPrincipal.addWidget(self.DataBase_page)
        self.Report_Page = QWidget()
        self.Report_Page.setObjectName(u"Report_Page")
        self.verticalLayout_24 = QVBoxLayout(self.Report_Page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_6 = QLabel(self.Report_Page)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)

        self.verticalLayout_22.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.lbl_labelMasterEdit = QLabel(self.Report_Page)
        self.lbl_labelMasterEdit.setObjectName(u"lbl_labelMasterEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lbl_labelMasterEdit.sizePolicy().hasHeightForWidth())
        self.lbl_labelMasterEdit.setSizePolicy(sizePolicy6)
        self.lbl_labelMasterEdit.setMinimumSize(QSize(700, 200))
        self.lbl_labelMasterEdit.setMaximumSize(QSize(700, 500))
        self.lbl_labelMasterEdit.setStyleSheet(u"background-color: rgba(0, 85, 127, 180);")
        self.lbl_labelMasterEdit.setPixmap(QPixmap(u"../Label_Master.PNG"))
        self.lbl_labelMasterEdit.setScaledContents(True)

        self.verticalLayout_34.addWidget(self.lbl_labelMasterEdit)

        self.verticalSpacer_7 = QSpacerItem(20, 175, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_34.addItem(self.verticalSpacer_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_34)

        self.verticalFrame_2 = QFrame(self.Report_Page)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMaximumSize(QSize(200, 1500))
        self.verticalLayout_25 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 40, -1, -1)
        self.label_11 = QLabel(self.verticalFrame_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy5.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy5)

        self.verticalLayout_25.addWidget(self.label_11)

        self.box_serial = QComboBox(self.verticalFrame_2)
        self.box_serial.setObjectName(u"box_serial")
        self.box_serial.setStyleSheet(u"background-color: rgba(161, 161, 161,90);")

        self.verticalLayout_25.addWidget(self.box_serial)

        self.label_8 = QLabel(self.verticalFrame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)

        self.verticalLayout_25.addWidget(self.label_8)

        self.lbl_PartNoprint = QLabel(self.verticalFrame_2)
        self.lbl_PartNoprint.setObjectName(u"lbl_PartNoprint")
        self.lbl_PartNoprint.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.lbl_PartNoprint.setFont(font3)
        self.lbl_PartNoprint.setStyleSheet(u"color: rgb(255, 196, 0);\n"
"background-color: rgba(161, 161, 161,90);")

        self.verticalLayout_25.addWidget(self.lbl_PartNoprint)

        self.label_9 = QLabel(self.verticalFrame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)

        self.verticalLayout_25.addWidget(self.label_9)

        self.lbl_QtyPrint = QLabel(self.verticalFrame_2)
        self.lbl_QtyPrint.setObjectName(u"lbl_QtyPrint")
        self.lbl_QtyPrint.setMinimumSize(QSize(0, 25))
        self.lbl_QtyPrint.setStyleSheet(u"color: rgb(255, 196, 0);\n"
"background-color: rgba(161, 161, 161,90);")

        self.verticalLayout_25.addWidget(self.lbl_QtyPrint)

        self.label_10 = QLabel(self.verticalFrame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy5)

        self.verticalLayout_25.addWidget(self.label_10)

        self.lbl_ProveedorPrint = QLabel(self.verticalFrame_2)
        self.lbl_ProveedorPrint.setObjectName(u"lbl_ProveedorPrint")
        self.lbl_ProveedorPrint.setMinimumSize(QSize(0, 25))
        self.lbl_ProveedorPrint.setStyleSheet(u"color: rgb(255, 196, 0);\n"
"background-color: rgba(161, 161, 161,90);")

        self.verticalLayout_25.addWidget(self.lbl_ProveedorPrint)

        self.label_12 = QLabel(self.verticalFrame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)

        self.verticalLayout_25.addWidget(self.label_12)

        self.lbl_OTPrint = QLabel(self.verticalFrame_2)
        self.lbl_OTPrint.setObjectName(u"lbl_OTPrint")
        self.lbl_OTPrint.setMinimumSize(QSize(0, 25))
        self.lbl_OTPrint.setStyleSheet(u"color: rgb(255, 196, 0);\n"
"background-color: rgba(161, 161, 161,90);")

        self.verticalLayout_25.addWidget(self.lbl_OTPrint)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_9)

        self.btn_saveDataLabel = QPushButton(self.verticalFrame_2)
        self.btn_saveDataLabel.setObjectName(u"btn_saveDataLabel")
        self.btn_saveDataLabel.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_25.addWidget(self.btn_saveDataLabel)

        self.btn_PrintLabel = QPushButton(self.verticalFrame_2)
        self.btn_PrintLabel.setObjectName(u"btn_PrintLabel")
        self.btn_PrintLabel.setStyleSheet(u"QPushButton{background-color: rgba(207, 162, 9,150);\n"
"font:15pt \"Segoe UI\";\n"
"border-radius: 4px;\n"
"border: 4px solid black;\n"
"border-color: rgb(207, 162, 9);}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 233, 51 );\n"
"}")

        self.verticalLayout_25.addWidget(self.btn_PrintLabel)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_5)


        self.horizontalLayout_8.addWidget(self.verticalFrame_2)


        self.verticalLayout_22.addLayout(self.horizontalLayout_8)


        self.verticalLayout_24.addLayout(self.verticalLayout_22)

        self.MenuPrincipal.addWidget(self.Report_Page)
        self.Black_page = QWidget()
        self.Black_page.setObjectName(u"Black_page")
        self.gridLayout = QGridLayout(self.Black_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.Black_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.widget_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_CodigoActual = QLabel(self.widget_2)
        self.label_CodigoActual.setObjectName(u"label_CodigoActual")

        self.verticalLayout_29.addWidget(self.label_CodigoActual)

        self.txt_input = QTextEdit(self.widget_2)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setMaximumSize(QSize(16777204, 33))
        self.txt_input.setStyleSheet(u"background-color: rgba(113, 127, 147, 150);\n"
" font-size:18pt; \n"
"font-weight:700;\n"
"color:#e12807;\n"
"border-radius:7px;")
        self.txt_input.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.txt_input.setUndoRedoEnabled(True)

        self.verticalLayout_29.addWidget(self.txt_input)

        self.lbl_StateLabel = QLabel(self.widget_2)
        self.lbl_StateLabel.setObjectName(u"lbl_StateLabel")
        self.lbl_StateLabel.setStyleSheet(u"QLabel {\n"
"    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(0, 255, 0);\n"
"	border-radius:15px;\n"
"}")

        self.verticalLayout_29.addWidget(self.lbl_StateLabel)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_13)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)


        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.Black_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.verticalLayout_31 = QVBoxLayout(self.widget_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_ServerState = QLabel(self.widget_3)
        self.lbl_ServerState.setObjectName(u"lbl_ServerState")
        self.lbl_ServerState.setStyleSheet(u"QLabel {\n"
"    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(0, 85, 255);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.lbl_ServerState)

        self.lbl_PrinterState = QLabel(self.widget_3)
        self.lbl_PrinterState.setObjectName(u"lbl_PrinterState")
        self.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
"    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(0, 85, 255);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.lbl_PrinterState)

        self.lbl_wifiState = QLabel(self.widget_3)
        self.lbl_wifiState.setObjectName(u"lbl_wifiState")
        self.lbl_wifiState.setStyleSheet(u"QLabel {\n"
"    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(0, 85, 255);\n"
"	border-radius:5px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.lbl_wifiState)


        self.verticalLayout_31.addLayout(self.horizontalLayout_9)


        self.gridLayout.addWidget(self.widget_3, 2, 0, 1, 1)

        self.widget = QWidget(self.Black_page)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_27 = QVBoxLayout(self.widget)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_PzsRealizadas = QLabel(self.widget)
        self.label_PzsRealizadas.setObjectName(u"label_PzsRealizadas")

        self.verticalLayout_26.addWidget(self.label_PzsRealizadas)

        self.lcdNumber_Realizado = QLCDNumber(self.widget)
        self.lcdNumber_Realizado.setObjectName(u"lcdNumber_Realizado")

        self.verticalLayout_26.addWidget(self.lcdNumber_Realizado)

        self.label_PzsFaltantes = QLabel(self.widget)
        self.label_PzsFaltantes.setObjectName(u"label_PzsFaltantes")

        self.verticalLayout_26.addWidget(self.label_PzsFaltantes)

        self.lcdNumber_Faltantes = QLCDNumber(self.widget)
        self.lcdNumber_Faltantes.setObjectName(u"lcdNumber_Faltantes")

        self.verticalLayout_26.addWidget(self.lcdNumber_Faltantes)


        self.verticalLayout_27.addLayout(self.verticalLayout_26)


        self.gridLayout.addWidget(self.widget, 0, 1, 2, 1)

        self.MenuPrincipal.addWidget(self.Black_page)
        self.Datamatrix_Page = QWidget()
        self.Datamatrix_Page.setObjectName(u"Datamatrix_Page")
        self.verticalLayout_33 = QVBoxLayout(self.Datamatrix_Page)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_2 = QLabel(self.Datamatrix_Page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_32.addWidget(self.label_2)

        self.label_3 = QLabel(self.Datamatrix_Page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        self.label_3.setMaximumSize(QSize(1000, 500))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    border: 3px solid #FF0000; /* Cambia el color del borde a rojo */\n"
"	border-color: rgb(255, 196, 0);\n"
"	border-color: rgb(255, 0, 0);\n"
"	border-radius:1px;\n"
"}")
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setPixmap(QPixmap(u":/images/images/Label_Spec.PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setMargin(5)

        self.verticalLayout_32.addWidget(self.label_3)


        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_8)

        self.MenuPrincipal.addWidget(self.Datamatrix_Page)

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
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy7)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font3)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy7)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font3)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy7.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy7)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font3)
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
        self.MenuModel_CK.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Atlas", None))
        self.label_4.setText("")
        self.titleLeftApp_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700; color:#e12807;\">RADIADOR</span></p></body></html>", None))
        self.toggleButton.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btn_Report.setText(QCoreApplication.translate("MainWindow", u"Historial Piezas", None))
        self.btn_Master.setText(QCoreApplication.translate("MainWindow", u"Historial Master", None))
        self.btn_DataMatrix.setText(QCoreApplication.translate("MainWindow", u"DataMatrix", None))
        self.btn_printer.setText(QCoreApplication.translate("MainWindow", u"Imprimir ", None))
        self.btn_configData.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">INFORMACION</span></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">RADIADOR ATLAS</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#e12807;\">HISTORIAL PIEZAS</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-b"
                        "ottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#9c9c9c;\">En la pesta\u00f1a de Historial de Piezas<br />podra encontrar el resumen de los ultimos 30 modulos guardados en este dispositivo.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#e12807;\">HISTORIAL MASTER</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#9c9c9c;\">En la pesta\u00f1a de Historial Master<br />podra encontrar el resumen de los ultimos 30 Contenedores creados.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-t"
                        "op:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#e12807;\">DATA MATRIX</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#9c9c9c;\">En la pesta\u00f1a de DataMatrix<br />podra encontrar una representacion detallada de los elementos a evaluar de la etiqueta para este radiador.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; color:#9c9c9c;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                        "0px;\"><span style=\" font-size:12pt; font-weight:700; color:#e12807;\">By: Geovanni Ortiz</span></p></body></html>", None))
        self.user.setText(QCoreApplication.translate("MainWindow", u"N.Parte:", None))
        self.lbl_Nparte.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>3QF 121 251 E</p></body></html>", None))
        self.model.setText(QCoreApplication.translate("MainWindow", u"N.Piezas:", None))
        self.lbl_nPiezas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#e12807;\">10</span></p></body></html>", None))
        self.mSerial.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>N.Serie:</p></body></html>", None))
        self.lbl_Serial1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#e12807;\">1802120524155855</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"OT:", None))
        self.lbl_OT.setText(QCoreApplication.translate("MainWindow", u"192589", None))
        self.minimizeAppBtn.setText("")
        self.maximizeRestoreAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.btn_Start.setText(QCoreApplication.translate("MainWindow", u"COMENZAR", None))
        self.lbl_infoCurrentUser.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:rgba(255,255,255,100);\">Iniciar sesion para comenzar la verificacion de Modulo</span></p></body></html>", None))
        self.titulo_modelo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#e12807;\">Seleccionar Accion</span></p></body></html>", None))
        self.btn_EditAction.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.btn_PrintAction.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
        self.btn_deleteRegister.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.btn_backSlide.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.btn_nextSlide.setText("")
        self.btn_screenShoot.setText("")
        self.btn_saveModule.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#e12807;\">ACTUALIZAR DATOS</span></p></body></html>", None))
        self.laabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Numero de Parte:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Cantidad:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Orden de Trabajo:</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Proveedor:</span></p></body></html>", None))
        self.btn_initSave.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btn_initCancel.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#e12807;\">Historial Modelo Actual</span></p></body></html>", None))
        self.btn_printCurrIndex.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700; color:#e12807;\">GENERAR ETIQUETA</span></p></body></html>", None))
        self.lbl_labelMasterEdit.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Serial:</span></p></body></html>", None))
        self.box_serial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Numero de Parte:</span></p></body></html>", None))
        self.lbl_PartNoprint.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Cantidad:</span></p></body></html>", None))
        self.lbl_QtyPrint.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Proveedor:</span></p></body></html>", None))
        self.lbl_ProveedorPrint.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Orden de Trabajo:</span></p></body></html>", None))
        self.lbl_OTPrint.setText("")
        self.btn_saveDataLabel.setText(QCoreApplication.translate("MainWindow", u"GUARDAR", None))
        self.btn_PrintLabel.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR", None))
        self.label_CodigoActual.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Codigo Actual:</span></p></body></html>", None))
        self.lbl_StateLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00ff00;\">PIEZA APROBADA</span></p></body></html>", None))
        self.lbl_ServerState.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">SERVIDOR:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CONECTADO</span></p></body></html>", None))
        self.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CONECTADA</span></p></body></html>", None))
        self.lbl_wifiState.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">WIFI: <br/></span><span style=\" font-size:16pt; font-weight:700; color:#00aa00;\">CONECTADO</span></p></body></html>", None))
        self.label_PzsRealizadas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#e12807;\">Piezas Realizadas:</span></p></body></html>", None))
        self.label_PzsFaltantes.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#e12807;\">Piezas Faltantes:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:700; color:#e12807;\">Data Matrix</span></p></body></html>", None))
        self.label_3.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

