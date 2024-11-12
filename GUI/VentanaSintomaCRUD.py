from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_VentanaSintomaCRUD import Ui_Form
from typing import Dict, Union


class VentanaSintomaCRUD(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        connection = QSqlDatabase.addDatabase("QSQLITE")
        connection.setDatabaseName("databases/sistemamedico.db")
        if not connection.open():
            QMessageBox.critical(self, "ERROR", "No se pudo conectar a la base de datos")

        # Retrieving data from the "doctor" table
        self.model = QSqlTableModel()
        self.model.setTable("sintoma")
        self.model.select()

        # Passing data to the table
        self.symptomsTable.setModel(self.model)
        # Automatically resizing columns
        self.symptomsTable.resizeColumnsToContents()
        # Hiding the Doctor Id column in table
        self.symptomsTable.setColumnHidden(0, True)

        # To make the table non-editable
        self.symptomsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Changing the selection mode (from a single cell to an entire row)
        self.symptomsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # To select an item at the row level
        self.symptomsTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Signals
        self.symptomsTable.selectionModel().selectionChanged.connect(self.select_row)
        self.modifyButton.clicked.connect(self.modify_row)
        self.createButton.clicked.connect(self.create_row)
        self.removeButton.clicked.connect(self.remove_row)

        self.row = -1

    # Slots
    def select_row(self, selection):
        # Is there anything selected?
        if selection.indexes():
            # Retrieving the index of the current row being selected
            self.row = selection.indexes()[0].row()
            
            symptom = self.model.index(self.row, 1).data() # 0 refers to the "id" field, so we never use the value "0"

            self.symptomInput.setText(symptom)


    def modify_row(self):
        # Retrieving values from inputs
        symptom = self.symptomInput.text()

        if len(symptom) > 0:
            # Writting data into the model .index(index of row, index of column)
            self.model.setData(self.model.index(self.row, 1), symptom)

            # Commiting model changes to the database
            self.model.submit()
            self.symptomInput.setText("")
        else:
            QMessageBox.critical(self, "ERROR", "No dejar vacio el campo")

    def create_row(self):
        # Retrieving values from inputs
        symptom = self.symptomInput.text()

        if len(symptom) > 0:
            # Creating a new row in the model
            new_row = self.model.rowCount()
            self.model.insertRow(new_row)

            # Defining the fields of the new row
            self.model.setData(self.model.index(new_row, 1), symptom)

            # Commiting model changes to the database
            self.model.submit()
            self.symptomInput.setText("")

    def remove_row(self):
        if self.row >= 0:
            self.model.removeRow(self.row)

            # Updating the table with the number that the model currently has after deleting a record
            self.model.select()

            self.row = -1

            self.symptomInput.setText("")

