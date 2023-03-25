# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen_1.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 391)
        self.btn_1 = QPushButton(Dialog)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(84, 280, 131, 61))
        self.btn_1.setStyleSheet(u"border-radius: 10px;\n"
"\n"
"background-color:rgb(85, 255, 0);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"screen_1", None))
        self.btn_1.setText(QCoreApplication.translate("Dialog", u"go to screen 2", None))
    # retranslateUi

