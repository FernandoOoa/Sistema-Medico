# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaPanelDoctorSZmrgb.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)

class Ui_Consultas(object):
    def setupUi(self, Consultas):
        if not Consultas.objectName():
            Consultas.setObjectName(u"Consultas")
        Consultas.resize(609, 425)
        self.gridLayout = QGridLayout(Consultas)
        self.gridLayout.setObjectName(u"gridLayout")
        self.atenderBoton = QPushButton(Consultas)
        self.atenderBoton.setObjectName(u"atenderBoton")

        self.gridLayout.addWidget(self.atenderBoton, 7, 0, 1, 1)

        self.consultaAtendidaTabla = QTableView(Consultas)
        self.consultaAtendidaTabla.setObjectName(u"consultaAtendidaTabla")

        self.gridLayout.addWidget(self.consultaAtendidaTabla, 4, 0, 1, 1)

        self.label = QLabel(Consultas)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Consultas)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.consultaTabla = QTableView(Consultas)
        self.consultaTabla.setObjectName(u"consultaTabla")

        self.gridLayout.addWidget(self.consultaTabla, 2, 0, 1, 1)

        self.label_3 = QLabel(Consultas)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)


        self.retranslateUi(Consultas)

        QMetaObject.connectSlotsByName(Consultas)
    # setupUi

    def retranslateUi(self, Consultas):
        Consultas.setWindowTitle(QCoreApplication.translate("Consultas", u"Consultas", None))
        self.atenderBoton.setText(QCoreApplication.translate("Consultas", u"Atender", None))
        self.label.setText(QCoreApplication.translate("Consultas", u"Bienvenido Doctor", None))
        self.label_2.setText(QCoreApplication.translate("Consultas", u"Consultas por atender", None))
        self.label_3.setText(QCoreApplication.translate("Consultas", u"Consultas atendidas", None))
    # retranslateUi

