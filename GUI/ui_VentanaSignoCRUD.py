# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaSignoCRUDGdmxQq.ui'
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
        Form.resize(342, 332)
        icon = QIcon()
        icon.addFile(u":/icons/icons/signo-sintoma.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 341, 111))
        self.formLayoutWidget_2 = QWidget(self.groupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 321, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.signLabel = QLabel(self.formLayoutWidget_2)
        self.signLabel.setObjectName(u"signLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.signLabel)

        self.signInput = QLineEdit(self.formLayoutWidget_2)
        self.signInput.setObjectName(u"signInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.signInput)

        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 50, 321, 51))
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

        self.signsTable = QTableView(Form)
        self.signsTable.setObjectName(u"signsTable")
        self.signsTable.setGeometry(QRect(0, 110, 341, 221))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Signo CRUD", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Datos", None))
        self.signLabel.setText(QCoreApplication.translate("Form", u"Signo:", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Borrar", None))
        self.createButton.setText(QCoreApplication.translate("Form", u"Crear", None))
        self.modifyButton.setText(QCoreApplication.translate("Form", u"Modificar", None))
    # retranslateUi

