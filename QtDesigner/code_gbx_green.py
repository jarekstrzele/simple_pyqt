import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from ui_modules.gbx_multi import *

class DlgMain(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # in this line you import all from gbx_multi.py 

        self.rbtCheckTrue.toggled.connect(self.evt_rbtCHeckTrue_toggle)

    def evt_rbtCHeckTrue_toggle(self, chk):
        print(chk)

if __name__ == "__main__":
    app = QApplication([])
    dlgMain = DlgMain()
    dlgMain.show() 

    sys.exit(app.exec_())




