import re
import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt

from PySide6.QtCore import Qt, Slot, QTimer, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox, QMessageBox, QScrollArea, QVBoxLayout, QFileDialog, \
    QDialog, QLabel, QProgressBar, QPushButton

from Interfaz.Rugosimetro_gui import Ui_MainWindow as Interfaz
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QComboBox
from PySide6.QtCore import Qt

class WelcomeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Bienvenido")
        self.setFixedSize(360, 260)
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)

        # Atributos para guardar selecciones
        self.selected_cutoff = None
        self.selected_cuadros = None

        # Estilo inspirado en Material Design + colores personalizados
        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e1e;
                border: 3px solid #e12807;
                border-radius: 12px;
            }
            QLabel {
                color: white;
                font-size: 17px;
                padding: 10px;
                font-weight: 500;
            }
            QComboBox {
                background-color: #2e2e2e;
                color: white;
                padding: 6px;
                border: 1px solid #e12807;
                border-radius: 6px;
                font-size: 14px;
            }
            QComboBox QAbstractItemView {
                background-color: #2e2e2e;
                color: white;
                selection-background-color: #e12807;
            }
            QPushButton {
                background-color: #e12807;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #ff3b1f;
            }
            QPushButton:pressed {
                background-color: #b31f06;
            }
        """)

        # Crea el layout principal
        layout = QVBoxLayout(self)

        # Mensaje de bienvenida
        self.label = QLabel("Configuracion Inicial:", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Primer ComboBox
        # Título y ComboBox para Cut-Off
        self.label_cutoff = QLabel("Cut-Off: ", self)
        layout.addWidget(self.label_cutoff)
        self.combo_cutoff = QComboBox(self)
        self.combo_cutoff.addItems(["0.25", "2.5", "0.08", "0.8"])
        layout.addWidget(self.combo_cutoff)

        # Segundo ComboBox
        # Título y ComboBox para Cuadros
        self.label_cuadros = QLabel("Cuadros: ", self)
        layout.addWidget(self.label_cuadros)
        self.combo_cuadros = QComboBox(self)
        self.combo_cuadros.addItems(["1", "2", "3", "4", "5"])
        layout.addWidget(self.combo_cuadros)

        # Botón OK centrado
        self.ok_button = QPushButton("OK", self)
        self.ok_button.setFixedWidth(100)
        self.ok_button.clicked.connect(self.on_ok_clicked)
        layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)

    def on_ok_clicked(self):
        # Leer los valores seleccionados
        self.selected_cutoff = self.combo_cutoff.currentText()
        self.selected_cuadros = self.combo_cuadros.currentText()
        self.accept()
    def closeEvent(self, event):
        event.accept()

class ProgressDialog(QDialog):
    def __init__(self, time, parent=None):
        super().__init__(parent)
        self.timeAlert = int(time)
        self.setWindowTitle("Procesando...")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setFixedSize(320, 160)

        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e1e;
                border: 3px solid #e12807;  /* Borde rojo brillante */
                border-radius: 12px;
            }
            QLabel {
                color: white;
                font-size: 16px;
                font-weight: bold;
            }
            QProgressBar {
                border: 1px solid #e12807;
                border-radius: 6px;
                background-color: #2a2a2a;
                height: 20px;
                text-align: center;
                color: white;
            }
            QProgressBar::chunk {
                background-color: #e12807;
                width: 24px;
            }
        """)

        # Layout principal
        layout = QVBoxLayout(self)

        # Etiqueta de mensaje
        self.label = QLabel("Generando gráfica...", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Barra de progreso en modo indeterminado
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 0)  # Modo indeterminado (barra animada)
        layout.addWidget(self.progress_bar)

        # Temporizador de cierre automático
        QTimer.singleShot(self.timeAlert, self.accept)

    def closeEvent(self, event):
        event.accept()
class Rugosimetro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_main = Interfaz()
        self.ui_main.setupUi(self)
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Rugosimetro Air Temp 1.0")
        self.filas = []
        self.Vv = 0
        self.Vh = 0
        self.cutOff = 0.8
        self.cuadros_X = 5

        # Actualiza el label de conexion con el puerto com
        self.ui_main.lb_statePortCom.setText(QCoreApplication.translate("MainWindow",
                                                                        f"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#e12807;\">DESCONECTADO</span></p></body></html>",
                                                                        None))

        self.spin_y_min = QSpinBox()
        self.spin_y_min.setRange(-1000, 1000)
        self.spin_y_min.setValue(-20)

        self.spin_y_max = QSpinBox()
        self.spin_y_max.setRange(-1000, 1000)
        self.spin_y_max.setValue(20)

        # Inicia apagado el indicador
        self.ui_main.radioButton.setChecked(False)
        self.ui_main.radioButton.setEnabled(False)

        # asigana por default 2 segmentos
        self.ui_main.comboBox_Secciones.setCurrentText("5")

        # Setea el toggle checkeado y deshabilitado
        self.ui_main.toggleButton.setChecked(True)
        self.ui_main.toggleButton.setEnabled(False)

        # Crear figura y axes
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Cambiar el fondo de la gráfica en Matplotlib
        self.figure.patch.set_facecolor("lightgray")
        self.ax.set_facecolor("lightgray")

        # Crear scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.canvas)

        # Obtener o crear layout del widget ya existente
        existing_layout = self.ui_main.widget.layout()
        if existing_layout is None:
            existing_layout = QVBoxLayout(self.ui_main.widget)
            self.ui_main.widget.setLayout(existing_layout)

        # Añadir toolbar y scroll area al layout (no agregues canvas directamente)
        existing_layout.addWidget(self.toolbar)
        existing_layout.addWidget(scroll_area)

        # Configuración del puerto serie (inicialmente desconectado)
        self.serial_port = None
        self.buffer_hex = ""

        # Timer para actualizar la lectura cada 100 ms
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_serial_data)

        # Actualizar puertos COM disponibles
        self.update_ports()

        # Deshabilitado al inicio
        self.ui_main.btn_printer.setVisible(False)
        self.ui_main.btn_Report.setVisible(False)
        self.ui_main.btn_Master.setVisible(False)

        # Variable para establecer el diametro de los puntos
        self.PontDiameter = 2

        # Variable para l separacion entre columnas
        self.spaceX = 5

        # Inicializa los Slot de la app
        self.initSlots()

        # Actualiza el grafico
        self.update_plot()

        # Mostrar el diálogo de bienvenida después de 1 segundo
        QTimer.singleShot(1000, self.show_welcome_dialog)

    @Slot()
    def initSlots(self):
        self.ui_main.btn_Report.clicked.connect(self.clear_plot)
        self.ui_main.btn_home.clicked.connect(self.connect_serial)
        self.ui_main.btn_printer.clicked.connect(self.disconnect_serial)
        self.ui_main.btn_Master.clicked.connect(self.save_data)
        self.ui_main.btn_DataMatrix.clicked.connect(self.load_data_from_file)
        self.ui_main.btn_configData.released.connect(self.clear_plot)
    def update_ports(self):
        """Actualizar los puertos COM disponibles en el ComboBox"""
        try:
            self.ui_main.comboBox_COM.clear()  # Limpiar ComboBox antes de agregar nuevos puertos
            available_ports = self.get_available_ports()
            self.ui_main.comboBox_COM.addItems(available_ports)
        except Exception as e:
            pass
    def show_welcome_dialog(self):
        dialog = WelcomeDialog(self)
        if dialog.exec() == QDialog.Accepted:
            print("Cut-Off seleccionado:", dialog.selected_cutoff)
            print("Cuadros seleccionado:", dialog.selected_cuadros)
            self.ui_main.comboBox_cutOff.setCurrentText(dialog.selected_cutoff)
            self.ui_main.comboBox_Secciones.setCurrentText(dialog.selected_cuadros)

    def get_available_ports(self):
        try:
            """Obtener una lista de puertos COM disponibles"""
            rs232_ports = []
            ports = serial.tools.list_ports.comports()

            for port in ports:
                # Se agregan dispositivos USB-Serial como CH340, CP210x, FTDI, etc.
                if any(x in port.description.upper() for x in ["RS-232", "SERIAL", "UART", "USB"]):
                    rs232_ports.append(port.device)

            return rs232_ports if rs232_ports else None
        except Exception as e:
            return None
    def connect_serial(self):
        """Conectar al puerto COM seleccionado y comenzar a leer los datos"""
        selected_port = self.ui_main.comboBox_COM.currentText()
        try:
            self.serial_port = serial.Serial(selected_port, 9600, timeout=1)  # Usar el puerto seleccionado
            self.serial_port.flush()
            #self.status_label.setText("Conectado")
            self.ui_main.lb_statePortCom.setText(QCoreApplication.translate("MainWindow",
                                                                    f"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#00aa00;\">CONECTADO</span></p></body></html>",
                                                                    None))

            self.ui_main.radioButton.setChecked(True)
            self.clear_plot()
            QMessageBox.information(self, "Puerto Conectado", "Se establecio conexion con el puerto COM.")


            # Muestra boton desconectar y esconde el conectar
            self.ui_main.btn_printer.setVisible(True)
            self.ui_main.btn_home.setVisible(False)

            # Botones laterales
            self.ui_main.btn_Report.setVisible(True)
            self.ui_main.btn_Master.setVisible(True)
            self.ui_main.btn_DataMatrix.setVisible(False)

            self.timer.start(80)  # Iniciar timer para leer datos del puerto serie
        except serial.SerialException as e:
            QMessageBox.warning(self, "Error", f"Error de conexion: {e}")
            #self.status_label.setText(f"Error de conexión: {e}")
    def disconnect_serial(self):
        """Desconectar del puerto COM"""
        if self.serial_port:
            self.serial_port.close()
            self.serial_port = None

            # Cambia el estado del label de conexion
            self.ui_main.lb_statePortCom.setText(QCoreApplication.translate("MainWindow",
                                                                            f"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; color:#e12807;\">DESCONECTADO</span></p></body></html>",
                                                                           None))
            # cambia el estado del indicador visua;
            self.ui_main.radioButton.setChecked(False)
            QMessageBox.warning(self, "Puerto Desconectado", "Se cerro conexion con el puerto COM.")

            # Muestra el boton conectar y esconde el desconectar
            self.ui_main.btn_printer.setVisible(False)
            self.ui_main.btn_home.setVisible(True)

            # Botones laterales
            self.ui_main.btn_Report.setVisible(False)
            self.ui_main.btn_Master.setVisible(False)
            self.ui_main.btn_DataMatrix.setVisible(True)

            self.timer.stop()  # Detener el timer para leer datos
        else:
            pass
            #self.ui_main.btn_printer.setEnabled(True)
    def clear_plot(self):
        """Borrar solo los datos de la gráfica sin desconectar el puerto COM"""
        self.ax.clear()
        self.filas = []  # Limpiar los datos
        self.buffer_hex = ""  # Limpiar el buffer de datos
        self.update_plot()  # Actualizar la gráfica a su estado vacío
    def read_serial_data(self):
        """Leer los datos del puerto serie y extraer valores Vv y Vh si están presentes"""
        if self.serial_port and self.serial_port.in_waiting > 0:
            try:
                raw_data = self.serial_port.read(self.serial_port.in_waiting)

                # Decodificar los datos como texto (ignorando errores)
                try:
                    decoded_data = raw_data.decode('utf-8', errors='ignore')
                    #print(f"[Texto recibido]: {decoded_data.strip()}")
                except UnicodeDecodeError:
                    decoded_data = ""
                    print("[Advertencia]: No se pudo decodificar como UTF-8")

                # Buscar coincidencias del tipo Vv: XX y Vh: XXX
                matches = re.findall(r'Vv:\s*(\d+)\s+Vh:\s*(\d+)', decoded_data)
                for vv, vh in matches:
                    # print(f"[Valores extraídos] Vv: {vv}, Vh: {vh}")
                    self.Vv= vv
                    self.Vh = vh

                    # Determina los rangos en X
                    RangoY = 42 / int(self.Vv)
                    Resolucion = (RangoY * 1000.00) / 128
                    LimiteSuperior = (RangoY / 2) * 1000
                    LimiteInferior = (-1) * (RangoY / 2) * 1000

                    # Actualiza el valor de la escala
                    self.spin_y_min.setValue(LimiteInferior)
                    self.spin_y_max.setValue(LimiteSuperior)


                # Procesar como bytes (mantener el análisis anterior)
                hex_data = raw_data.hex().upper()
                hex_pairs = " ".join([hex_data[i:i + 2] for i in range(0, len(hex_data), 2)])
                self.buffer_hex += " " + hex_pairs

                nuevas_filas = self.extract_data(self.buffer_hex)
                if nuevas_filas != self.filas:
                    self.filas = nuevas_filas
                    self.update_plot()

            except Exception as e:
                print(f"[Error al leer datos seriales]: {e}")
    def extract_data(self, byte_list):
        """Extraer y filtrar los datos de acuerdo al formato esperado"""
        hex_clean = re.findall(r'\b[0-9A-F]{2}\b', byte_list)
        byte_list = [int(h, 16) for h in hex_clean]
        datos = []
        i = 0
        while i < len(byte_list) - 3:
            # Buscar cabecera 1B 27 XX
            if byte_list[i] == 0x1B and byte_list[i + 1] == 0x27:
                i += 3  # Ignorar la cabecera
                fila = []
                while i < len(byte_list):
                    if byte_list[i] == 0x00:
                        break  # Fin de los datos
                    fila.append(byte_list[i])
                    i += 1
                datos.append(fila)
            else:
                i += 1
        return datos
    def update_plot(self):
        """Actualizar la gráfica con los nuevos datos"""
        self.ax.clear()

        if self.filas:
            for idx, fila in enumerate(self.filas):
                y_values = [p for p in fila if 0 <= p <= 129]
                self.ax.scatter([idx] * len(y_values), y_values, color="black", s=self.PontDiameter)

        self.ax.set_ylim(0, 129)

        ymin = self.spin_y_min.value()
        ymax = self.spin_y_max.value()

        # Eje Y
        n_div_y = 4
        tick_locs = [int(round(i * 129 / n_div_y)) for i in range(n_div_y + 1)]
        tick_labels = [round(ymin + (i * (ymax - ymin) / n_div_y)) for i in range(n_div_y + 1)]
        self.ax.set_yticks(tick_locs)
        self.ax.set_yticklabels(tick_labels)
        self.ax.set_ylabel("um (Micras)")

        num_filas = len(self.filas)
        self.ax.set_xlim(-1, num_filas)

        self.cuadros_X = int(self.ui_main.comboBox_Secciones.currentText())
        self.cutOff = float(self.ui_main.comboBox_cutOff.currentText())

        # Eje X
        n_div_x = self.cuadros_X
        x_start = 0  # Valor inicial
        x_step =self.cutOff  # Paso acumulativo para cada etiqueta

        if num_filas > 0:
            tick_x = [int(round(i * (num_filas - 1) / n_div_x)) for i in range(n_div_x + 1)]
            tick_labels_x = [round(x_start + i * x_step, 2) for i in range(n_div_x + 1)]

            self.ax.set_xticks(tick_x)
            self.ax.set_xticklabels(tick_labels_x)
        else:
            self.ax.set_xticks([])
            self.ax.set_xticklabels([])

        self.ax.set_xlabel("mm (Milímetros)")
        self.ax.set_title("Perfil")

        self.canvas.draw()

        # Ajuste del ancho del canvas según datos
        width_per_column = self.spaceX
        canvas_width = max(800, width_per_column * num_filas)
        self.canvas.setFixedWidth(canvas_width)
    def save_data(self):
        """Guardar los datos crudos del puerto serie en un archivo .txt"""
        if not self.buffer_hex.strip():
            QMessageBox.warning(self, "No hay datos", "No existen datos para guardar.")
            return

        # Abrir el diálogo para guardar el archivo
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar Datos Crudos", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.buffer_hex.strip())
                QMessageBox.information(self, "Datos guardados", "Los datos crudos se han guardado correctamente.")
            except Exception as e:
                QMessageBox.critical(self, "Error al guardar", f"No se pudo guardar el archivo: {e}")
    def load_data_from_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Seleccionar archivo de datos", "",
                                                   "Archivos de texto (*.txt)")

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    raw_data = file.read()

                # Separa y limpia los hexadecimales
                hex_values = raw_data.strip().split()
                bytes_data = bytes(int(h, 16) for h in hex_values)

                # Convierte a ASCII
                ascii_text = bytes_data.decode('ascii', errors='ignore')

                # Busca los valores con expresiones regulares
                vv_match = re.search(r'Vv:(\d+)', ascii_text)
                vh_match = re.search(r'Vh:(\d+)', ascii_text)

                vv_valor = vv_match.group(1) if vv_match else None
                vh_valor = vh_match.group(1) if vh_match else None

                print(f"Vv:{vv_valor}\nVh:{vh_valor}")

                RangoY=42/int(vv_valor)
                Resolucion=(RangoY*1000.00)/128
                LimiteSuperior = (RangoY/2)*1000
                LimiteInferior = (-1)*(RangoY/2)*1000

                # Actualiza el valor de la escala
                self.spin_y_min.setValue(LimiteInferior)
                self.spin_y_max.setValue(LimiteSuperior)


                # Quitar saltos de línea y asegurar que haya espacios entre los bytes
                hex_input = raw_data.replace('\n', ' ').replace('\r', ' ').strip()
                hex_input = ' '.join(hex_input.split())  # Normaliza los espacios

                #print("Hex input cargado correctamente:")
                #print(hex_input)  # solo muestra los primeros bytes para no saturar

                # Guardamos el resultado como atributo de la clase si lo necesitas luego
                self.hex_input = hex_input

                filas_limpias = self.extract_data(self.hex_input)
                self.filas = filas_limpias

                # Crear y mostrar el diálogo de progreso solo cuando se comienza a procesar
                progress_dialog = ProgressDialog(10000,self)
                progress_dialog.show()



                # Ejecutar la actualización de la gráfica en un hilo separado para evitar bloqueos
                QTimer.singleShot(2000, self.update_plot)  # 2000 milisegundos = 2 segundos

            except Exception as e:
                QMessageBox.critical(self, "Error al cargar archivo", f"No se pudo leer el archivo:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication([])
    window = Rugosimetro()
    window.show()
    app.exec()
