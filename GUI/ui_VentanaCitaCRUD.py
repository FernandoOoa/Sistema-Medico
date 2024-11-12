# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaCitaCRUDJZesbN.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableView, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 407)
        icon = QIcon()
        icon.addFile(u":/icons/icons/cita.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 341, 171))
        self.formLayoutWidget_2 = QWidget(self.groupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 321, 80))
        self.formLayout = QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.officeLabel = QLabel(self.formLayoutWidget_2)
        self.officeLabel.setObjectName(u"officeLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.officeLabel)

        self.officeInput = QLineEdit(self.formLayoutWidget_2)
        self.officeInput.setObjectName(u"officeInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.officeInput)

        self.dateLabel = QLabel(self.formLayoutWidget_2)
        self.dateLabel.setObjectName(u"dateLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dateLabel)

        self.dateInput = QLineEdit(self.formLayoutWidget_2)
        self.dateInput.setObjectName(u"dateInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateInput)

        self.statusLabel = QLabel(self.formLayoutWidget_2)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.statusLabel)

        self.statusComboBox = QComboBox(self.formLayoutWidget_2)
        self.statusComboBox.setObjectName(u"statusComboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.statusComboBox)

        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 110, 321, 51))
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

        self.appointmentsTable = QTableView(Form)
        self.appointmentsTable.setObjectName(u"appointmentsTable")
        self.appointmentsTable.setGeometry(QRect(10, 180, 341, 221))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cita CRUD", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Datos", None))
        self.officeLabel.setText(QCoreApplication.translate("Form", u"Consultorio:", None))
        self.dateLabel.setText(QCoreApplication.translate("Form", u"Fecha:", None))
        self.dateInput.setPlaceholderText(QCoreApplication.translate("Form", u"YYYY-MM-DD HH:MM:SS", None))
        self.statusLabel.setText(QCoreApplication.translate("Form", u"Estado:", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.createButton.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.modifyButton.setText(QCoreApplication.translate("Form", u"Modificar", None))
    # retranslateUi

