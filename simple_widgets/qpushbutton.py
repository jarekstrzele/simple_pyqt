# QPushButton inherits from QAbstratButton and that inherits from QWidget
# methods
#   setIcon(QIcon)
#   setText(str)
#   setAutoRepeat(bool), setAutoRepeatDelay(msec), setAutoRepeatInterval
# signals
#   clicked
# QPushButton(str, parent)
#   setFlat(bool), setDefault(bool)

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPixmap

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PushButton")
        self.resize(200,200)

        self.btn = QPushButton("Disable Label", self)
        self.btn.setIcon(QIcon(QPixmap("images/face-icon.png")))
        self.btn.move(40,40)
        self.btn.resize(120,50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.lbl = QLabel("Sme text", self)
        self.lbl.move(30,100)
        self.lbl.resize(100,100)
        font = QFont("Times New Roman",  11,75,True)
        self.lbl.setFont(font)
    
    def evt_btn_clicked(self):
        if self.lbl.isEnabled():
            self.lbl.setDisabled(True)
            self.repaint()
            self.btn.setText("Enable label")
            self.btn.repaint()
        else:
            self.lbl.setDisabled(False)
            self.lbl.repaint()
            self.btn.setText("Disable label")
            self.btn.repaint()



if __name__ == "__main__":
    app = QApplication([])
    main = DlgMain()
    main.show()

    sys.exit(app.exec_())






