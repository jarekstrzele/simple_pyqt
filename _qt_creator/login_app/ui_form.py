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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(409, 430)
        Dialog.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 30, 101, 41))
        self.label.setStyleSheet(u"color: rgb(255m255m255);\n"
"font-size: 30px;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 110, 61, 41))
        self.label_2.setStyleSheet(u"font-size:20px;\n"
"color: rgb(255, 0, 0)")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 110, 251, 31))
        self.lineEdit.setStyleSheet(u"font-size: 20px;\n"
"color: rgb(235, 235, 235)")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 160, 251, 31))
        self.lineEdit_2.setStyleSheet(u"font-size: 20px;\n"
"color: rgb(235, 235, 235)")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 160, 81, 41))
        self.label_3.setStyleSheet(u"font-size:20px;\n"
"color: rgb(255, 0, 0)")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 330, 111, 51))
        self.pushButton.setStyleSheet(u"font-size: 20px;\n"
"color: rgb(255, 255, 127)")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.lineEdit.setText("")
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Log in", None))
    # retranslateUi

