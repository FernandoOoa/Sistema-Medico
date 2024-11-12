from PySide6.QtWidgets import QWidget, QMessageBox, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_VentanaPanelDoctor import Ui_Consultas
from typing import Dict, Union
import sqlite3
import sys


class VentanaPanelDoctor(QWidget, Ui_Consultas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
