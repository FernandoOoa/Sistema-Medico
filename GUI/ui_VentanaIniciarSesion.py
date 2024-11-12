# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaIniciarSesionFlCJRV.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 440)
        icon = QIcon()
        icon.addFile(u":/icons/icons/usuario.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color:#18062a  ;\n"
"	color: #000000;\n"
"\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"	color: white;\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"	border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 80, 255, 255),stop:1 rgba(105, 105, 255, 255));\n"
"	color: #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 2px;\n"
"	border-color: #c196ff;\n"
"	padding: 2px;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 148, 255, 255),stop:1 rgba(127, 127, 255, 255));\n"
"	color: #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 2px;\n"
"	border-color: #c196ff;\n"
"	padding: 2px;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed"
                        "\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(102, 26, 255, 255),stop:1 rgba(98, 98, 255, 255));\n"
"	color: #fff;\n"
"	border-width: 1px;\n"
"	border-radius: 2px;\n"
"	border-color: #c196ff;\n"
"	padding: 2px;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"	background-color: transparent;\n"
"	color: #b9b9bb;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #000;\n"
"    border: 1px solid #8b50ff;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"	background-color: #1f2b2b;\n"
"    border: 1px solid #8b50ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #8b50ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicato"
                        "r:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QListView-----*/\n"
"QListView \n"
"{\n"
"    border : none;\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"    outline: 0;\n"
"	font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::disabled \n"
"{\n"
"	background-color: #656565;\n"
"	color: #1b1b1b;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item \n"
"{\n"
"    padding: 1px;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:alternate \n"
"{\n"
"    background-color: #4a4b4d;\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected \n"
"{\n"
"    border: 1px solid #6a6ea9;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:selected:!active \n"
"{\n"
"    background-color: #45ffff;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QList"
                        "View::item:selected:active \n"
"{\n"
"    background-color: #45ffff;\n"
"    border: none;\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"\n"
"QListView::item:hover {\n"
"    background-color: #d4acff;\n"
"    border: none;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 80, 255, 255),stop:1 rgba(105, 105, 255, 255));\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 80, 255, 255),stop:1 rgba(105, 105, 255, 255));\n"
"    width: 14px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 80, 255, 255),stop:1 rgba(105, 105, 255, 255));\n"
"    width: 14px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 13px;\n"
"    margin: 16px 0 16px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread"
                        ":repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 80, 255, 255),stop:1 rgba(105, 105, 255, 255));\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 80, 255, 255),stop:1 rgba(105, 105, 255, 255));\n"
"    height: 14px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(139, 80, 255, 255),stop:1 rgba(105, 105, 255, 255));\n"
"    height: 14px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
""
                        "\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background-color: none;\n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 60, 131, 131))
        self.label.setPixmap(QPixmap(u":/icons/icons/usuario.png"))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(80, 230, 221, 71))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.emailLabel = QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.emailLabel)

        self.emailInput = QLineEdit(self.formLayoutWidget)
        self.emailInput.setObjectName(u"emailInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.emailInput)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordInput = QLineEdit(self.formLayoutWidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.passwordInput)

        self.loginButton = QPushButton(self.centralwidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(150, 370, 101, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.label.setText("")
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Correo:", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"example@example.com", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1234...", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
    # retranslateUi

