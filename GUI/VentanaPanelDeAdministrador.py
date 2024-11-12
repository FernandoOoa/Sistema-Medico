from PySide6.QtWidgets import QWidget
from ui_VentanaPanelDeAdministrador import Ui_Form 
from VentanaPacienteCRUD import VentanaPacienteCRUD
from VentanaEnfermedadCRUD import VentanaEnfermedadCRUD
from VentanaDoctorCRUD import VentanaDoctorCRUD
from VentanaSintomaCRUD import VentanaSintomaCRUD
from VentanaSignoCRUD import VentanaSignoCRUD
from VentanaCitaCRUD import VentanaCitaCRUD
from typing import Dict, Union
import sqlite3
import sys


class VentanaPanelDeAdministrador(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logged_in_user_information: Dict[Union[str, int], Union[str, int]] = dict()

        # Optional windows
        self.ventana_doctor_crud = VentanaDoctorCRUD()
        self.ventana_paciente_crud = VentanaPacienteCRUD()
        self.ventana_signo_crud = VentanaSignoCRUD()
        self.ventana_sintoma_crud = VentanaSintomaCRUD()

        # Signal
        self.logoutButton.clicked.connect(self.close)
        self.doctorcrudButton.clicked.connect(self.show_doctor_crud)
        self.pacientecrudButton.clicked.connect(self.show_patient_crud)
        self.signocrudButton.clicked.connect(self.show_sign_crud)
        self.sintomacrudButton.clicked.connect(self.show_symptom_crud)
        self.enfermedadcrudButton.clicked.connect(self.show_disease_crud)
        self.citascrudButton.clicked.connect(self.show_appointment_crud)

    # Slot
    def show_doctor_crud(self):
        self.ventana_doctor_crud.show()

    def show_patient_crud(self):
        self.ventana_paciente_crud.show()

    def show_sign_crud(self):
        self.ventana_signo_crud.show()

    def show_symptom_crud(self):
        self.ventana_sintoma_crud.show()

    def show_disease_crud(self):
        self.ventana_enfermedad_crud = VentanaEnfermedadCRUD()
        self.ventana_enfermedad_crud.show()

    def show_appointment_crud(self):
        self.ventana_cita_crud = VentanaCitaCRUD()
        self.ventana_cita_crud.show()