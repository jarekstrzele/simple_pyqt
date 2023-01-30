import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First FORMLayout")

        # widgets
        self.ledFname = QLineEdit("Joe")
        self.ledLname = QLineEdit("SMith")
        self.dteStarted = QDateTimeEdit()
        self.spbAge = QSpinBox()
        self.btnSubmit = QPushButton("Submit")


        ## layout
        self.mainLayout = QFormLayout()
        self.mainLayout.setLabelAlignment(Qt.AlignRight) #doesn't work
        self.mainLayout.setRowWrapPolicy(QFormLayout.WrapLongRows) # doesn't work
        self.mainLayout.addRow("First Name: ", self.ledFname)
        self.mainLayout.addRow("Last Name: ", self.ledLname)
        self.mainLayout.addRow("Date starte", self.dteStarted)
        self.mainLayout.addRow("Age: ", self.spbAge)
        self.mainLayout.addRow("", self.btnSubmit)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("gtk+")
    main=Main()
 
    main.show()

    sys.exit(app.exec_())