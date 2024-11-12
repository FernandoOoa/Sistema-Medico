# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaDoctorCRUDYvNhlp.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(756, 483)
        icon = QIcon()
        icon.addFile(u"icons/equipo-medico.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 701, 211))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(30, 20, 311, 181))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.fullnameLabel = QLabel(self.formLayoutWidget)
        self.fullnameLabel.setObjectName(u"fullnameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fullnameLabel)

        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.emailLabel)

        self.telephoneLabel = QLabel(self.formLayoutWidget)
        self.telephoneLabel.setObjectName(u"telephoneLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.telephoneLabel)

        self.OfficeLabel = QLabel(self.formLayoutWidget)
        self.OfficeLabel.setObjectName(u"OfficeLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.OfficeLabel)

        self.fullnameInput = QLineEdit(self.formLayoutWidget)
        self.fullnameInput.setObjectName(u"fullnameInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fullnameInput)

        self.emailInput = QLineEdit(self.formLayoutWidget)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.emailInput)

        self.telephoneInput = QLineEdit(self.formLayoutWidget)
        self.telephoneInput.setObjectName(u"telephoneInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.telephoneInput)

        self.officeInput = QLineEdit(self.formLayoutWidget)
        self.officeInput.setObjectName(u"officeInput")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.officeInput)

        self.specialtyLabel = QLabel(self.formLayoutWidget)
        self.specialtyLabel.setObjectName(u"specialtyLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.specialtyLabel)

        self.professionalLicenseLabel = QLabel(self.formLayoutWidget)
        self.professionalLicenseLabel.setObjectName(u"professionalLicenseLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.professionalLicenseLabel)

        self.specialtyInput = QLineEdit(self.formLayoutWidget)
        self.specialtyInput.setObjectName(u"specialtyInput")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.specialtyInput)

        self.professionalLicenseInput = QLineEdit(self.formLayoutWidget)
        self.professionalLicenseInput.setObjectName(u"professionalLicenseInput")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.professionalLicenseInput)

        self.formLayoutWidget_2 = QWidget(self.groupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(350, 20, 321, 51))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stateLabel = QLabel(self.formLayoutWidget_2)
        self.stateLabel.setObjectName(u"stateLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.stateLabel)

        self.stateInput = QLineEdit(self.formLayoutWidget_2)
        self.stateInput.setObjectName(u"stateInput")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.stateInput)

        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(350, 80, 321, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.removeButton = QPushButton(self.horizontalLayoutWidget)
        self.removeButton.setObjectName(u"removeButton")

        self.horizontalLayout.addWidget(self.removeButton)

        self.createButton = QPushButton(self.horizontalLayoutWidget)
        self.createButton.setObjectName(u"createButton")

        self.horizontalLayout.addWidget(self.createButton)

        self.modifyButton = QPushButton(self.horizontalLayoutWidget)
        self.modifyButton.setObjectName(u"modifyButton")

        self.horizontalLayout.addWidget(self.modifyButton)

        self.doctorsTable = QTableView(Form)
        self.doctorsTable.setObjectName(u"doctorsTable")
        self.doctorsTable.setGeometry(QRect(30, 240, 701, 221))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Doctor CRUD", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Datos", None))
        self.fullnameLabel.setText(QCoreApplication.translate("Form", u"Nombre:", None))
        self.emailLabel.setText(QCoreApplication.translate("Form", u"Correo:", None))
        self.telephoneLabel.setText(QCoreApplication.translate("Form", u"Telefono:", None))
        self.OfficeLabel.setText(QCoreApplication.translate("Form", u"Consultorio:", None))
        self.specialtyLabel.setText(QCoreApplication.translate("Form", u"Especialidad:", None))
        self.professionalLicenseLabel.setText(QCoreApplication.translate("Form", u"Cedula Profesional:", None))
        self.stateLabel.setText(QCoreApplication.translate("Form", u"Estado:", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.createButton.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.modifyButton.setText(QCoreApplication.translate("Form", u"Modificar", None))
    # retranslateUi

