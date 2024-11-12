from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_VentanaCitaCRUD import Ui_Form
from datetime import datetime

class VentanaCitaCRUD(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Available appointment options
        self.statusComboBox.addItems(["Disponible", "No disponible"])

        connection = QSqlDatabase.addDatabase("QSQLITE")
        connection.setDatabaseName("databases/sistemamedico.db")
        if not connection.open():
            QMessageBox.critical(self, "ERROR", "No se pudo conectar a la base de datos")

        # Retrieving data from the "cita" table
        self.model = QSqlTableModel()
        self.model.setTable("cita")
        self.model.select()

        # Passing data to the table
        self.appointmentsTable.setModel(self.model)
        # Automatically resizing columns
        self.appointmentsTable.resizeColumnsToContents()
        # Hiding the Cita Id column in table
        self.appointmentsTable.setColumnHidden(0, True)

        # To make the table non-editable
        self.appointmentsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Changing the selection mode (from a single cell to an entire row)
        self.appointmentsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # To select an item at the row level
        self.appointmentsTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Signals
        self.appointmentsTable.selectionModel().selectionChanged.connect(self.select_row)
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
            
            office = self.model.index(self.row, 1).data() 
            data = self.model.index(self.row, 2).data() 
            status = self.model.index(self.row, 3).data() 

            self.officeInput.setText(str(office))
            self.dateInput.setText(data)
            self.statusComboBox.setCurrentText(status)


    def modify_row(self):
        # Retrieving values from inputs
        try:
            office = int(self.officeInput.text())
        except:
            QMessageBox.critical(self, "ERROR", "El consultorio debe ser un numero")
            self.officeInput.setText("")
            self.dateInput.setText("")
            return
        date = self.dateInput.text()
        status = self.statusComboBox.currentText()

        if len(date) > 0 and self.validate_date(date):
            # Defining the fields of the new row
            self.model.setData(self.model.index(self.row, 1), office)
            self.model.setData(self.model.index(self.row, 2), date)
            self.model.setData(self.model.index(self.row, 3), status)

            # Commiting model changes to the database
            self.model.submit()
        else:
            QMessageBox.critical(self, "ERROR", "No dejar vacio los campos o escribir fecha y hora correctamente")

        self.officeInput.setText("")
        self.dateInput.setText("")

    def create_row(self):
        # Retrieving values from inputs
        try:
            office = int(self.officeInput.text())
        except:
            QMessageBox.critical(self, "ERROR", "El consultorio debe ser un numero")
            self.officeInput.setText("")
            self.dateInput.setText("")
            return
        date = self.dateInput.text()
        status = self.statusComboBox.currentText()

        if len(date) > 0 and self.validate_date(date):
            # Creating a new row in the model
            new_row = self.model.rowCount()
            self.model.insertRow(new_row)

            # Defining the fields of the new row
            self.model.setData(self.model.index(new_row, 1), office)
            self.model.setData(self.model.index(new_row, 2), date)
            self.model.setData(self.model.index(new_row, 3), status)

            # Commiting model changes to the database
            self.model.submit()
        else:
            QMessageBox.critical(self, "ERROR", "No dejar vacio los campos o escribir fecha y hora correctamente")

        self.officeInput.setText("")
        self.dateInput.setText("")

    def remove_row(self):
        if self.row >= 0:
            self.model.removeRow(self.row)

            # Updating the table with the number that the model currently has after deleting a record
            self.model.select()

            self.row = -1

            self.officeInput.setText("")
            self.dateInput.setText("")

    def validate_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            return True 
        except ValueError:
            return False 