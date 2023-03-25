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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(535, 639)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(10, 10, 10);\n"
"    margin: 5%;\n"
"}\n"
"\n"
"QListWidget{\n"
"  background-color: rgb(110, 110, 110);\n"
"  margin: 10%;\n"
"  font 12pt;\n"
"  border-radius: 5px;\n"
"  color: rgb(255, 252, 215);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(55, 152, 215);\n"
"color: rgb(222, 255, 254);\n"
"border-radius: 5px;\n"
"font: 15px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"   background-color: #1565C0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.todo_listWidget = QListWidget(self.centralwidget)
        self.todo_listWidget.setObjectName(u"todo_listWidget")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        self.todo_listWidget.setFont(font)
        self.todo_listWidget.setStyleSheet(u"")

        self.gridLayout.addWidget(self.todo_listWidget, 2, 0, 1, 2)

        self.btn_add_item = QPushButton(self.centralwidget)
        self.btn_add_item.setObjectName(u"btn_add_item")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_item.sizePolicy().hasHeightForWidth())
        self.btn_add_item.setSizePolicy(sizePolicy)
        self.btn_add_item.setMinimumSize(QSize(200, 40))
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_add_item.setFont(font1)
        self.btn_add_item.setStyleSheet(u"QPushButton::pressed {\n"
"   background-color: #1565C0;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color:rgb(0, 170, 155);\n"
"\n"
"border-color: rgb(0, 85, 0);\n"
"border-style: groove;\n"
"\n"
"color: rgb(250, 255, 194);\n"
"}")

        self.gridLayout.addWidget(self.btn_add_item, 1, 0, 1, 1)

        self.led_new_item = QLineEdit(self.centralwidget)
        self.led_new_item.setObjectName(u"led_new_item")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.led_new_item.sizePolicy().hasHeightForWidth())
        self.led_new_item.setSizePolicy(sizePolicy1)
        self.led_new_item.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(14)
        self.led_new_item.setFont(font2)
        self.led_new_item.setStyleSheet(u"color: rgb(250, 250, 250);\n"
"padding: 10px;")

        self.gridLayout.addWidget(self.led_new_item, 1, 1, 1, 1)

        self.btn_toggle = QPushButton(self.centralwidget)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy2)
        self.btn_toggle.setMinimumSize(QSize(0, 40))
        self.btn_toggle.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_toggle, 0, 0, 1, 2)

        self.btn_save_items = QPushButton(self.centralwidget)
        self.btn_save_items.setObjectName(u"btn_save_items")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_save_items.sizePolicy().hasHeightForWidth())
        self.btn_save_items.setSizePolicy(sizePolicy3)
        self.btn_save_items.setMinimumSize(QSize(250, 40))
        self.btn_save_items.setLayoutDirection(Qt.LeftToRight)
        self.btn_save_items.setStyleSheet(u"\n"
"QPushButton::pressed {\n"
"   background-color: #1565C0;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color:   rgb(36, 102, 24);\n"
"\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_save_items, 7, 1, 1, 1)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy4)
        self.btn_delete.setMinimumSize(QSize(0, 40))
        self.btn_delete.setMaximumSize(QSize(100, 16777215))
        self.btn_delete.setLayoutDirection(Qt.LeftToRight)
        self.btn_delete.setStyleSheet(u"QPushButton{\n"
"font:12px;\n"
"color: white;\n"
"background-color: rgb(130, 28, 78);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"   background-color: #1565C0;\n"
"}")

        self.gridLayout.addWidget(self.btn_delete, 7, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 535, 31))
        self.menumo_e_co = QMenu(self.menuBar)
        self.menumo_e_co.setObjectName(u"menumo_e_co")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menumo_e_co.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_add_item.setText(QCoreApplication.translate("MainWindow", u"Add a new item", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle all", None))
        self.btn_save_items.setText(QCoreApplication.translate("MainWindow", u"Save all items ", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete item(s)", None))
        self.menumo_e_co.setTitle(QCoreApplication.translate("MainWindow", u"mo\u017ce co\u015b", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

