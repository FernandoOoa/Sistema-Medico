from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from ui_VentanaPanelSecretaria import Ui_Citas
import sqlite3


class VentanaPanelSecretaria(QWidget, Ui_Citas):
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

        # Configuración de la tabla de citas
        self.modelCitas = QSqlTableModel()
        self.modelCitas.setTable("cita")
        self.modelCitas.setFilter("estado = 'Disponible'")
        self.modelCitas.select()

        # Configuración de la tabla de pacientes
        self.modelPacientes = QSqlTableModel()
        self.modelPacientes.setTable("paciente")
        self.modelPacientes.select()

        # Configuración de la tabla de doctores
        self.modelDoctores = QSqlTableModel()
        self.modelDoctores.setTable("doctor")
        self.modelDoctores.select()

        # Configuración de la tabla de consultas
        self.modelConsultas = QSqlTableModel()
        self.modelConsultas.setTable("consulta")
        self.modelConsultas.select()

        # Configuracion visual para la tabla de consultas
        self.consultasGeneradasTable.setModel(self.modelConsultas)
        self.consultasGeneradasTable.resizeColumnsToContents()
        self.consultasGeneradasTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.consultasGeneradasTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.consultasGeneradasTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Configuración visual para la tabla de citas
        self.citasTable.setModel(self.modelCitas)
        self.citasTable.resizeColumnsToContents()
        self.citasTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.citasTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.citasTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Configuración visual para la tabla de pacientes
        self.pacientesTable.setModel(self.modelPacientes)
        self.pacientesTable.resizeColumnsToContents()
        self.pacientesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pacientesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pacientesTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Configuración visual para la tabla de doctores
        self.doctorTable.setModel(self.modelDoctores)
        self.doctorTable.resizeColumnsToContents()
        self.doctorTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.doctorTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.doctorTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Conectar la selección de la tabla de pacientes
        self.pacientesTable.selectionModel().selectionChanged.connect(self.filtrarCitas)
        self.pacientesTable.selectionModel().selectionChanged.connect(
            self.filtrarDoctores
        )

        # Conectar el botón guardar a la función guardarConsulta
        self.botonGuardar.clicked.connect(self.guardarConsulta)
        self.botonEliminar.clicked.connect(self.eliminarConsulta)

    def filtrarCitas(self):
        # Obtener el índice de la fila seleccionada en la tabla de pacientes
        selected_index = self.pacientesTable.selectionModel().currentIndex()
        if selected_index.isValid():
            # Obtener el valor de la columna 'consultorio' del paciente seleccionado
            consultorio_paciente = self.modelPacientes.data(
                self.modelPacientes.index(
                    selected_index.row(), self.modelPacientes.fieldIndex("consultorio")
                )
            )

            # Aplicar filtro en la tabla de citas para mostrar solo las citas en el mismo consultorio y que estén disponibles
            self.modelCitas.setFilter(
                f"consultorio = {consultorio_paciente} AND estado = 'Disponible'"
            )
        else:
            # Si no hay selección, mostrar todas las citas disponibles
            self.modelCitas.setFilter("estado = 'Disponible'")

    def filtrarDoctores(self):
        # Obtener el índice de la fila seleccionada en la tabla de pacientes
        selected_index = self.pacientesTable.selectionModel().currentIndex()
        if selected_index.isValid():
            # Obtener el valor de la columna 'consultorio' del paciente seleccionado
            consultorio_paciente = self.modelPacientes.data(
                self.modelPacientes.index(
                    selected_index.row(), self.modelPacientes.fieldIndex("consultorio")
                )
            )

            # Aplicar filtro en la tabla de doctores para mostrar solo los doctores en el mismo consultorio
            self.modelDoctores.setFilter(f"consultorio = {consultorio_paciente}")

    def eliminarConsulta(self):
        consulta_index = self.consultasGeneradasTable.selectionModel().currentIndex()
        cita_id = self.modelConsultas.data(
            self.modelConsultas.index(
                consulta_index.row(), self.modelConsultas.fieldIndex("cita_id")
            )
        )

        self.modelConsultas.removeRow(consulta_index.row())
        self.modelConsultas.select()

        connection = sqlite3.connect('databases/sistemamedico.db')
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE cita SET estado='Disponible' WHERE cita_id={cita_id};"
        )
        connection.commit()
        connection.close()
        self.modelCitas.select()

    def guardarConsulta(self):
        # Obtener la fila seleccionada en la tabla de citas
        cita_index = self.citasTable.selectionModel().currentIndex()
        if not cita_index.isValid():
            QMessageBox.warning(
                self, "Advertencia", "Seleccione una cita para guardar."
            )
            return

        # Obtener la fila seleccionada en la tabla de pacientes
        paciente_index = self.pacientesTable.selectionModel().currentIndex()
        if not paciente_index.isValid():
            QMessageBox.warning(
                self, "Advertencia", "Seleccione un paciente para la consulta."
            )
            return

        # Obtener la fila seleccionada en la tabla de doctores
        doctor_index = self.doctorTable.selectionModel().currentIndex()
        if not doctor_index.isValid():
            QMessageBox.warning(
                self, "Advertencia", "Seleccione un doctor para la consulta."
            )
            return

        # Obtener IDs de la cita, el paciente y el doctor seleccionados
        cita_id = self.modelCitas.data(
            self.modelCitas.index(
                cita_index.row(), self.modelCitas.fieldIndex("cita_id")
            )
        )
        paciente_id = self.modelPacientes.data(
            self.modelPacientes.index(
                paciente_index.row(), self.modelPacientes.fieldIndex("paciente_id")
            )
        )
        doctor_id = self.modelDoctores.data(
            self.modelDoctores.index(
                doctor_index.row(), self.modelDoctores.fieldIndex("doctor_id")
            )
        )

        connection = sqlite3.connect('databases/sistemamedico.db')
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE cita SET estado='No disponible' WHERE cita_id={cita_id};"
        )
        cursor.execute(
            f"INSERT INTO consulta(cita_id, doctor_id, paciente_id) VALUES ({cita_id}, {doctor_id}, {paciente_id});"
        )
        connection.commit()
        connection.close()


        # Refrescar el modelo para que actualice la vista
        self.modelCitas.select()
        self.modelConsultas.select()
        QMessageBox.information(self, "Éxito", "Consulta guardada exitosamente.")
