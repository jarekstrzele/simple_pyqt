# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_login.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 600)
        Dialog.setMinimumSize(QSize(500, 600))
        Dialog.setMaximumSize(QSize(500, 600))
        Dialog.setStyleSheet(u"background-color: rgb(57, 57, 85)")
        Dialog.setSizeGripEnabled(True)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 30, 221, 61))
        font = QFont()
        font.setFamilies([u"Ravie"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 40px;\n"
"color: rgb(255, 85, 255);")
        self.btn_login = QPushButton(Dialog)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(330, 420, 131, 61))
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	font-size: 20px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(66, 0, 99);\n"
"	color: white;\n"
"	padding: 10px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(34, 177, 32);\n"
"}")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 130, 481, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 225, 189);\n"
"font-size: 25px;")

        self.horizontalLayout.addWidget(self.label_2)

        self.led_email = QLineEdit(self.verticalLayoutWidget)
        self.led_email.setObjectName(u"led_email")
        self.led_email.setStyleSheet(u"color: rgb(255, 225, 189);\n"
"font-size: 25px;")

        self.horizontalLayout.addWidget(self.led_email)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 225, 189);\n"
"font-size: 25px;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.led_password = QLineEdit(self.verticalLayoutWidget)
        self.led_password.setObjectName(u"led_password")
        self.led_password.setStyleSheet(u"color: rgb(255, 225, 189);\n"
"font-size: 25px;\n"
"")

        self.horizontalLayout_2.addWidget(self.led_password)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 5)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 480, 171, 21))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_4.setFont(font1)
        self.btn_create_account = QPushButton(Dialog)
        self.btn_create_account.setObjectName(u"btn_create_account")
        self.btn_create_account.setGeometry(QRect(30, 510, 191, 41))
        self.btn_create_account.setFont(font)
        self.btn_create_account.setStyleSheet(u"QPushButton{\n"
"	font-size: 15px;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(23, 125, 136);\n"
"	color: white;\n"
"	padding: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(34, 177, 32);\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"L o g i n", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.led_email.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.led_password.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Don't have an accouint?", None))
        self.btn_create_account.setText(QCoreApplication.translate("Dialog", u"Create Account", None))
    # retranslateUi

