from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_VentanaPanelDoctor import Ui_Consultas
import sqlite3


class VentanaPanelDoctor(QWidget, Ui_Consultas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conexión a la base de datos
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("databases/sistemamedico.db")
        if not self.db.open():
            QMessageBox.critical(
                self, "ERROR", "No se pudo conectar a la base de datos"
            )
            return

        # Configuración de la tabla de consultas pendientes
        self.modelCitasPendientes = QSqlTableModel()
        self.modelCitasPendientes.setTable("consulta")
        self.modelCitasPendientes.setFilter("estado = 'Pendiente'")
        self.modelCitasPendientes.select()

        # Configuracion visual para la tabla de consultas pendientes
        self.consultaTabla.setModel(self.modelCitasPendientes)
        self.consultaTabla.resizeColumnsToContents()
        self.consultaTabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.consultaTabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.consultaTabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Configuración de la tabla de citas pendientyes
        self.modelCitasAtendidas = QSqlTableModel()
        self.modelCitasAtendidas.setTable("historial")
        self.modelCitasAtendidas.select()

        # Configuracion visual para la tabla de consultas
        self.consultaAtendidaTabla.setModel(self.modelCitasAtendidas)
        self.consultaAtendidaTabla.resizeColumnsToContents()
        self.consultaAtendidaTabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.consultaAtendidaTabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.consultaAtendidaTabla.setSelectionBehavior(QAbstractItemView.SelectRows)
