from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_VentanaIniciarSesion import Ui_MainWindow
from VentanaPanelDeAdministrador import VentanaPanelDeAdministrador
from typing import Optional, Tuple
import sqlite3
import sys



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Iniciar Sesion")

        # Optional Windows
        self.ventana_panel_de_administrador = VentanaPanelDeAdministrador()

        # Signal
        self.loginButton.clicked.connect(self.login)

    # Slot
    def login(self):
        email = self.emailInput.text()
        password = self.passwordInput.text()

        if " " in email or " " in password:
            QMessageBox.critical(self, "ERROR", "No insertar espacios")
            return
        if len(email) == 0 or len(password) == 0:
            QMessageBox.critical(self, "ERROR", "Completa todos los campos")
            return
        
        statement = f"SELECT * FROM user_auth WHERE correo = '{email}' AND password = '{password}';"
        authenticated_user = self.query(statement)

        if authenticated_user is None:
            QMessageBox.critical(self, "ERROR", "Usuario no registrado")
            return
        
        match authenticated_user[3]:
            case "Administrador":
                self.ventana_panel_de_administrador.logged_in_user_information = {
                    "user_id": authenticated_user[0],
                    "user_email": authenticated_user[1],
                    "user_password": authenticated_user[2],
                    "user_type": authenticated_user[3]
                }
                self.ventana_panel_de_administrador.show()
                self.close()
            case "Doctor":
                pass
            case "Recepcion":
                pass
            case _:
                pass

    def query(self, statement: str) -> Optional[Tuple[str, int]]:
        connection = sqlite3.connect('databases/sistemamedico.db')
        cursor = connection.cursor()
        response = cursor.execute(statement)
        
        authenticated_user = response.fetchone()
        connection.close()
        
        return authenticated_user

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
