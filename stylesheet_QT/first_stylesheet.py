import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Style Sheet")
        # for all elems in the container
        # self.setStyleSheet("background-color:red; border-radius: 3px; padding: 3px")

        sStyle="""
            QPushButton {
                background-color:blue;
                color: white ;
                border-radius: 3px;
                padding: 5px;
                margin: 10px;
            }

            QPushButton:default {
                background-color: red;
                color:white;
                border-radius: 5px;
                padding: 5px;
                margin: 10px;
            }
         

            QPushButton:default:hover {
                background-color:white;
                color: blue ;
                border-radius: 3px;
                border: 5px solid #000000;
                padding: 3px;
            }

            QPushButton:hover {
                background-color:green;
                color: white ;
                border-radius: 3px;
                border: 5px solid #000000;
                padding: 3px;
                
            }
        """

        self.setStyleSheet(sStyle)

        self.btn1 = QPushButton("Button 1")
        self.btn1.setDefault(True)
        self.btn2 = QPushButton("Button 2")
        self.btn3 = QPushButton("Button 3")
        self.btn3.setStyleSheet("background-color:orange; border-radius: 6px; border: 2 solid #000000; padding: 5px")
        # self.btn3.setDefault(True)

        self.lytMain = QVBoxLayout()
        self.lytMain.addWidget(self.btn1)
        self.lytMain.addWidget(self.btn2)
        self.lytMain.addWidget(self.btn3)

        self.setLayout(self.lytMain)

if __name__ == "__main__":
    app = QApplication([])
    main=Main()
    main.show()

    sys.exit(app.exec_())