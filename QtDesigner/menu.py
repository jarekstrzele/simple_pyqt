import sys, os
from PyQt5.QtWidgets import *
from ui_modules.menu import *
import exe_to_my_clacul


class MainMenu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lyt_main = QHBoxLayout()
        self.centralwidget.setLayout(self.lyt_main)
        self.lyt_main.addWidget(self.splitter)

        self.actionOpen.triggered.connect(self.evt_open_triggered)
        self.actionQuit.triggered.connect(self.evt_quit_triggered)
        self.actionAbout_menu.triggered.connect(self.evt_help_triggered)

    def evt_help_triggered(self):
        mycal= exe_to_my_clacul.Main()
        mycal.show()
        mycal.exec_()
       

      
        self.prg = QProgressBar()
        self.prg.setValue(43)
        self.prg.setStyle(QStyleFactory.create("Window"))
        # self.statusbar.addWidget(self.prg)
        self.statusbar.addPermanentWidget(self.prg)

        self.listWidget.addItems(os.listdir("ui_modules/"))
        self.listWidget.itemDoubleClicked.connect(self.evt_lst_dbl)

    def evt_lst_dbl(self, lwi):

        # QMessageBox.information(self, "File", f"you selected {lwi.text()}")
        try:
            f = open("ui_modules/"+lwi.text())
            self.plainTextEdit.setPlainText(f.read())
        except PermissionError:
            self.statusbar.showMessage("I can't open that file", 2500)


  

    def evt_quit_triggered(self):
        sys.exit(0)    

    def evt_open_triggered(self):
        sFile, sFilter = QFileDialog.getOpenFileName(self, "Open", "ui/", "Any file (*.*)")
        if sFile:
            f = open(sFile)
            self.plainTextEdit.setPlainText(f.read())
        else:
            print("Canceld by user")

if __name__ == "__main__":
    app = QApplication([])
    mainMenu = MainMenu()
    mainMenu.show()

    sys.exit(app.exec_())