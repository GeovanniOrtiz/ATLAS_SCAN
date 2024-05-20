import time
from datetime import datetime
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidget, QVBoxLayout, QHeaderView, QDialog, QMessageBox, \
    QTextEdit, QLineEdit

from Interfaz.AtlasInterfaz_gui import Ui_MainWindow as Interfaz
from Alerts import *
from Printer import *
from SQL import managerDataBase

from Interfaz.Dialogo_ConfirmData_gui import Ui_Dialog as ConfirmData
from Interfaz.Loggin_gui import Ui_Dialog as Loggin
from Printer import ConsultStatePrint, PrinterState

dataBase = managerDataBase()
class ConfirmData(QDialog, ConfirmData):
    def __init__(self, parent=None):
        super(ConfirmData, self).__init__(parent)
        self.setupUi(self)
        self.state=False

        # Elimina la barra de menú y el botón de cierre
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.btn_Accept.released.connect(lambda:self.GetState(True))
        self.btn_Reject.released.connect(lambda:self.GetState(False))
    def SetData(self, partNo, Qty, Supplier, Serial, Ot):
        self.lbl_PartNo.setText(QCoreApplication.translate("Dialog",
                                                           f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{partNo}</span></p></body></html>",
                                                           None))
        self.lbl_Cantidad.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Qty}</span></p></body></html>", None))
        self.lbl_Proveedor.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Supplier}</span></p></body></html>", None))
        self.lbl_Serial.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Serial}</span></p></body></html>", None))
        self.lbl_OT.setText(QCoreApplication.translate("Dialog", f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{Ot}</span></p></body></html>", None))

    def GetState(self, respuesta):
        result = respuesta
        if result == True:
            self.accept()
            self.state=True
        else:
            self.reject()
            self.state=False
class Loggin(QDialog, Loggin):
    def __init__(self, parent=None):
        super(Loggin, self).__init__(parent)
        self.setupUi(self)
        self.line_contra.setEchoMode(QLineEdit.Password)

        self.state=False

        # Elimina la barra de menú y el botón de cierre
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.box_Admin.addItems(["Administrador", "Usuario"])
        self.btn_iniciarSesion.released.connect(self.tryInit)
        self.btn_cancelar.released.connect(self.Cancel)

    def tryInit(self):
        if len(self.box_Admin.currentText())>0 and len(self.txt_User.toPlainText())>0 and len(self.line_contra.text())>0:
            print("Get data")
            username = self.txt_User.toPlainText()
            password = self.line_contra.text()

            # Aquí puedes realizar la validación del usuario y contraseña
            if username == "Atlas2024" and password == "0300":
                # Ejemplo simple de validación: solo imprimir los valores ingresados
                print(f"Usuario: {username}, Contraseña: {password}")
                # Cerrar el cuadro de diálogo después de iniciar sesión
                self.state=True
                self.accept()
                QMessageBox.information(None, "Bienvenido", "Administrador registrado con exito")

            else:
                QMessageBox.information(None, "Verificar Informacion", "Usuario o Contraseña Incorrectos")


        else:
            QMessageBox.information(None, "Verificar Informacion", "Usuario o Contraseña Incorrectos")

    def Cancel(self):
        self.state=False
        self.reject()

class Atlas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Interfaz()
        self.ui_main.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.showFullScreen()
        self.InitSlots()
        self.InitAnimations()
        self.initGui()
        #SendTemplate()


    def InitAnimations(self):
        # Configuración de la animación menu principal
        self.ui_main.animation = QPropertyAnimation(self.ui_main.leftMenuBg, b'minimumWidth')
        self.ui_main.animation.setDuration(500)
        self.ui_main.animation.setEasingCurve(QEasingCurve.OutQuint)  # Cambia la curva de aceleración aquí

        # Configuración de la animación menu secundario
        self.ui_main.animation_secundario = QPropertyAnimation(self.ui_main.extraLeftBox, b'minimumWidth')
        self.ui_main.animation_secundario.setDuration(500)
        self.ui_main.animation_secundario.setEasingCurve(QEasingCurve.OutQuint)  # Cambia la curva de aceleración aquí

        self.ui_main.animation_config = QPropertyAnimation(self.ui_main.extraRightBox, b'minimumWidth')
        self.ui_main.animation_config.setDuration(500)
        self.ui_main.animation_config.setEasingCurve(QEasingCurve.OutQuint)  # Cambia la curva de aceleración aquí

        self.ui_main.animation_Sesion = QPropertyAnimation(self.ui_main.Login_page, b'geometry')
        self.ui_main.animation_Sesion.setDuration(500)
        self.ui_main.animation_Sesion.setEasingCurve(QEasingCurve.OutQuint)  # Cambia la curva de aceleración aquí
    def InitSlots(self):
        #self.ui_main.settingsTopBtn.released.connect(self.ConfigMenu_Control)
        #self.ui_main.btn_logout.released.connect(self.CloseMenuControl)
        self.ui_main.closeAppBtn.released.connect(QApplication.instance().quit)
        self.ui_main.minimizeAppBtn.released.connect(self.showMinimized)
        self.ui_main.btn_Report.released.connect(self.HistorialPressed)
        self.ui_main.btn_home.released.connect(self.HomePressed)
        self.ui_main.btn_DataMatrix.released.connect(self.DataMatrixPressed)
        self.ui_main.btn_Master.released.connect(self.HistorialMasterPressed)
        self.ui_main.btn_printer.released.connect(self.PrintPressed)
        self.ui_main.btn_PrintLabel.released.connect(self.GetData)
        self.ui_main.btn_configData.released.connect(self.ShowLoggin)
        self.ui_main.btn_initSave.released.connect(lambda:self.SetCurrentData())
        self.ui_main.btn_initCancel.released.connect(self.CancelChange)
        self.ui_main.btn_EditAction.released.connect(lambda:self.ui_main.MenuPrincipal.setCurrentIndex(3))
        self.ui_main.btn_PrintAction.released.connect(self.PrintPressed)
    def initGui(self):
        #Esconde el label de Alertas de proceso
        HideAlerts(self.ui_main)

        #Crea la instancia de PrinterState
        self.printer_state = PrinterState()

        #Timer para consultar el estado de la impresora
        self.StatePrinter = QTimer()
        self.StatePrinter.timeout.connect(lambda:ConsultStatePrint(self.ui_main, self.printer_state))
        self.StatePrinter.start(1000)

        #timer para correr el proceso de escaneado
        self.TimeProcess = QTimer()
        self.TimeProcess.timeout.connect(self.Run_process)
        self.TimeProcess.start(500)

        #Timer para las alertas vizuales
        self.Alerts = QTimer()

        #Timer para actualizar los label de la impresora
        self.timeLabelPrinter = QTimer()
        self.timeLabelPrinter.timeout.connect(self.UpdateLabelStatus_printer)
        self.timeLabelPrinter.start(500)

        #obtiene el respaldo de los datos
        data = dataBase.GetDataBackUp()

        #Variables que se inicializan con el backup
        self.PartNo = data[1]
        self.Supplier = data[2]
        self.OT = data[3]
        self.PzsTotales = int(data[4])
        self.PzsRealizadas = int(data[5])
        self.SerialNum = data[6]
        self.CreationDate = data[7]

        currDate = datetime.now()
        currDate = currDate.strftime("%d/%m/%Y %H:%M:%S")
        #SendReqPrint(currDate, self.PartNo, self.PzsTotales, self.Supplier, self.SerialNum, self.OT)

        #Calcula las piezas faltantes a escanear
        self.PzsFaltantes = int(self.PzsTotales - self.PzsRealizadas)
        self.PrinterMode = 0
        self.state = 0
        self.CodeRadd = ""
        self.DateLabel = ""
        self.Key=False

        #Actualiza las vistas de  los label de interfaz
        self.ui_main.lbl_Serial1.setText(QCoreApplication.translate("MainWindow", f"{self.SerialNum}", None))
        self.ui_main.lbl_OT.setText(QCoreApplication.translate("MainWindow", f"{self.OT}", None))
        self.ui_main.lbl_nPiezas.setText(QCoreApplication.translate("MainWindow",
                                                                    f"<html><head/><body><p><span style=\" color:#ffc400;\">{self.PzsTotales}</span></p></body></html>",
                                                                    None))
        self.ui_main.lbl_Nparte.setText(
            QCoreApplication.translate("MainWindow", f"<html><head/><body><p>{self.PartNo}</p></body></html>", None))
        self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                         f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\"></span></p></body></html>",
                                                                         None))

        self.ui_main.lbl_labelMasterEdit.setPixmap(QPixmap(u"./Label_Master.PNG"))

        # Creo la tabla para la base de datos
        self.CreateTable()
        self.CreateTableMaster()

        #slot de index de tabla
        self.tableMastertaBase.cellClicked.connect(self.print_selected_row)

        #Actualiza los displays de contenedores
        self.ui_main.lcdNumber_Realizado.display(self.PzsRealizadas)
        self.ui_main.lcdNumber_Faltantes.display(self.PzsFaltantes)

        #Oculta las tablas de Historial
        self.tableMastertaBase.hide()
        self.tableWidgetdataBase.hide()

        #Inicializa en la hoja de home 6
        self.ui_main.MenuPrincipal.setCurrentIndex(6)

        #Esconde el boton de savedata
        self.ui_main.btn_saveDataLabel.hide()

        #Inicializa los combobox de la etiqueta
        #self.ui_main.box_PartNo.addItems(["3QF121251E"])
        #self.ui_main.box_Cantidad.addItems(["5", "6", "7", "8", "9", "10"])
        #self.ui_main.box_proveedor.addItems(["6001003941"])
        self.ui_main.box_serial.addItems(dataBase.GetSerialMaster("atlas_master"))
        #self.ui_main.box_OT.addItems(dataBase.GetOTMaster("atlas_master"))

        #Inivializa los combox de configuracion inicial
        self.ui_main.initBox_PartNo.addItems(["3QF121251E"])
        self.ui_main.initBox_Cantidad.addItems(["5", "6", "7", "8", "9", "10"])
        mData = dataBase.GetDataBackUp()
        PzsTotales = mData[4]
        self.ui_main.initBox_Cantidad.setCurrentText(PzsTotales)
        self.ui_main.initBox_Proveedor.addItems(["6001003941"])
        self.ui_main.initTxt_OT.clear()

        #Esconde el boton de imprimir
        self.ui_main.btn_printCurrIndex.hide()

        #Inicializa el widget con la tabla master
        self.tableMastertaBase.show()
    def UpdateLabelStatus_printer(self):
        mState = self.printer_state.mState
        mText = self.printer_state.mText
        match mState:
            case 0:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FFFFFF; /* Cambia el color del borde a rojo */\n"
                                                       "	border-color: #FFFFFF;\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#7FFF00;\">{mText}</span></p></body></html>",
                                                                            None))
            case 1:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                       "	border-color: rgb(255, 196, 0);\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>",
                                                                            None))
            case 2:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                       "	border-color: rgb(255, 196, 0);\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>",
                                                                            None))
            case 3:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                       "	border-color: rgb(255, 196, 0);\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>",
                                                                            None))
            case 4:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                       "	border-color: rgb(255, 196, 0);\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>",
                                                                            None))
            case 5:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                       "	border-color: #FF0000;\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADA</span></p></body></html>",
                                                                            None))
    def CloseMainMenu(self):
        if self.ui_main.toggleButton.isChecked():
            self.ui_main.toggleButton.setChecked(False)
            self.ui_main.animation.setStartValue(250)
            self.ui_main.animation.setEndValue(84)  # Ajusta el ancho según tus necesidades
            self.ui_main.animation.start()
    def CloseSecondMenu(self):
        if self.ui_main.btn_configData.isChecked():
            self.ui_main.btn_configData.setChecked(False)
            self.ui_main.animation_secundario.setStartValue(250)
            self.ui_main.animation_secundario.setEndValue(0)  # Ajusta el ancho según tus necesidades
            self.ui_main.animation_secundario.start()
    def ConfigMenu_Control(self):
        self.CloseMainMenu()
        self.CloseSecondMenu()

        if self.ui_main.settingsTopBtn.isChecked():
            self.ui_main.animation_config.setStartValue(0)
            self.ui_main.animation_config.setEndValue(147)

        else:
            self.ui_main.animation_config.setStartValue(147)
            self.ui_main.animation_config.setEndValue(0)
        self.ui_main.animation_config.start()
    def CloseMenuControl(self):
        if self.ui_main.settingsTopBtn.isChecked():
            self.ui_main.settingsTopBtn.setChecked(False)
            self.ui_main.animation_config.setStartValue(147)
            self.ui_main.animation_config.setEndValue(0)
            self.ui_main.animation_config.start()
    def Run_process(self):
        if self.ui_main.MenuPrincipal.currentIndex() == 6:
            if self.printer_state.mState ==0:
                match self.state:
                    case 0:  # Read TextEdit
                        self.ui_main.txt_input.setFocus()
                        text = self.ui_main.txt_input.toPlainText()
                        if (len(text) == 33):  # ZAT08052416134613QF121351F-731694
                            print(text)
                            if text[:3]=="ZAR":
                                if text[16:26]=="3QF121351E":
                                    self.CodeRadd = text
                                    self.DateLabel = text[3:9]
                                    self.DateLabel = self.DateLabel[:2] + "/" + self.DateLabel[2:4] + "/" + self.DateLabel[4:6]
                                    print(self.DateLabel)
                                    self.state = 1
                                else:
                                    print("Codigo Invalido por PartNo")
                                    QMessageBox.critical(None, "Numero de Parte Invalido",
                                                        f"Verificar Numero de Parte: {text[16:26]}")
                                    self.ui_main.txt_input.clear()
                            else:
                                print("Codigo Invalido por ID")
                                QMessageBox.critical(None, "ID Invalido",
                                                     f"Verificar Datos en Etiqueta: {text[:3]}")
                                self.ui_main.txt_input.clear()
                        else:
                            self.ui_main.txt_input.clear()

                    case 1:  # Check DataMatrix in DB
                        if dataBase.Check_nCode(self.CodeRadd) == False:
                            print(self.state)
                            self.state = 2
                        else:
                            print("Codigo Repetido")
                            self.state = 3

                    case 2:  # Add Table and DB
                        print(self.state)
                        dataBase.addModule(self.SerialNum, self.CodeRadd, self.DateLabel)
                        Approve(self.ui_main)
                        self.Alerts.singleShot(1000, lambda: HideAlerts(self.ui_main))

                        self.PzsRealizadas = int(self.PzsRealizadas) + 1
                        self.PzsFaltantes = int(self.PzsTotales) - int(self.PzsRealizadas)

                        self.ui_main.lcdNumber_Realizado.display(self.PzsRealizadas)
                        self.ui_main.lcdNumber_Faltantes.display(self.PzsFaltantes)
                        dataBase.updateData(self.PartNo, self.Supplier, self.OT, self.PzsTotales, self.PzsRealizadas,
                                            self.SerialNum, self.CreationDate)

                        #Check Current Count to print Master Label
                        if self.PzsFaltantes == 0 and self.PzsRealizadas == self.PzsTotales:
                            # Manda a imprimir
                            currDate = datetime.now()
                            # Formatear la fecha y hora en el formato deseado
                            hora_formateada = currDate.strftime("%d/%m/%Y %H:%M:%S")

                            fecha = hora_formateada
                            partNo = self.PartNo  # "3QF121257E"
                            Qty = str(self.PzsTotales)  # 10
                            supplier = self.Supplier  # "6001003941"
                            serial = self.SerialNum
                            OT = self.OT  # "162555

                            # Evalua el estado de la impresora
                            self.StatePrinter.stop()

                            # Envia a Imprimir
                            SendReqPrint(fecha, partNo, Qty, supplier, serial, OT)

                            # Guarda los datos en la DB master
                            dataBase.addMaster(self.SerialNum, self.PzsTotales, self.OT, self.CreationDate, fecha,
                                               "COMPLETADO")

                            # Actualiza los datos de los display
                            self.PzsRealizadas = 0
                            self.PzsFaltantes = self.PzsTotales - self.PzsRealizadas
                            self.ui_main.lcdNumber_Realizado.display(self.PzsRealizadas)
                            self.ui_main.lcdNumber_Faltantes.display(self.PzsFaltantes)
                            QApplication.processEvents()

                            # Crea un nuevo numero de serie
                            mSerie = str(currDate.strftime("%d%m%Y%H%M%S"))
                            serial = str("1802" + mSerie)
                            self.SerialNum = serial
                            self.CreationDate = fecha

                            # Actualiza la base de datos del backUp
                            dataBase.updateData(self.PartNo, self.Supplier, self.OT, self.PzsTotales,
                                                self.PzsRealizadas, self.SerialNum, self.CreationDate)

                            # Actializa los label de interfaz
                            self.ui_main.lbl_Serial1.setText(
                                QCoreApplication.translate("MainWindow", f"{self.SerialNum}", None))
                            self.ui_main.lbl_OT.setText(QCoreApplication.translate("MainWindow", f"{self.OT}", None))
                            self.ui_main.lbl_nPiezas.setText(QCoreApplication.translate("MainWindow",
                                                                                        f"<html><head/><body><p><span style=\" color:#ffc400;\">{self.PzsTotales}</span></p></body></html>",
                                                                                        None))
                            self.ui_main.lbl_Nparte.setText(
                                QCoreApplication.translate("MainWindow",
                                                           f"<html><head/><body><p>{self.PartNo}</p></body></html>",
                                                           None))

                            # Reinicia la consulta del estado de la impresora
                            self.StatePrinter.start(1000)

                            # Elimina el contenido del text edit y reinicia el escaneo
                            self.ui_main.txt_input.clear()
                            self.state = 0

                        else:
                            # Limpia el contenedor del text edit y reinicia el escaneo
                            self.ui_main.txt_input.clear()
                            self.state = 0

                    case 3:  # Repeat Data
                        print(self.state)
                        Repeat(self.ui_main)
                        self.Alerts.singleShot(1000, lambda: HideAlerts(self.ui_main))
                        # QApplication.processEvents()
                        self.ui_main.txt_input.clear()
                        self.state = 0
            else:
                if self.state != 2:
                    QMessageBox.warning(None, "Verificar Impresora",
                                        "Verificar que la impresora este correctamente configurada")
    def CreateTable(self):
        # Crear la tabla sin especificar el número de filas y columnas
        self.tableWidgetdataBase = QTableWidget(0, 5, self.ui_main.DatabaseWidget)
        #self.tableWidgetdataBase.setStyleSheet(u"background-color: rgb(18, 118, 118);border: 2px transparent #000000;border-radius: 5px;")

        self.tableWidgetdataBase.setObjectName(u"tableWidget")
        self.tableWidgetdataBase.setHorizontalHeaderLabels(
            ['ID', 'NUMERO DE SERIE', 'CODIGO DE RADIADOR', 'FECHA DE CREACION', 'FECHA DE ETIQUETA'])
        self.tableWidgetdataBase.horizontalHeader().setStyleSheet("background-color: #A9A9A9; color: black")
        self.tableWidgetdataBase.setStyleSheet("color: black")

        # Ajustar el tamaño de las columnas para que se expandan automáticamente
        #self.tableWidgetdataBase.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidgetdataBase.setAlternatingRowColors(True)
        self.tableWidgetdataBase.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidgetdataBase.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidgetdataBase.setSelectionMode(QTableWidget.SingleSelection)

        if self.ui_main.DatabaseWidget.layout() is not None:
            self.ui_main.DatabaseWidget.layout().addWidget(self.tableWidgetdataBase)
        else:
            # Puedes crear un nuevo QVBoxLayout si aún no hay un layout
            new_layout = QVBoxLayout()
            new_layout.addWidget(self.tableWidgetdataBase)
            self.ui_main.DatabaseWidget.setLayout(new_layout)
    def CreateTableMaster(self):
        # Crear la tabla sin especificar el número de filas y columnas
        self.tableMastertaBase = QTableWidget(0, 7, self.ui_main.DatabaseWidget)
        #self.tableWidgetdataBase.setStyleSheet(u"background-color: rgb(18, 118, 118);border: 2px transparent #000000;border-radius: 5px;")

        self.tableMastertaBase.setObjectName(u"tableWidget2")
        self.tableMastertaBase.setHorizontalHeaderLabels(
            ['ID', 'SERIAL', 'CANTIDAD', 'O.T.', 'F.CREACION', 'F.PRODUCCION', 'ESTATUS'])
        self.tableMastertaBase.horizontalHeader().setStyleSheet("background-color: #A9A9A9; color: black")
        self.tableMastertaBase.setStyleSheet("color: black")

        # Ajustar el tamaño de las columnas para que se expandan automáticamente
        #self.tableMastertaBase.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableMastertaBase.setAlternatingRowColors(True)
        self.tableMastertaBase.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableMastertaBase.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableMastertaBase.setSelectionMode(QTableWidget.SingleSelection)

        if self.ui_main.DatabaseWidget.layout() is not None:
            self.ui_main.DatabaseWidget.layout().addWidget(self.tableMastertaBase)
        else:
            # Puedes crear un nuevo QVBoxLayout si aún no hay un layout
            new_layout = QVBoxLayout()
            new_layout.addWidget(self.tableMastertaBase)
            self.ui_main.DatabaseWidget.setLayout(new_layout)
    def print_selected_row(self, row, column):
        row_data = []
        for col in range(self.tableMastertaBase.columnCount()):
            item = self.tableMastertaBase.item(row, col)
            if item is not None:
                row_data.append(item.text())
            else:
                row_data.append('')
        print(f"Row {row} data: {row_data}")

        # obtiene el respaldo de los datos
        data = dataBase.GetDataBackUp()
        # Variables que se inicializan con el backup
        partno = data[1]
        supplier=data[2]
        serial= row_data[1]
        cantidad = row_data[2]
        ot= row_data[3]
        self.ConfirmPrint(partno, cantidad, supplier, serial, ot)
    def HistorialPressed(self):
        self.ui_main.btn_printCurrIndex.hide()
        self.tableMastertaBase.hide()
        self.tableWidgetdataBase.show()
        dataBase.InsertinTable(1,self.tableWidgetdataBase, 10)
        # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
        self.tableWidgetdataBase.resizeColumnsToContents()
        self.ui_main.MenuPrincipal.setCurrentIndex(4)
        self.Key = False
    def HistorialMasterPressed(self):
        self.ui_main.btn_printCurrIndex.hide()
        self.tableWidgetdataBase.hide()
        self.tableMastertaBase.show()
        dataBase.InsertinTable(2, self.tableMastertaBase, 10)
        # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
        self.tableMastertaBase.resizeColumnsToContents()
        self.ui_main.MenuPrincipal.setCurrentIndex(4)
        self.Key=False
    def PrintPressed(self):
        self.ui_main.btn_printCurrIndex.hide()
        if self.Key == True:
            self.ui_main.box_serial.clear()
            #self.ui_main.box_OT.clear()
            self.ui_main.box_serial.addItems(dataBase.GetSerialMaster("atlas_master"))
            #self.ui_main.box_OT.addItems(dataBase.GetOTMaster("atlas_master"))
            dataBase.InsertinTable(2, self.tableMastertaBase, 30)
            # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
            self.tableMastertaBase.resizeColumnsToContents()
            self.ui_main.MenuPrincipal.setCurrentIndex(4)#5
    def HomePressed(self):
        self.Key = False
        self.ui_main.btn_printCurrIndex.hide()
        self.ui_main.MenuPrincipal.setCurrentIndex(6)
    def DataMatrixPressed(self):
        self.Key = False
        self.ui_main.btn_printCurrIndex.hide()
        self.ui_main.MenuPrincipal.setCurrentIndex(7)
    def ShowDialog(self, dialog, enable):
        if enable:
            dialog.setModal(True)
            # Muestra el diálogo
            dialog.show()
        else:
            # Oculta el diálogo si enable es False
            dialog.hide()
    def GetData(self):
        if len(self.ui_main.box_serial.currentText())>0:
            self.ui_main.btn_PrintLabel.hide()
            serial = self.ui_main.box_serial.currentText()
            print(serial, type(serial))
            result = dataBase.GetDataMaster(serial)
            data = dataBase.GetDataBackUp()
            partno = data[1]
            qty = result[2]
            supplier = data[2]
            ot = result[3]

            self.ui_main.lbl_PartNoprint.setText(partno)
            self.ui_main.lbl_QtyPrint.setText(qty)
            self.ui_main.lbl_ProveedorPrint.setText(supplier)
            self.ui_main.lbl_OTPrint.setText(ot)

            #partno = self.ui_main.box_PartNo.currentText()
            #qty = self.ui_main.box_Cantidad.currentText()
            #supplier = self.ui_main.box_proveedor.currentText()
            #ot = self.ui_main.box_OT.currentText()
            self.ConfirmPrint(partno, qty, supplier, serial, ot)
        else:
            QMessageBox.warning(None, "Informacion Incompleta", "Verificar que todos los campos esten correctamente especificados")
    def GetData_original(self):
        if len(self.ui_main.box_PartNo.currentText()) > 0 and len(self.ui_main.box_Cantidad.currentText()) > 0 and len(self.ui_main.box_proveedor.currentText()) > 0 and len(self.ui_main.box_serial.currentText()) > 0 and len(self.ui_main.box_OT.currentText()) > 0:
            self.ui_main.btn_PrintLabel.hide()
            partno = self.ui_main.box_PartNo.currentText()
            qty = self.ui_main.box_Cantidad.currentText()
            supplier = self.ui_main.box_proveedor.currentText()
            serial = self.ui_main.box_serial.currentText()
            ot = self.ui_main.box_OT.currentText()
            self.ConfirmPrint(partno, qty, supplier, serial, ot)
        else:
            QMessageBox.warning(None, "Informacion Incompleta",
                                "Verificar que todos los campos esten correctamente especificados")
    def ConfirmPrint(self, PartNo,Qty,Supplier,Serial,OT):
        ConfirmPrint = ConfirmData()
        ConfirmPrint.setModal(True)
        ConfirmPrint.SetData(PartNo, Qty, Supplier, Serial, OT)
        ConfirmPrint.exec()

        result = ConfirmPrint.state

        if result == True:
            if self.Key ==True:
                print("Imprime Etiqueta")
                currDate = datetime.now()
                currDate = currDate.strftime("%d/%m/%Y %H:%M:%S")
                self.StatePrinter.stop()
                SendReqPrint(currDate, PartNo, Qty, Supplier, Serial, OT)
                QMessageBox.information(None, "Etiqueta Impresa", "Se ha enviado la etiqueta correctamente")

                self.ui_main.btn_PrintLabel.show()
                self.ui_main.MenuPrincipal.setCurrentIndex(6)
                self.Key = False
                self.StatePrinter.start(1000)

        else:
            print("Editar informacion")
            self.ui_main.btn_PrintLabel.show()
            self.ui_main.btn_saveDataLabel.hide()
    def ShowLoggin(self):
        loggin = Loggin()
        loggin.setModal(True)
        loggin.exec()
        self.Key = loggin.state

        if self.Key == True:
            self.ui_main.MenuPrincipal.setCurrentIndex(1)
        else:
            self.ui_main.MenuPrincipal.setCurrentIndex(6)
            self.Key=False
    def SetCurrentData(self):
        if len(self.ui_main.initBox_PartNo.currentText())>0 and len(self.ui_main.initBox_Cantidad.currentText())>0 and len(self.ui_main.initBox_Proveedor.currentText())>0 and len(self.ui_main.initTxt_OT.toPlainText())>0:
            print("Guardar Datos")
            PartNo = self.ui_main.initBox_PartNo.currentText()
            Cantidad = self.ui_main.initBox_Cantidad.currentText()
            Proveedor = self.ui_main.initBox_Proveedor.currentText()
            OT = self.ui_main.initTxt_OT.toPlainText()

            currDate = datetime.now()
            hora_formateada = currDate.strftime("%d/%m/%Y %H:%M:%S")
            fecha = hora_formateada
            mSerie = str(currDate.strftime("%d%m%Y%H%M%S"))
            serial = str("1802" + mSerie)
            self.SerialNum = serial
            self.CreationDate = fecha

            self.PartNo = PartNo
            self.Supplier = Proveedor
            self.OT = OT
            self.PzsTotales = Cantidad
            self.PzsRealizadas = 0
            self.PzsFaltantes = int(self.PzsTotales) - int(self.PzsRealizadas)

            # Actualiza la base de datos del backUp
            dataBase.updateData(self.PartNo, self.Supplier, self.OT, self.PzsTotales, self.PzsRealizadas,
                                self.SerialNum,
                                self.CreationDate)

            self.ui_main.lbl_Serial1.setText(QCoreApplication.translate("MainWindow", f"{self.SerialNum}", None))
            self.ui_main.lbl_OT.setText(QCoreApplication.translate("MainWindow", f"{self.OT}", None))
            self.ui_main.lbl_nPiezas.setText(QCoreApplication.translate("MainWindow",
                                                                        f"<html><head/><body><p><span style=\" color:#ffc400;\">{self.PzsTotales}</span></p></body></html>",
                                                                        None))
            self.ui_main.lbl_Nparte.setText(
                QCoreApplication.translate("MainWindow", f"<html><head/><body><p>{self.PartNo}</p></body></html>",
                                           None))
            self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                             f"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Estado de la Impresora: </span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\"></span></p></body></html>",
                                                                             None))
            self.ui_main.lcdNumber_Realizado.display(self.PzsRealizadas)
            self.ui_main.lcdNumber_Faltantes.display(self.PzsFaltantes)

            self.ui_main.MenuPrincipal.setCurrentIndex(6)
            self.Key = False
            QMessageBox.information(None, "Informacion Actualizada", "Datos Actualizados Correctamente")

        else:
            QMessageBox.warning(None, "Informacion Incompleta", "Verificar que todos los campos esten correctamente especificados")
    def CancelChange(self):
        self.Key=False
        self.ui_main.MenuPrincipal.setCurrentIndex(6)

if __name__ == "__main__":
    app = QApplication([])
    window = Atlas()
    window.show()
    app.exec()
