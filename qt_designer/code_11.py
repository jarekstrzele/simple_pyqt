# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.evt_clicked())
        self.btn.setGeometry(QtCore.QRect(232, 340, 311, 101))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(250, 90, 251, 91))
        self.lbl.setLocale(QtCore.QLocale(QtCore.QLocale.Polish, QtCore.QLocale.Poland))
        self.lbl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def evt_clicked(self):
        self.lbl.setText("BBOOOOO!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Click me"))
        self.lbl.setText(_translate("MainWindow", "Something"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
