from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_VentanaEnfermedadCRUD import Ui_Form
from PySide6.QtCore import Qt
import sqlite3


class VentanaEnfermedadCRUD(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        connection = QSqlDatabase.addDatabase("QSQLITE")
        connection.setDatabaseName("databases/sistemamedico.db")
        if not connection.open():
            QMessageBox.critical(self, "ERROR", "No se pudo conectar a la base de datos")

        self.signModel = QSqlTableModel()
        self.signModel.setTable("signo")
        self.signModel.select()
        self.signModel.setHeaderData(0, Qt.Horizontal, "Id")
        self.signModel.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.signsTable.setModel(self.signModel)
        self.signsTable.resizeColumnsToContents()
        self.signsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.signsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.signsTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.symptomModel = QSqlTableModel()
        self.symptomModel.setTable("sintoma")
        self.symptomModel.select()
        self.symptomModel.setHeaderData(0, Qt.Horizontal, "Id")
        self.symptomModel.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.symptomsTable.setModel(self.symptomModel)
        self.symptomsTable.resizeColumnsToContents()
        self.symptomsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.symptomsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.symptomsTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.diseaseModel = QSqlTableModel()
        self.diseaseModel.setTable("enfermedad")
        self.diseaseModel.select()
        self.diseaseModel.setHeaderData(0, Qt.Horizontal, "Id")
        self.diseaseModel.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.diseaseModel.setHeaderData(2, Qt.Horizontal, "Tratamiento")
        self.diseaseModel.setHeaderData(3, Qt.Horizontal, "Signo Id")
        self.diseaseModel.setHeaderData(4, Qt.Horizontal, "Sintoma Id")
        self.diseasesTable.setModel(self.diseaseModel)
        self.diseasesTable.resizeColumnsToContents()
        self.diseasesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.diseasesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.diseasesTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.diseasesTable.selectionModel().selectionChanged.connect(self.select_diseases_table_row)
        self.signsTable.selectionModel().selectionChanged.connect(self.select_signs_table_row)
        self.symptomsTable.selectionModel().selectionChanged.connect(self.select_symptoms_table_row)

        self.row = -1 # Refers to the row in the disease table
        self.sign = None
        self.symptom = None

        self.createButton.clicked.connect(self.create_row)
        self.modifyButton.clicked.connect(self.modify_row)
        self.removeButton.clicked.connect(self.remove_row)

    def select_signs_table_row(self, selection):
        if selection.indexes():
            row = selection.indexes()[0].row()
            self.sign = (
                self.signModel.index(row, 0).data(),
                self.signModel.index(row, 1).data()
            )

    def select_symptoms_table_row(self, selection):
        if selection.indexes():
            row = selection.indexes()[0].row()
            self.symptom = (
                self.symptomModel.index(row, 0).data(),
                self.symptomModel.index(row, 1).data()
            )

    def select_diseases_table_row(self, selection):
        if selection.indexes():
            self.row = selection.indexes()[0].row()

            disease = self.diseaseModel.index(self.row, 1).data()
            treatment = self.diseaseModel.index(self.row, 2).data()

            self.diseaseInput.setText(disease)
            self.treatmentInput.setText(treatment)

    def modify_row(self):
        disease = self.diseaseInput.text()
        treatment = self.treatmentInput.toPlainText()
        sign_id = self.sign[0] if self.sign is not None else -1
        symptom_id = self.symptom[0] if self.symptom is not None else -1

        if len(disease) > 0 and len(treatment) > 0 and sign_id != -1 and symptom_id != -1:
            self.diseaseModel.setData(self.diseaseModel.index(self.row, 1), disease)
            self.diseaseModel.setData(self.diseaseModel.index(self.row, 2), treatment)
            self.diseaseModel.setData(self.diseaseModel.index(self.row, 3), sign_id)
            self.diseaseModel.setData(self.diseaseModel.index(self.row, 4), symptom_id)
            self.diseaseModel.submit()

        else:
            QMessageBox.critical(self, "ERROR", "Llenar todos los campos y/o seleccionar signo y sintoma")

        self.diseaseInput.setText("")
        self.treatmentInput.setText("")
        self.signsTable.clearSelection()
        self.symptomsTable.clearSelection()

    def create_row(self):
        disease = self.diseaseInput.text()
        treatment = self.treatmentInput.toPlainText()
        sign_id = self.sign[0] if self.sign is not None else -1
        symptom_id = self.symptom[0] if self.symptom is not None else -1

        if len(disease) > 0 and len(treatment) > 0 and sign_id != -1 and symptom_id != -1:
            new_row = self.diseaseModel.rowCount()
            self.diseaseModel.insertRow(new_row)

            self.diseaseModel.setData(self.diseaseModel.index(new_row, 1), disease)
            self.diseaseModel.setData(self.diseaseModel.index(new_row, 2), treatment)
            self.diseaseModel.setData(self.diseaseModel.index(new_row, 3), sign_id)
            self.diseaseModel.setData(self.diseaseModel.index(new_row, 4), symptom_id)
            self.diseaseModel.submit()

        else:
            QMessageBox.critical(self, "ERROR", "Llenar todos los campos y/o seleccionar signo y sintoma")

        self.diseaseInput.setText("")
        self.treatmentInput.setText("")
        self.signsTable.clearSelection()
        self.symptomsTable.clearSelection()

    def remove_row(self):
        if self.row >= 0:
            self.diseaseModel.removeRow(self.row)
            self.diseaseModel.select()
            self.row = -1

            self.diseaseInput.setText("")
            self.treatmentInput.setText("")
            self.signsTable.clearSelection()
            self.symptomsTable.clearSelection()

