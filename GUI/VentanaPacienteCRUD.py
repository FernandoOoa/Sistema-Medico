from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_VentanaPacienteCRUD import Ui_Form


class VentanaPacienteCRUD(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
        connection = QSqlDatabase.addDatabase("QSQLITE")
        connection.setDatabaseName("databases/sistemamedico.db")
        if not connection.open():
            QMessageBox.critical(self, "ERROR", "No se pudo conectar a la base de datos")

        # Retrieving data from the "doctor" table
        self.model = QSqlTableModel()
        self.model.setTable("paciente")
        self.model.select()

        # Passing data to the table
        self.patientsTable.setModel(self.model)
        # Automatically resizing columns
        self.patientsTable.resizeColumnsToContents()
        # Hiding the Doctor Id column in table
        self.patientsTable.setColumnHidden(0, True)

        # To make the table non-editable
        self.patientsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Changing the selection mode (from a single cell to an entire row)
        self.patientsTable.setSelectionMode(QAbstractItemView.SingleSelection)
        # To select an item at the row level
        self.patientsTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Signals
        self.patientsTable.selectionModel().selectionChanged.connect(self.select_row)
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

            fullname = self.model.index(self.row, 1).data()
            email = self.model.index(self.row, 2).data()
            telephone = self.model.index(self.row, 3).data()
            address = self.model.index(self.row, 4).data()
            blood_type = self.model.index(self.row, 5).data()
            office = self.model.index(self.row, 6).data()
            state = self.model.index(self.row, 7).data()

            self.fullnameInput.setText(fullname)
            self.emailInput.setText(email)
            self.telephoneInput.setText(telephone)
            self.addressInput.setText(address)
            self.bloodTypeInput.setText(blood_type)
            self.officeInput.setText(str(office))
            self.stateInput.setText(state)


    def modify_row(self):
        # Retrieving values from inputs
        fullname = self.fullnameInput.text()
        email = self.emailInput.text()
        telephone = self.telephoneInput.text()
        address = self.addressInput.text()
        blood_type = self.bloodTypeInput.text()
        office = 0
        try: 
            office = int(self.officeInput.text())
        except:
            QMessageBox.critical(self, "ERROR", "El consultorio debe ser un numero")
            self.fullnameInput.setText("")
            self.emailInput.setText("")
            self.telephoneInput.setText("")
            self.addressInput.setText("")
            self.bloodTypeInput.setText("")
            self.officeInput.setText("")
            self.stateInput.setText("")
            return
        state = self.stateInput.text()

        if len(fullname) > 0 and len(email) > 0 and len(telephone) > 0 and len(address) > 0 and len(blood_type) > 0 and len(state) > 0:
            # Writting data into the model .index(index of row, index of column)
            self.model.setData(self.model.index(self.row, 1), fullname)
            self.model.setData(self.model.index(self.row, 2), email)
            self.model.setData(self.model.index(self.row, 3), telephone)
            self.model.setData(self.model.index(self.row, 4), address)
            self.model.setData(self.model.index(self.row, 5), blood_type)
            self.model.setData(self.model.index(self.row, 6), office)
            self.model.setData(self.model.index(self.row, 7), state)

            # Commiting model changes to the database
            self.model.submit()
        else: 
            QMessageBox.critical(self, "ERROR", "Completar todos los campos")

        self.fullnameInput.setText("")
        self.emailInput.setText("")
        self.telephoneInput.setText("")
        self.addressInput.setText("")
        self.bloodTypeInput.setText("")
        self.officeInput.setText("")
        self.stateInput.setText("")

    def create_row(self):
        # Retrieving values from inputs
        fullname = self.fullnameInput.text()
        email = self.emailInput.text()
        telephone = self.telephoneInput.text()
        address = self.addressInput.text()
        blood_type = self.bloodTypeInput.text()
        office = 0
        try: 
            office = int(self.officeInput.text())
        except:
            QMessageBox.critical(self, "ERROR", "El consultorio debe ser un numero")
            self.fullnameInput.setText("")
            self.emailInput.setText("")
            self.telephoneInput.setText("")
            self.addressInput.setText("")
            self.bloodTypeInput.setText("")
            self.officeInput.setText("")
            self.stateInput.setText("")
            return
        state = self.stateInput.text()

        if len(fullname) > 0 and len(email) > 0 and len(telephone) > 0 and len(address) > 0 and len(blood_type) > 0 and len(state) > 0:
            # Creating a new row in the model
            new_row = self.model.rowCount()
            self.model.insertRow(new_row)

            # Defining the fields of the new row
            self.model.setData(self.model.index(new_row, 1), fullname)
            self.model.setData(self.model.index(new_row, 2), email)
            self.model.setData(self.model.index(new_row, 3), telephone)
            self.model.setData(self.model.index(new_row, 4), address)
            self.model.setData(self.model.index(new_row, 5), blood_type)
            self.model.setData(self.model.index(new_row, 6), office)
            self.model.setData(self.model.index(new_row, 7), state)

            # Commiting model changes to the database
            self.model.submit()
            self.fullnameInput.setText("")
            self.emailInput.setText("")
            self.telephoneInput.setText("")
            self.addressInput.setText("")
            self.bloodTypeInput.setText("")
            self.officeInput.setText("")
            self.stateInput.setText("")

    def remove_row(self):
        if self.row >= 0:
            self.model.removeRow(self.row)

            # Updating the table with the number that the model currently has after deleting a record
            self.model.select()

            self.row = -1

            self.fullnameInput.setText("")
            self.emailInput.setText("")
            self.telephoneInput.setText("")
            self.addressInput.setText("")
            self.bloodTypeInput.setText("")
            self.officeInput.setText("")
            self.stateInput.setText("")



