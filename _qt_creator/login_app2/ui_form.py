# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 624)
        Dialog.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 221, 61))
        font = QFont()
        font.setFamilies([u"Ravie"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 40px;\n"
"color: rgb(255, 85, 255);")
        self.btn_login = QPushButton(Dialog)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(270, 420, 131, 61))
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet(u"font-size: 20px;\n"
"border-radius: 10px;\n"
"background-color:rgb(0, 0, 0) ;\n"
"color: white;")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 130, 401, 241))
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

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"L o g i n", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.led_email.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.led_password.setText("")
    # retranslateUi

