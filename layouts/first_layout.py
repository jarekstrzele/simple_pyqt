import sys 
from PyQt5.QtWidgets import *


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Layout")

        ## widgets
        self.lbl1 = QLabel("FIrst lable")
        self.btn2 = QPushButton("BTN 2")
        self.led3 = QLineEdit("Line Edit 3")
        self.cmb4 = QComboBox()
        self.cmb4.addItems(["utem 1", "item2", "item 3"])

        ## layout
        self.mainLayout = QHBoxLayout()
        #self.mainLayout = QVBoxLayout()
        # .addWidget(object, number_that_indicates_how_many_place_takes_that_widget)
        self.mainLayout.addWidget(self.lbl1, 20)
        self.mainLayout.addWidget(self.btn2, 10)
        
        self.mainLayout.addWidget(self.led3, 10)
        self.mainLayout.addWidget(self.cmb4, 20)
        self.mainLayout.addStretch(4)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("gtk+")
    main=Main()
 
    main.show()

    sys.exit(app.exec_())