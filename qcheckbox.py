import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox")
        self.resize(200,200)

        self.chkEnable = QCheckBox("Enable", self)
        self.chkEnable.move(30,40)
        self.chkEnable.setChecked(True)
        # event/signal handler/slot
        self.chkEnable.toggled.connect(self.evt_handler)

        # three state checkbox
        self.chkThree = QCheckBox("Three State", self)
        self.chkThree.move(30,70)
        self.chkThree.setTristate(True)
        self.chkThree.stateChanged.connect(self.evt_three_handler)


        self.lbl = QLabel("Some text", self)
        self.lbl.move(40,100)
        self.lbl.resize(100,100)
        font=QFont("Times New Roman", 15,75, True)
        self.lbl.setFont(font)

    def evt_handler(self, chkd):
        if chkd:
            self.lbl.setDisabled(False)
        else:
            self.lbl.setDisabled(True)

    def evt_three_handler(self, state):
        print(state)
        if state == 0:
            QMessageBox.information(self, "State", "UnChecked")
        elif state == 2:
            QMessageBox.information(self, "State", "Checked")
        else:
            QMessageBox.information(self, "State", "Partially checked")


if __name__=="__main__":
    app = QApplication(sys.argv)
    main=DlgMain()
    main.show()

    sys.exit(app.exec_())

