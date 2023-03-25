# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen_2.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(253, 413)
        self.btn_2 = QPushButton(Dialog)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(20, 20, 191, 81))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 160, 131, 51))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"screen 2", None))
        self.btn_2.setText(QCoreApplication.translate("Dialog", u"go to screen 1", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SCREEN 2", None))
    # retranslateUi

