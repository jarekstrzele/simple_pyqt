from my_clacul import *
from PyQt5.QtWidgets import *
import exe_to_my_clacul

import sys

class Main(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    main=Main()
    main.show()

    sys.exit(app.exec_())

