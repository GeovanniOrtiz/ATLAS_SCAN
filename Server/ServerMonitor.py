import socket
import time

from PySide6.QtCore import QObject, Signal, Slot, QTimer, QThread
import requests
import subprocess
import platform

class ConnectionMonitor(QThread):
    connection_status_changed = Signal(bool)  # Señal para notificar cambios

    def __init__(self, host="10.1.0.187", port=8086, interval=5, parent=None):
        """
        Clase que monitorea la conexión a un servidor sin bloquear la GUI.

        Args:
            host (str): IP o dominio del servidor.
            port (int): Puerto del servidor.
            interval (int): Intervalo de chequeo en segundos (por defecto 5 segundos).
        """
        super().__init__(parent)
        self.host = host
        self.port = port
        self.interval = interval
        self.last_status = None
        self.running = True  # Control de ejecución del hilo

    def run(self):
        """Ejecuta la verificación de conexión en un bucle sin bloquear la GUI."""
        while self.running:
            status = self.is_server_reachable(self.host, self.port)

            if status != self.last_status:  # Emitir señal solo si hay un cambio
                self.last_status = status
                self.connection_status_changed.emit(status)

            time.sleep(self.interval)  # Esperar antes de la siguiente verificación

    def stop(self):
        """Detiene el monitoreo de conexión de manera segura."""
        self.running = False
        self.quit()
        self.wait()

    def is_server_reachable(self, host, port, timeout=3):
        """
        Verifica si el servidor está accesible sin bloquear la GUI.

        Returns:
            bool: True si el servidor está disponible, False en caso contrario.
        """
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except (socket.timeout, socket.error):
            return False

    def pingIP(self, ip: str) -> bool:
        """Realiza un ping a la dirección IP dada y devuelve True si hay comunicación."""
        param = "-n" if platform.system().lower() == "windows" else "-c"
        comando = ["ping", param, "1", ip]

        try:
            resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
            return resultado.returncode == 0
        except Exception as e:
            print(f"Error al hacer ping: {e}")
            return False