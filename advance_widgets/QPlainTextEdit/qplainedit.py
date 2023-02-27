import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainEdit")

        self.ted=QPlainTextEdit("This nest was surveu for 4 consecutive yuear wfwofi wekom fwef")

        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.ted)

        self.setLayout(self.lyt_main)

        



if __name__=="__main__":
    app=QApplication([])
    main=Main()
    main.show()

    sys.exit(app.exec_())