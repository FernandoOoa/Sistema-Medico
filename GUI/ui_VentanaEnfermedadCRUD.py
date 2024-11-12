# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaEnfermedadCRUDHoMESh.ui'
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
    QSizePolicy, QTableView, QTextEdit, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 506)
        icon = QIcon()
        icon.addFile(u":/icons/icons/enfermedad.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 331, 271))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 311, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.diseaseLabel = QLabel(self.formLayoutWidget)
        self.diseaseLabel.setObjectName(u"diseaseLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.diseaseLabel)

        self.diseaseInput = QLineEdit(self.formLayoutWidget)
        self.diseaseInput.setObjectName(u"diseaseInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.diseaseInput)

        self.treatmentLabel = QLabel(self.formLayoutWidget)
        self.treatmentLabel.setObjectName(u"treatmentLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.treatmentLabel)

        self.treatmentInput = QTextEdit(self.formLayoutWidget)
        self.treatmentInput.setObjectName(u"treatmentInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.treatmentInput)

        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 160, 311, 80))
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

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(350, 0, 401, 271))
        self.verticalLayoutWidget = QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 371, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.signsLabel = QLabel(self.verticalLayoutWidget)
        self.signsLabel.setObjectName(u"signsLabel")

        self.verticalLayout.addWidget(self.signsLabel)

        self.signsTable = QTableView(self.verticalLayoutWidget)
        self.signsTable.setObjectName(u"signsTable")

        self.verticalLayout.addWidget(self.signsTable)

        self.symptomsLabel = QLabel(self.verticalLayoutWidget)
        self.symptomsLabel.setObjectName(u"symptomsLabel")

        self.verticalLayout.addWidget(self.symptomsLabel)

        self.symptomsTable = QTableView(self.verticalLayoutWidget)
        self.symptomsTable.setObjectName(u"symptomsTable")

        self.verticalLayout.addWidget(self.symptomsTable)

        self.diseasesTable = QTableView(Form)
        self.diseasesTable.setObjectName(u"diseasesTable")
        self.diseasesTable.setGeometry(QRect(10, 280, 741, 221))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Enfermedades CRUD", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Datos", None))
        self.diseaseLabel.setText(QCoreApplication.translate("Form", u"Enfermedad:", None))
        self.treatmentLabel.setText(QCoreApplication.translate("Form", u"Tratamiento:", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.createButton.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.modifyButton.setText(QCoreApplication.translate("Form", u"Modificar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Signos y Sintomas", None))
        self.signsLabel.setText(QCoreApplication.translate("Form", u"Signos:", None))
        self.symptomsLabel.setText(QCoreApplication.translate("Form", u"Sintomas:", None))
    # retranslateUi

