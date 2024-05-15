from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, \
    QHBoxLayout

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Iniciar Sesión")

        # Crear widgets para el formulario de inicio de sesión
        self.label_user = QLabel("Usuario:")
        self.label_password = QLabel("Contraseña:")
        self.lineedit_user = QLineEdit()
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)  # Ocultar la contraseña
        self.button_login = QPushButton("Iniciar Sesión")
        self.button_loginC = QPushButton("Cancelar")

        # Diseño del formulario usando un diseño vertical
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_user)
        layout.addWidget(self.lineedit_user)
        layout.addWidget(self.label_password)
        layout.addWidget(self.lineedit_password)
        layout2 = QHBoxLayout(self)
        layout2.addWidget(self.button_login)
        layout2.addWidget(self.button_loginC)
        layout.addLayout(layout2)

        # Conectar el botón de inicio de sesión a la función correspondiente
        self.button_login.clicked.connect(self.try_login)
        self.button_loginC.clicked.connect(lambda :self.reject())

    def try_login(self):
        # Obtener el usuario y la contraseña ingresados
        username = self.lineedit_user.text()
        password = self.lineedit_password.text()

        # Aquí puedes realizar la validación del usuario y contraseña
        if username == "Atlas2024" and password == "180220":
            # Ejemplo simple de validación: solo imprimir los valores ingresados
            print(f"Usuario: {username}, Contraseña: {password}")
            # Cerrar el cuadro de diálogo después de iniciar sesión
            self.accept()
        else:
            QMessageBox.information(None, "Usuario Invalido", "Usuario o Contraseña Incorrectos")


if __name__ == "__main__":
    app = QApplication([])
    login_dialog = LoginDialog()
    login_dialog.exec()
