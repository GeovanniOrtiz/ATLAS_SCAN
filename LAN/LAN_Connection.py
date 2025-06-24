import subprocess
import platform
from PySide6.QtCore import QObject, QTimer, Signal, QThread


class WifiMonitor(QObject):
    connection_status_changed = Signal(bool)  # Señal para notificar cambios de conexión

    def __init__(self, ssid, password, adapter_description=None, interval=5000, parent=None):
        """
        Monitoriza la conexión a una red Wi-Fi específica y reconecta si es necesario.
        """
        super().__init__(parent)
        self.ssid = ssid
        self.password = password
        self.adapter_name = None

        if platform.system() == "Windows" and adapter_description:
            self.adapter_name = self.get_adapter_name_by_description(adapter_description)

        # Temporizador para iniciar la verificación periódica
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.start_check_thread)
        self.timer.start(interval)

        self.check_thread = None
        self.reconnect_thread = None

        # Verificación inicial
        self.start_check_thread()

    def get_adapter_name_by_description(self, description):
        """Busca el nombre de la interfaz de red (NetConnectionID) que tenga la descripción dada."""
        try:
            ps_command = (
                "Get-WmiObject Win32_NetworkAdapter "
                f"| Where-Object {{ $_.Description -eq '{description}' }} "
                "| Select-Object -ExpandProperty NetConnectionID"
            )
            result = subprocess.run(
                ["powershell", "-NoProfile", "-Command", ps_command],
                capture_output=True,
                text=True,
                timeout=10
            )
            name = result.stdout.strip()
            if name:
                print(f"Adaptador encontrado: '{name}' para descripción '{description}'")
                return name
            else:
                print(f"No se encontró adaptador para descripción '{description}'")
                return None
        except subprocess.TimeoutExpired:
            print("Timeout buscando adaptador.")
            return None
        except Exception as e:
            print(f"Error buscando adaptador: {e}")
            return None

    def start_check_thread(self):
        if self.check_thread and self.check_thread.isRunning():
            return
        self.check_thread = WifiCheckThread(self.ssid, self.adapter_name)
        self.check_thread.connection_checked.connect(self.handle_connection_status)
        self.check_thread.start()

    def handle_connection_status(self, connected):
        self.connection_status_changed.emit(connected)
        if not connected:
            print("Wi-Fi desconectado. Intentando reconectar...")
            self.start_reconnect_thread()

    def start_reconnect_thread(self):
        if self.reconnect_thread and self.reconnect_thread.isRunning():
            return
        self.reconnect_thread = WifiReconnectThread(self.ssid, self.password, self.adapter_name)
        self.reconnect_thread.connection_result.connect(self.connection_status_changed.emit)
        self.reconnect_thread.start()


class WifiCheckThread(QThread):
    connection_checked = Signal(bool)

    def __init__(self, ssid, interface_name=None, parent=None):
        super().__init__(parent)
        self.ssid = ssid
        self.interface_name = interface_name

    def run(self):
        connected = self.is_connected_to_wifi()
        self.connection_checked.emit(connected)

    def is_connected_to_wifi(self) -> bool:
        try:
            if platform.system() == "Windows":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                result = subprocess.run(
                    ["netsh", "wlan", "show", "interfaces"],
                    capture_output=True, text=True, timeout=4,
                    startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW
                )
                output = result.stdout
                if self.interface_name and self.interface_name not in output:
                    return False
                return f"SSID                   : {self.ssid}" in output

            elif platform.system() == "Linux":
                result = subprocess.run(["iwgetid", "-r"], capture_output=True, text=True, timeout=2)
                return result.stdout.strip() == self.ssid

            elif platform.system() == "Darwin":
                result = subprocess.run(
                    ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"],
                    capture_output=True, text=True, timeout=2
                )
                return self.ssid in result.stdout

        except subprocess.SubprocessError as e:
            print(f"Error verificando Wi-Fi: {e}")
            return False


class WifiReconnectThread(QThread):
    connection_result = Signal(bool)

    def __init__(self, ssid, password, interface_name=None, parent=None):
        super().__init__(parent)
        self.ssid = ssid
        self.password = password
        self.interface_name = interface_name

    def run(self):
        connected = self.connect_to_wifi()
        self.connection_result.emit(connected)

    def connect_to_wifi(self) -> bool:
        try:
            if platform.system() == "Windows":
                cmd = ["netsh", "wlan", "connect", f"name={self.ssid}"]
                if self.interface_name:
                    cmd.append(f"interface={self.interface_name}")

                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                subprocess.run(
                    cmd,
                    timeout=5,
                    startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW
                )

            elif platform.system() == "Linux":
                subprocess.run(["nmcli", "dev", "wifi", "connect", self.ssid, "password", self.password], timeout=5)

            elif platform.system() == "Darwin":
                subprocess.run(["networksetup", "-setairportnetwork", "en0", self.ssid, self.password], timeout=5)

            return WifiCheckThread(self.ssid, self.interface_name).is_connected_to_wifi()

        except subprocess.SubprocessError as e:
            print(f"Error reconectando Wi-Fi: {e}")
            return False
