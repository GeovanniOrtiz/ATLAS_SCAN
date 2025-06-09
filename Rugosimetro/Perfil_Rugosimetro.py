import sys
import serial
import re
import matplotlib.pyplot as plt
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QHBoxLayout, QLabel, QSpinBox, QScrollArea, QPushButton, QComboBox, QFileDialog, QMessageBox, QDialog
)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

# Crear el dialogo de progreso
class ProgressDialog(QDialog):
    def __init__(self, time, parent=None):
        super().__init__(parent)
        self.timeAlert = int(time)
        self.setWindowTitle("PROCESANDO")

        # Crear un layout y una etiqueta
        layout = QVBoxLayout()
        self.label = QLabel("Generando gráfica...", self)
        layout.addWidget(self.label)

        # Establecer el layout del diálogo
        self.setLayout(layout)

        # Configurar el temporizador para cerrar el diálogo después de 2 segundos
        QTimer.singleShot(self.timeAlert, self.accept)  # Cierra el diálogo después de 2 segundos

    def closeEvent(self, event):
        # Cerrar el diálogo cuando termine el temporizador
        event.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Perfil de Datos")
        self.filas = []
        self.Vv=0
        self.Vh=0
        self.cutOff=0.8
        self.cuadros_X=5

        # Configuración de la interfaz
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Sección de Control
        control_layout = QHBoxLayout()
        #control_layout.addWidget(QLabel("Y mínimo:"))
        self.spin_y_min = QSpinBox()
        self.spin_y_min.setRange(-1000, 1000)
        self.spin_y_min.setValue(-20)
        #control_layout.addWidget(self.spin_y_min)

        #control_layout.addWidget(QLabel("Y máximo:"))
        self.spin_y_max = QSpinBox()
        self.spin_y_max.setRange(-1000, 1000)
        self.spin_y_max.setValue(20)
        #control_layout.addWidget(self.spin_y_max)

        #self.spin_y_min.valueChanged.connect(self.update_plot)
        #self.spin_y_max.valueChanged.connect(self.update_plot)

        main_layout.addLayout(control_layout)

        self.infolabels_layout = QHBoxLayout()
        self.labelDeltaY = QLabel()
        deltaY = 0.25
        self.labelDeltaY.setText(f"Resolucion en eje Y: {deltaY} Um/Punto")

        self.labelDeltaX = QLabel()
        deltaX = 0.25
        self.labelDeltaX.setText(f"Resolucion en eje X: {deltaX} Um/Punto")
        self.infolabels_layout.addWidget(self.labelDeltaY)
        self.infolabels_layout.addWidget(self.labelDeltaX)

        self.configure_layout = QHBoxLayout()

        # Crea las posibles configuraciones de CutOff
        self.CutOFF_select = QComboBox()
        self.CutOFF_select.addItems(["0.08", "0.8","0.25", "2.5"])

        # Crea las posibles configuraciones de CutOff
        self.Num_Cuadros_select = QComboBox()
        self.Num_Cuadros_select.addItems(["1", "2", "3", "4", "5"])
        self.configure_layout.addWidget((QLabel("CutOff:")))
        self.configure_layout.addWidget(self.CutOFF_select)
        self.configure_layout.addWidget((QLabel("Total de Cuadros:")))
        self.configure_layout.addWidget(self.Num_Cuadros_select)

        main_layout.addLayout(self.configure_layout)


        # Sección de Conexión del Puerto Serie
        self.connection_layout = QHBoxLayout()

        # ComboBox para seleccionar el puerto COM
        self.port_combo = QComboBox()
        self.update_ports()  # Actualizar puertos COM disponibles
        self.connection_layout.addWidget(QLabel("Puerto COM:"))
        self.connection_layout.addWidget(self.port_combo)

        # Indicador de conexión
        self.status_label = QLabel("Desconectado")
        self.connection_layout.addWidget(self.status_label)

        # Botones de Conectar y Desconectar
        self.connect_button = QPushButton("Conectar")
        self.connect_button.clicked.connect(self.connect_serial)
        self.connection_layout.addWidget(self.connect_button)

        self.disconnect_button = QPushButton("Desconectar")
        self.disconnect_button.clicked.connect(self.disconnect_serial)
        self.disconnect_button.setEnabled(False)  # Deshabilitado al inicio
        self.connection_layout.addWidget(self.disconnect_button)

        # Botón para borrar la gráfica
        self.clear_button = QPushButton("Borrar Gráfica")
        self.clear_button.clicked.connect(self.clear_plot)
        self.connection_layout.addWidget(self.clear_button)

        # Botón para guardar los datos en un archivo .txt
        self.save_button = QPushButton("Guardar Datos")
        self.save_button.clicked.connect(self.save_data)
        self.connection_layout.addWidget(self.save_button)

        # Botón para cargar y graficar datos desde archivo
        self.load_button = QPushButton("Cargar y Graficar Datos")
        self.load_button.clicked.connect(self.load_data_from_file)
        self.connection_layout.addWidget(self.load_button)

        main_layout.addLayout(self.connection_layout)
        main_layout.addLayout(self.infolabels_layout)

        # Gráfico
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.canvas)

        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(scroll_area)

        # Configuración del puerto serie (inicialmente desconectado)
        self.serial_port = None
        self.buffer_hex = ""

        # Timer para actualizar la lectura cada 100 ms
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_serial_data)

        # Variable para establecer el diametro de los puntos
        self.PontDiameter=2

        # Variable para l separacion entre columnas
        self.spaceX=5


    def update_ports(self):
        """Actualizar los puertos COM disponibles en el ComboBox"""
        self.port_combo.clear()  # Limpiar ComboBox antes de agregar nuevos puertos
        available_ports = self.get_available_ports()
        self.port_combo.addItems(available_ports)

    def get_available_ports(self):
        """Obtener una lista de puertos COM disponibles"""
        ports = []
        for i in range(256):  # Comprobar puertos del 0 al 255
            try:
                port = f"COM{i}"
                serial.Serial(port)  # Intentar abrir el puerto
                ports.append(port)
            except (OSError, serial.SerialException):
                continue  # Si no se puede abrir, ignorar el puerto
        return ports

    def connect_serial(self):
        """Conectar al puerto COM seleccionado y comenzar a leer los datos"""
        selected_port = self.port_combo.currentText()
        try:
            self.serial_port = serial.Serial(selected_port, 9600, timeout=1)  # Usar el puerto seleccionado
            self.serial_port.flush()
            self.status_label.setText("Conectado")
            self.connect_button.setEnabled(False)
            self.disconnect_button.setEnabled(True)
            self.timer.start(80)  # Iniciar timer para leer datos del puerto serie
        except serial.SerialException as e:
            self.status_label.setText(f"Error de conexión: {e}")

    def disconnect_serial(self):
        """Desconectar del puerto COM"""
        if self.serial_port:
            self.serial_port.close()
            self.serial_port = None
            self.status_label.setText("Desconectado")
            self.connect_button.setEnabled(True)
            self.disconnect_button.setEnabled(False)
            self.timer.stop()  # Detener el timer para leer datos

    def clear_plot(self):
        """Borrar solo los datos de la gráfica sin desconectar el puerto COM"""
        self.ax.clear()
        self.filas = []  # Limpiar los datos
        self.buffer_hex = ""  # Limpiar el buffer de datos
        self.update_plot()  # Actualizar la gráfica a su estado vacío

    def read_serial_data_last(self):
        """Leer los datos del puerto serie"""
        if self.serial_port and self.serial_port.in_waiting > 0:
            raw_data = self.serial_port.read(self.serial_port.in_waiting)
            print(raw_data)
            hex_data = raw_data.hex().upper()
            hex_pairs = " ".join([hex_data[i:i + 2] for i in range(0, len(hex_data), 2)])
            self.buffer_hex += " " + hex_pairs

            nuevas_filas = self.extraer_datos(self.buffer_hex)

            if nuevas_filas != self.filas:
                self.filas = nuevas_filas
                self.update_plot()

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

                nuevas_filas = self.extraer_datos(self.buffer_hex)
                if nuevas_filas != self.filas:
                    self.filas = nuevas_filas
                    self.update_plot()

            except Exception as e:
                print(f"[Error al leer datos seriales]: {e}")

    def extraer_datos(self, byte_list):
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

    def update_plot_last(self):
        """Actualizar la gráfica con los nuevos datos"""
        self.ax.clear()

        if self.filas:
            for idx, fila in enumerate(self.filas):
                # Los valores en Y deben estar entre 0 y 129
                y_values = [p for p in fila if 0 <= p <= 129]
                self.ax.scatter([idx] * len(y_values), y_values, color="black", s=self.PontDiameter)

        self.ax.set_ylim(0, 129)

        ymin = self.spin_y_min.value()
        ymax = self.spin_y_max.value()

        # Dividir en 5 segmentos (6 puntos) el eje Y
        n_div = 5
        tick_locs = [int(round(i * 129 / n_div)) for i in range(n_div + 1)]
        tick_labels = [
            round(ymin + (i * (ymax - ymin) / n_div)) for i in range(n_div + 1)
        ]

        self.ax.set_yticks(tick_locs)
        self.ax.set_yticklabels(tick_labels)
        self.ax.set_ylabel("um (Micras)")

        num_filas = len(self.filas)
        self.ax.set_xlim(-1, num_filas + 1)
        self.ax.set_xlabel("mm (Milímetros)")
        self.ax.set_title("Perfil")

        self.ax.set_xticklabels([])  # Borra las etiquetas del eje X

        self.canvas.draw()

        # Ajuste del ancho del canvas según datos
        width_per_column = self.spaceX
        canvas_width = max(800, width_per_column * num_filas)
        self.canvas.setFixedWidth(canvas_width)

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

        self.cuadros_X = int(self.Num_Cuadros_select.currentText())
        self.cutOff = float(self.CutOFF_select.currentText())

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

                filas_limpias = self.extraer_datos(self.hex_input)
                self.filas = filas_limpias

                # Crear y mostrar el diálogo de progreso solo cuando se comienza a procesar
                progress_dialog = ProgressDialog(7000,self)
                progress_dialog.show()

                # Ejecutar la actualización de la gráfica en un hilo separado para evitar bloqueos
                QTimer.singleShot(2000, self.update_plot)  # 2000 milisegundos = 2 segundos

            except Exception as e:
                QMessageBox.critical(self, "Error al cargar archivo", f"No se pudo leer el archivo:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
