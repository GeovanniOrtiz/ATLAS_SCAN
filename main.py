import os
import sys
import time
from datetime import datetime
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidget, QVBoxLayout, QHeaderView, QDialog, QMessageBox, \
    QTextEdit, QLineEdit, QLabel
from LAN.LAN_Connection import WifiMonitor
from Server.ServerMonitor import *
from API_Functions.request_API import *
from Interfaz.AtlasInterfaz_gui import Ui_MainWindow as Interfaz
from Alerts import *
from Printer import *
from SQL import managerDataBase

from Interfaz.Dialogo_ConfirmData_gui import Ui_Dialog as ConfirmData
from Interfaz.Loggin_gui import Ui_Dialog as Loggin
from Printer import ConsultStatePrint, PrinterState
import json

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

        self.state=0

        # Elimina la barra de menú y el botón de cierre
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.box_Admin.addItems(["Administrador", "Usuario"])
        self.btn_iniciarSesion.released.connect(self.tryInit)
        self.btn_cancelar.released.connect(self.Cancel)

    def tryInit(self):
        if self.box_Admin.currentText() == 'Usuario' and len(self.txt_User.toPlainText())>0 and len(self.line_contra.text())>0:
            print("Get data")
            username = self.txt_User.toPlainText()
            password = self.line_contra.text()

            # Aquí puedes realizar la validación del usuario y contraseña
            if username == "Atlas2024" and password == "0300":
                # Ejemplo simple de validación: solo imprimir los valores ingresados
                #print(f"Usuario: {username}, Contraseña: {password}")
                # Cerrar el cuadro de diálogo después de iniciar sesión
                self.state=1
                self.accept()
                QMessageBox.information(None, "Bienvenido", "Usuario registrado con exito")

            else:
                QMessageBox.information(None, "Verificar Informacion", "Usuario o Contraseña Incorrectos")
        elif self.box_Admin.currentText() == 'Administrador' and len(self.txt_User.toPlainText()) > 0 and len(self.line_contra.text()) > 0:
            print("Get data")
            username = self.txt_User.toPlainText()
            password = self.line_contra.text()

            # Aquí puedes realizar la validación del usuario y contraseña
            if username == "Atlas" and password == "0900":
                # Ejemplo simple de validación: solo imprimir los valores ingresados
                #print(f"Usuario: {username}, Contraseña: {password}")
                # Cerrar el cuadro de diálogo después de iniciar sesión
                self.state = 2
                self.accept()
                QMessageBox.information(None, "Bienvenido", "Administrador registrado con exito")

            else:
                QMessageBox.information(None, "Verificar Informacion", "Usuario o Contraseña Incorrectos")

        else:
            QMessageBox.information(None, "Verificar Informacion", "Usuario o Contraseña Incorrectos")

    def Cancel(self):
        self.state=False
        self.reject()

class DialogoError(QDialog):
    def __init__(self, mensaje, parent=None):
        super().__init__(parent)
        self.mensaje = mensaje
        self.setWindowTitle("Aviso")
        self.setFixedSize(400, 200)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # Opcional: sin bordes de ventana
        self.setup_ui()

    def setup_ui(self):
        # Estilo con fondo rojo semitransparente y borde rojo
        self.setStyleSheet("""
            QDialog {
                background-color: rgba(255, 0, 0, 100);  /* Rojo con transparencia */
                border: 4px solid red;
                border-radius: 10px;
            }
            QLabel {
                color: white;
                font-size: 34px;
                font-weight: bold;
            }
        """)

        etiqueta = QLabel(self.mensaje, self)
        etiqueta.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)
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

        # lee si se configurara algun parametro
        self.GetPrinetMode()

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
        # Conecta la senal con el text edit
        self.ui_main.txt_input.textChanged.connect(self.on_text_changed)
        self.ui_main.btn_deleteRegister.released.connect(self.delete_CurrData)
    def initGui(self):
        #Esconde el label de Alertas de proceso
        HideAlerts(self.ui_main)

        #Crea la instancia de PrinterState
        self.printer_state = PrinterState()

        #Timer para consultar el estado de la impresora
        self.StatePrinter = QTimer()
        self.StatePrinter.timeout.connect(lambda:ConsultStatePrint(self.ui_main, self.printer_state))
        self.StatePrinter.start(2000)
        ConsultStatePrint(self.ui_main, self.printer_state)

        # Esconde el boton de eliminar registros
        self.ui_main.btn_deleteRegister.setVisible(False)

        #timer para correr el proceso de escaneado
        self.TimeProcess = QTimer()
        self.TimeProcess.timeout.connect(self.Run_process)
        self.TimeProcess.start(200)

        # Timer para la lectura del Codigo de barras
        self.timerRead_text = QTimer()
        self.timerRead_text.timeout.connect(self.Focus_textEdit)
        self.timerRead_text.start(480)

        #Timer para las alertas vizuales
        self.Alerts = QTimer()
        self.AlertsFisrtScan = QTimer()

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
        self.timeAlarma=0

        #Calcula las piezas faltantes a escanear
        self.PzsFaltantes = int(self.PzsTotales - self.PzsRealizadas)
        self.PrinterMode = 0
        self.state = 0
        self.CodeRadd = ""
        self.DateLabel = ""
        self.Key=False

        self.mStatus_Wifi = 0
        self.mStatus_Server = 0
        self.retries = 0
        self.firstScan=1

        # Mantiene checkeado el boton toogle
        self.ui_main.toggleButton.setChecked(True)
        self.ui_main.toggleButton.setEnabled(False)

        # Recuperar datos de archivo Json
        self._Get_InitConditions()

        #Actualiza las vistas de  los label de interfaz
        self._Update_ViewLabels()

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
        #self.ui_main.initBox_Cantidad.addItems(["5", "6", "7", "8", "9", "10"])
        # Cargar los valores desde el JSON
        self.load_items_from_json()
        mData = dataBase.GetDataBackUp()
        PzsTotales = mData[4]
        self.ui_main.initBox_Cantidad.setCurrentText(PzsTotales)
        self.ui_main.initBox_Proveedor.addItems(["6001003941"])
        self.ui_main.initTxt_OT.clear()

        #Esconde el boton de imprimir
        self.ui_main.btn_printCurrIndex.hide()

        #Inicializa el widget con la tabla master
        self.tableMastertaBase.show()

        # Define variables para conexion de red
        self.ssid = "ADMINISTRATIVOS"  # SSID
        self.password = "M3X1C086"  # Password

        # Instancia de la Clase de Red Wifi
        self.WIFI = WifiMonitor(self.ssid, self.password)
        self.WIFI.connection_status_changed.connect(self.Update_WifiLabel)

        # Crear el monitor de conexión
        self.ServerMonitor = ConnectionMonitor()
        self.ServerMonitor.connection_status_changed.connect(self.Update_ServerLabel)
        self.ServerMonitor.start()

    def load_items_from_json(self):
        # Leer el archivo JSON
        archivo = "./Data/data.json"
        with open(archivo, 'r') as file:
            config_data = json.load(file)

        # Obtener el valor máximo
        max_value = config_data.get("cantidad", 10)  # 10 es un valor por defecto

        # Llenar el ComboBox con los valores desde 1 hasta max_value
        self.ui_main.initBox_Cantidad.addItems([str(i) for i in range(1, max_value + 1)])
    def UpdateLabelStatus_printer(self):
        mState = self.printer_state.mState
        mText = self.printer_state.mText
        match mState:
            case 0:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                "	border-color: rgb(0, 85, 255);\n"
                "	border-radius:5px;\n"
                "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#7FFF00;\">{mText}</span></p></body></html>", None))

            case 1:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                "	border-color: rgb(0, 85, 255);\n"
                "	border-radius:5px;\n"
                "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>", None))

            case 2:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                "	border-color: rgb(0, 85, 255);\n"
                "	border-radius:5px;\n"
                "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>", None))

            case 3:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                "	border-color: rgb(0, 85, 255);\n"
                "	border-radius:5px;\n"
                "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                                 f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>",
                                                                                 None))
            case 4:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                "	border-color: rgb(0, 85, 255);\n"
                "	border-radius:5px;\n"
                "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">{mText}</span></p></body></html>",
                                                                            None))
            case 5:
                self.ui_main.lbl_PrinterState.setStyleSheet(u"QLabel {\n"
                "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                "	border-color: rgb(0, 85, 255);\n"
                "	border-radius:5px;\n"
                "}")
                self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                         f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADA</span></p></body></html>",
                                                                         None))

    @Slot(bool)
    def Update_WifiLabel(self, status):
        """
        Actualiza la etiqueta de estado con la información más reciente.
        """
        if status == False:
            self.mStatus_Wifi = 0
            self.ui_main.lbl_wifiState.setStyleSheet(u"QLabel {\n"
                                                     "    border: 2px solid #FF0000; /* Cambia el color del borde a rojo */\n"
                                                     "	border-color: #FF0000;\n"
                                                     "	border-radius:5px;\n"
                                                     "}")
            self.ui_main.lbl_wifiState.setText(QCoreApplication.translate("MainWindow",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">WIFI: <br/></span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADO</span></p></body></html>",
                                                                          None))
        else:
            self.mStatus_Wifi = 1
            self.ui_main.lbl_wifiState.setStyleSheet(u"QLabel {\n"
                                                     "    border: 2px solid #FF0000;\n"
                                                     "	border-color: rgb(0, 85, 255);\n"
                                                     "	border-radius:5px;\n"
                                                     "}")
            self.ui_main.lbl_wifiState.setText(QCoreApplication.translate("MainWindow",
                                                                          u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">WIFI: <br/></span><span style=\" font-size:16pt; font-weight:700; color:#7FFF00;\">CONECTADO</span></p></body></html>",
                                                                          None))

    @Slot(bool)
    def Update_ServerLabel(self, status):
        if status:
            self.mStatus_Server = 1
            self.ui_main.lbl_ServerState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #00aa00;\n"
                                                       "	border-color:rgb(0, 85, 255);\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
            self.ui_main.lbl_ServerState.setText(QCoreApplication.translate("MainWindow",
                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">SERVIDOR:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#7FFF00;\">EN LINEA</span></p></body></html>",
                                                                            None))

        else:
            self.mStatus_Server = 0
            self.ui_main.lbl_ServerState.setStyleSheet(u"QLabel {\n"
                                                       "    border: 2px solid #FF0000;\n"
                                                       "	border-color: #FF0000;\n"
                                                       "	border-radius:5px;\n"
                                                       "}")
            self.ui_main.lbl_ServerState.setText(QCoreApplication.translate("MainWindow",
                                                                            u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">SERVIDOR:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#FF0000;\">DESCONECTADO</span></p></body></html>",
                                                                            None))

            """QMessageBox.information(None, "Servidor sin Conexion",
                                "Espera a que el servidor este conectado para comenzar. "
                                "Verificar conexion WIFI")"""
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

        if self.ui_main.MenuPrincipal.currentIndex() != 6:
            return

        if not self._is_ready():
            self._handle_errors()
            return

        # Sistema listo, iniciar proceso
        self.retries = 0
        self.DMC_SCAN()
    @Slot()
    def Focus_textEdit(self):
        if self.ui_main.MenuPrincipal.currentIndex() != 6:
            return

        self.ui_main.txt_input.setFocus()
    @Slot()
    def on_text_changed(self):
        #ZAR27052409020013QF121251E-0795677
        self.ui_main.txt_input.setFocus()
        text = self.ui_main.txt_input.toPlainText()

        # Esperar a que el escáner termine de enviar (incluye \n o \r)
        if not text.endswith('\n') and not text.endswith('\r'):
            return

        # Limpiar texto de caracteres invisibles
        text = text.strip()

        # Verifica longitud y parte
        if (len(text) == 34):
            if text[:3] == "ZAR":
                if text[16:26] ==  self.PartNo:
                    self.CodeRadd = text
                    self.DateLabel = text[3:9]
                    self.DateLabel = self.DateLabel[:2] + "/" + self.DateLabel[2:4] + "/" + self.DateLabel[4:6]
                    print(self.DateLabel)
                    self.state = 1
                else:
                    print("Codigo Invalido por PartNo")
                    # Muestra Dialogo de Pieza con error de numero de Parte
                    piezaIncorrecta = DialogoError(f"Error Número de Parte:\n {text[16:26]}")
                    piezaIncorrecta.setModal(True)
                    piezaIncorrecta.exec()

            else:
                print("Codigo Invalido por ID")
                QMessageBox.critical(None, "ID Invalido",
                                     f"Verificar Datos en Etiqueta: {text[:3]}")
                self.ui_main.txt_input.clear()

        else:
            # Muestra label de Aprovado
            Longitud_error(self.ui_main)
            self.Alerts.singleShot(self.timeAlarma, lambda: HideAlerts(self.ui_main))
            print("Longitud incorrecta")

        # Limpia después de procesar
        self.ui_main.txt_input.clear()
    @Slot()
    def _is_ready(self):
        _wifi = self.wifiControl
        _server = self.Servercontrol

        if _wifi and _server:
            return self.printer_state.mState == 0 and self.mStatus_Wifi == 1 and self.mStatus_Server == 1
        elif _wifi:
            return self.printer_state.mState == 0 and self.mStatus_Wifi == 1
        elif _server:
            return self.printer_state.mState == 0 and self.mStatus_Server == 1

        return self.printer_state.mState == 0  # Si ninguno está activado, la app no está lista.
    @Slot()
    def DMC_SCAN(self):
        match self.state:
            case 0:  # Read TextEdit
                pass

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

                # Verifica conexion con la API
                if self.mStatus_Server == 1 and self.Servercontrol == True:
                    #Adquiere datos de la etiqueta
                    station, partNo, _serial = self._extract_label_data(self.CodeRadd)

                    # Asigna los varlores obtenidos del DMC actual
                    chamber = station
                    leak = 0.00

                    # Envia los registros al server
                    set_Register(chamber, partNo, _serial, leak, 2)

                    # lanza el mensaje de aprovado desde el servidor
                    ApproveServer(self.ui_main)
                    self.Alerts.singleShot(self.timeAlarma, lambda: HideAlerts(self.ui_main))

                else:
                    # Muestra label de Aprovado
                    Approve(self.ui_main)
                    self.Alerts.singleShot(self.timeAlarma, lambda: HideAlerts(self.ui_main))

                self.PzsRealizadas = int(self.PzsRealizadas) + 1
                self.PzsFaltantes = int(self.PzsTotales) - int(self.PzsRealizadas)

                if int(self.PzsRealizadas) >= int(self.PzsTotales):
                    self.PzsRealizadas = int(self.PzsTotales)

                if int(self.PzsFaltantes) <= 0:
                    self.PzsFaltantes = 0

                self.ui_main.lcdNumber_Realizado.display(self.PzsRealizadas)
                self.ui_main.lcdNumber_Faltantes.display(self.PzsFaltantes)

                dataBase.updateData(self.PartNo, self.Supplier, self.OT, self.PzsTotales, self.PzsRealizadas,
                                    self.SerialNum, self.CreationDate)

                # Check Current Count to print Master Label
                if int(self.PzsFaltantes) == 0 and int(self.PzsRealizadas) == int(self.PzsTotales):
                    # Manda a imprimir
                    currDate = datetime.datetime.now()
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
                    self.PzsFaltantes = int(self.PzsTotales)

                    self.ui_main.lcdNumber_Realizado.display(self.PzsRealizadas)
                    self.ui_main.lcdNumber_Faltantes.display(self.PzsFaltantes)
                    QApplication.processEvents()

                    # Crea un nuevo numero de serie
                    mSerie = str(currDate.strftime("%d%m%Y%H%M%S"))
                    serial = str("1609" + mSerie)
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
                                                                                f"<html><head/><body><p><span style=\" color:#e12807;\">{self.PzsTotales}</span></p></body></html>",
                                                                                None))
                    self.ui_main.lbl_Nparte.setText(
                        QCoreApplication.translate("MainWindow",
                                                   f"<html><head/><body><p>{self.PartNo}</p></body></html>",
                                                   None))

                    QMessageBox.information(None, "COMPLETADO",
                                            f"Contenedor Completado con exito!")

                    # Reinicia la consulta del estado de la impresora
                    self.StatePrinter.start(2000)

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
                self.Alerts.singleShot(self.timeAlarma, lambda: HideAlerts(self.ui_main))
                # QApplication.processEvents()
                self.ui_main.txt_input.clear()
                self.state = 0

    @Slot(str)
    def _extract_label_data(self, cadena: str) -> tuple:
        id = cadena[0:3]
        date = cadena[3:9]  # formato ddmmyy
        hour = cadena[9:15]  # formato hhmmss
        chamber = cadena[15]  # un solo dígito
        partNo = cadena[16:26]  # 10 caracteres
        separator = cadena[26]  # el guion "-"
        SerialNum = cadena[27:]  # el resto del string

        return chamber, partNo, SerialNum

    @Slot()
    def _handle_errors(self):
        """Maneja los mensajes de error dependiendo del estado de la aplicación."""
        if self.firstScan == 1:
            self.AlertsFisrtScan.singleShot(3000, lambda: self._reset_first_scan())

        elif self.printer_state.mState != 0:
            self._show_error("IMPRESORA", "Verificar el estado de la Impresora")

        elif self.mStatus_Wifi == 0:
            self.retries += 1
            self._show_error("CONEXION", f"Verificar la conexión WIFI del equipo.\nIntentos: {self.retries}/5")

        elif self.mStatus_Server == 0:
            self.retries += 1
            self._show_error("SERVIDOR", f"Verificar el SERVIDOR\nIntentos: {self.retries}/5")

        if self.retries > 4:
            self._show_error("CONEXION FALLIDA",
                             "El dispositivo no logra establecer una conexion exitosa.\nEjecute el setup para deshabilitar el monitoreo.")
            sys.exit(0)

    @Slot(str, str)
    def _show_error(self, title: str, message: str):
        """Muestra un mensaje de error y limpia la entrada."""
        print(f"Error: {message}")
        QMessageBox.critical(self, title, message)
    @Slot()
    def _reset_first_scan(self):
        self.firstScan = 0
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
        dataBase.InsertinTable(1, self.tableWidgetdataBase, 30)
        # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
        self.tableWidgetdataBase.resizeColumnsToContents()
        self.ui_main.MenuPrincipal.setCurrentIndex(4)
        self.Key = False
    def HistorialMasterPressed(self):
        self.ui_main.btn_printCurrIndex.hide()
        self.tableWidgetdataBase.hide()
        self.tableMastertaBase.show()
        dataBase.InsertinTable(2, self.tableMastertaBase, 30)
        # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
        self.tableMastertaBase.resizeColumnsToContents()
        self.ui_main.MenuPrincipal.setCurrentIndex(4)
        self.Key=False
    def PrintPressed(self):
        self.ui_main.btn_printCurrIndex.hide()
        if self.Key == True:
            #self.ui_main.box_serial.clear()
            #self.ui_main.box_OT.clear()
            #self.ui_main.box_serial.addItems(dataBase.GetSerialMaster("atlas_master"))
            #self.ui_main.box_OT.addItems(dataBase.GetOTMaster("atlas_master"))
            self.tableWidgetdataBase.hide()
            dataBase.InsertinTable(2, self.tableMastertaBase, 5)
            # Después de agregar los datos a la tabla, ajusta el ancho de las columnas al contenido máximo
            self.tableMastertaBase.resizeColumnsToContents()
            self.tableMastertaBase.show()
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
                currDate = datetime.datetime.now()
                currDate = currDate.strftime("%d/%m/%Y %H:%M:%S")
                self.StatePrinter.stop()
                SendReqPrint(currDate, PartNo, Qty, Supplier, Serial, OT)
                QMessageBox.information(None, "Etiqueta Impresa", "Se ha enviado la etiqueta correctamente")

                self.ui_main.btn_PrintLabel.show()
                self.ui_main.MenuPrincipal.setCurrentIndex(6)
                self.Key = False
                self.StatePrinter.start(2000)

        else:
            print("Editar informacion")
            self.ui_main.btn_PrintLabel.show()
            self.ui_main.btn_saveDataLabel.hide()
    def ShowLoggin(self):
        loggin = Loggin()
        loggin.setModal(True)
        loggin.exec()
        self.Key = loggin.state

        if self.Key == 1:
            # Muestra los botones de editar e imprimir
            self.ui_main.btn_PrintAction.show()
            self.ui_main.btn_EditAction.show()

            # Esconde el boton de Delete Register
            self.ui_main.btn_deleteRegister.setVisible(False)

            # Envia la GUI a la pagina de Accion
            self.ui_main.MenuPrincipal.setCurrentIndex(1)
        elif self.Key ==2:
            # Oculta los botones de editar e imprimir
            self.ui_main.btn_PrintAction.hide()
            self.ui_main.btn_EditAction.hide()

            # Muestra el boton de Delete Register
            self.ui_main.btn_deleteRegister.setVisible(True)

            # Envia la GUI a la pagina de Accion
            self.ui_main.MenuPrincipal.setCurrentIndex(1)

        else:
            # Esconde el boton de Delete Register
            self.ui_main.btn_deleteRegister.setVisible(False)

            # Envia la GUI a la pagina Principal
            self.ui_main.MenuPrincipal.setCurrentIndex(6)
            self.Key = 0
    def SetCurrentData(self):
        if len(self.ui_main.initBox_PartNo.currentText())>0 and len(self.ui_main.initBox_Cantidad.currentText())>0 and len(self.ui_main.initBox_Proveedor.currentText())>0 and len(self.ui_main.initTxt_OT.toPlainText())>0:
            print("Guardar Datos")
            PartNo = self.ui_main.initBox_PartNo.currentText()
            Cantidad = self.ui_main.initBox_Cantidad.currentText()
            Proveedor = self.ui_main.initBox_Proveedor.currentText()
            OT = self.ui_main.initTxt_OT.toPlainText()

            currDate = datetime.datetime.now()
            hora_formateada = currDate.strftime("%d/%m/%Y %H:%M:%S")
            fecha = hora_formateada
            mSerie = str(currDate.strftime("%d%m%Y%H%M%S"))
            serial = str("1609" + mSerie)
            self.SerialNum = serial
            self.CreationDate = fecha

            self.PartNo = PartNo
            self.Supplier = Proveedor
            self.OT = OT
            self.PzsTotales = int(Cantidad)
            self.PzsRealizadas= 0
            self.PzsFaltantes = int(self.PzsTotales)

            # Actualiza la base de datos del backUp
            dataBase.updateData(self.PartNo, self.Supplier, self.OT, self.PzsTotales, self.PzsRealizadas,
                                self.SerialNum,
                                self.CreationDate)

            self.ui_main.lbl_Serial1.setText(QCoreApplication.translate("MainWindow", f"{self.SerialNum}", None))
            self.ui_main.lbl_OT.setText(QCoreApplication.translate("MainWindow", f"{self.OT}", None))
            self.ui_main.lbl_nPiezas.setText(QCoreApplication.translate("MainWindow",
                                                                        f"<html><head/><body><p><span style=\" color:#e12807;\">{self.PzsTotales}</span></p></body></html>",
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
            self.Key = 0
            QMessageBox.information(None, "Informacion Actualizada", "Datos Actualizados Correctamente")

        else:
            QMessageBox.warning(None, "Informacion Incompleta", "Verificar que todos los campos esten correctamente especificados")
    def CancelChange(self):
        self.Key=0
        self.ui_main.MenuPrincipal.setCurrentIndex(6)

    def GetPrinetMode(self):
        # Abre y lee el contenido del archivo JSON
        archivo = "./Data/data.json"
        with open(archivo, 'r') as file:
            data = json.load(file)

        # Extrae los enteros del JSON
        template = data.get('template')
        calibrate = data.get('calibrate')
        timeAlarm = data.get('time')
        self.timeAlarma=int(timeAlarm)
        #print(self.timeAlarma)

        if template == 1:
            SendTemplate()
        elif calibrate == 1:
            SendLabelCalibrate()

    @Slot()
    def Read_Json(self):
        """
        Metodo que obtiene los valores base de cada estacion. Se define los Puertos COM y direcciones IP.
        :return:
        """
        archivo = "./Data/setup.json"
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Asignar los valores a variables individuales
        WIFI = data["WIFI"]
        SERVER = data["SERVER"]
        CODE = data["CODE"]
        return WIFI, SERVER, CODE

    @Slot()
    def delete_CurrData(self):
        # obtiene el valor actual del contador de piezas realizadas
        count = int(self.ui_main.lcdNumber_Realizado.value())
        print(count)

        if count > 0:
            # Elimina los registros grabados sin cerrar orden
            dataBase._delete_last_registers(dataBase.DB_table, count)

            # Eliminar los ultimos n registros de la tabla
            dataBase._delete_last_rows(self.tableWidgetdataBase, count)

            # Muestra el aviso de que los registros han sido Eliminados
            QMessageBox.warning(self, "Regitros Eliminados",
                                f"Se han eliminado los ultimos {count} registros con exito")

            # Actualiza el valor de piezas realizadas
            self.PzsRealizadas = 0

            # Actualiza el valor de piezas faltantes
            self.PzsFaltantes = int(self.PzsTotales)

            # Actualiza la base de datos del backUp
            dataBase.updateData(self.PartNo, self.Supplier, self.OT, self.PzsTotales, self.PzsRealizadas,
                                self.SerialNum,
                                self.CreationDate)

            # Actualiza los LCD de la GUI.
            self.ui_main.lcdNumber_Realizado.display(self.PzsRealizadas)
            self.ui_main.lcdNumber_Faltantes.display(self.PzsTotales)

            # Manda la GUI a la interfaz principal
            self.ui_main.MenuPrincipal.setCurrentIndex(6)
        else:
            # Muestra el aviso de que los registros han sido Eliminados
            QMessageBox.warning(self, "Sin Registros",
                                f"No existen registros a eliminar.")
            # Manda la GUI a la interfaz principal
            self.ui_main.MenuPrincipal.setCurrentIndex(6)

    @Slot()
    def _Get_InitConditions(self):
        try:
            wifi, server, code = self.Read_Json()
            self.wifiControl = wifi == "1"
            self.Servercontrol = server == "1"
            self.codeControl = code == "1"  # si es True es DMC si es False es CODE BAR

        except Exception as e:
            QMessageBox.critical(self, "Alerta de Registro", "No se encontro registro solicitado, ejecuta el setup!")

            # Si el archivo esta roto se procede a eliminarlo
            archivo = "./Data/setup.json"
            if os.path.exists(archivo):
                os.remove(archivo)
                print(f"{archivo} ha sido eliminado")

            else:
                print(f"{archivo} no se encontró")
            sys.exit(0)

    @Slot()
    def _Update_ViewLabels(self):
        self.ui_main.lbl_Serial1.setText(QCoreApplication.translate("MainWindow", f"{self.SerialNum}", None))
        self.ui_main.lbl_OT.setText(QCoreApplication.translate("MainWindow", f"{self.OT}", None))
        self.ui_main.lbl_nPiezas.setText(QCoreApplication.translate("MainWindow",
                                                                    f"<html><head/><body><p><span style=\" color:#e12807;\">{self.PzsTotales}</span></p></body></html>",
                                                                    None))
        self.ui_main.lbl_Nparte.setText(
            QCoreApplication.translate("MainWindow", f"<html><head/><body><p>{self.PartNo}</p></body></html>", None))
        self.ui_main.lbl_PrinterState.setText(QCoreApplication.translate("MainWindow",
                                                                         u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">IMPRESORA:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">CONECTANDO...</span></p></body></html>",
                                                                         None))
        self.ui_main.lbl_ServerState.setStyleSheet(u"QLabel {\n"
                                                   "    border: 2px solid #00aa00;\n"
                                                   "	border-color:rgb(0, 85, 255);\n"
                                                   "	border-radius:5px;\n"
                                                   "}")
        self.ui_main.lbl_ServerState.setText(QCoreApplication.translate("MainWindow",
                                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">SERVIDOR:<br/></span><span style=\" font-size:16pt; font-weight:700; color:#ffc400;\">CONECTANDO...</span></p></body></html>",
                                                                        None))

        self.ui_main.lbl_labelMasterEdit.setPixmap(QPixmap(u"./Label_Master.PNG"))

if __name__ == "__main__":
    app = QApplication([])
    window = Atlas()
    window.show()
    app.exec()
