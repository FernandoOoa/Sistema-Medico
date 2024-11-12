# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPanelSecretariamQtEMM.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableView, QWidget)
import resources_rc

class Ui_Citas(object):
    def setupUi(self, Citas):
        if not Citas.objectName():
            Citas.setObjectName(u"Citas")
        Citas.resize(887, 540)
        icon = QIcon()
        icon.addFile(u":/icons/icons/Secretaria.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Citas.setWindowIcon(icon)
        self.label = QLabel(Citas)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 10, 121, 21))
        self.pacientesTable = QTableView(Citas)
        self.pacientesTable.setObjectName(u"pacientesTable")
        self.pacientesTable.setGeometry(QRect(20, 60, 441, 131))
        self.citasTable = QTableView(Citas)
        self.citasTable.setObjectName(u"citasTable")
        self.citasTable.setGeometry(QRect(20, 390, 441, 131))
        self.doctorTable = QTableView(Citas)
        self.doctorTable.setObjectName(u"doctorTable")
        self.doctorTable.setGeometry(QRect(20, 220, 441, 141))
        self.botonEliminar = QPushButton(Citas)
        self.botonEliminar.setObjectName(u"botonEliminar")
        self.botonEliminar.setGeometry(QRect(710, 310, 75, 24))
        self.botonGuardar = QPushButton(Citas)
        self.botonGuardar.setObjectName(u"botonGuardar")
        self.botonGuardar.setGeometry(QRect(560, 310, 75, 24))
        self.consultasGeneradasTable = QTableView(Citas)
        self.consultasGeneradasTable.setObjectName(u"consultasGeneradasTable")
        self.consultasGeneradasTable.setGeometry(QRect(480, 60, 381, 181))
        self.tituloTablaPacientesLabel = QLabel(Citas)
        self.tituloTablaPacientesLabel.setObjectName(u"tituloTablaPacientesLabel")
        self.tituloTablaPacientesLabel.setGeometry(QRect(20, 40, 101, 16))
        self.label_2 = QLabel(Citas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 200, 101, 16))
        self.label_3 = QLabel(Citas)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 370, 81, 16))
        self.label_4 = QLabel(Citas)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(480, 40, 161, 16))

        self.retranslateUi(Citas)

        QMetaObject.connectSlotsByName(Citas)
    # setupUi

    def retranslateUi(self, Citas):
        Citas.setWindowTitle(QCoreApplication.translate("Citas", u"Consultas", None))
        self.label.setText(QCoreApplication.translate("Citas", u"Registro de Consultas", None))
        self.botonEliminar.setText(QCoreApplication.translate("Citas", u"Eliminar", None))
        self.botonGuardar.setText(QCoreApplication.translate("Citas", u"Guardar", None))
        self.tituloTablaPacientesLabel.setText(QCoreApplication.translate("Citas", u"Lista de pacientes:", None))
        self.label_2.setText(QCoreApplication.translate("Citas", u"Lista de doctores:", None))
        self.label_3.setText(QCoreApplication.translate("Citas", u"Lista de citas:", None))
        self.label_4.setText(QCoreApplication.translate("Citas", u"Lista de consultas generadas:", None))
    # retranslateUi

