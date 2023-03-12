import sys 
from PyQt5.QtWidgets import *
from ui_modules.gbx_multi import * 

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())