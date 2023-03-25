import sys 
from PyQt5.uic import loadUi 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication 


class MainWindow(QDialog):
   

    def gotoScreen2(self):
        self.screen2=Screen2()
        widget.addWidget(self.screen2)

        # widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setCurrentWidget(self.screen2)


class Screen2(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("screen_2.ui", self)

        self.btn_1.clicked.connect(self.gotoScreen2)

    def gotoScreen1(self):
       self.screen2=Screen2()
       widget.addWidget(self.screen2)

        # widget.setCurrentIndex(widget.currentIndex()+1)
       widget.setCurrentWidget(self.screen2)


class Screen2(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("screen_2.ui", self)

        self.btn_2.clicked.connect(self.gotoScreen1)

    def gotoScreen1(self):
        mainwindow=MainWindow()
        widget.addWidget(mainWindow)
        widget.addWidget(mainwindow)
        
        widget.setCurrentIndex(widget.currentIndex()+1)





app =QApplication([])
widget=QtWidgets.QStackedWidget()
mainWindow = MainWindow()

widget.addWidget(mainWindow)

widget.setFixedHeight(400)
widget.setFixedWidth(300)
widget.show()

sys.exit(app.exec_())







