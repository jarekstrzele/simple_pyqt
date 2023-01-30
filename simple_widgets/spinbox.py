import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spin box")

        self.spbInt = QSpinBox(self)
        self.spbInt.move(100,50)
        self.spbInt.setWrapping(True) # 0->99 , 99->0
        self.spbInt.setRange(0, 10000)
        self.spbInt.setSingleStep(200)
        self.spbInt.setValue(1000)
        self.spbInt.valueChanged.connect(self.evt_spbInt_valChanged)
        self.spbInt.editingFinished.connect(self.evt_spbInt_editingFinished)

        self.spbDouble = QDoubleSpinBox(self)
        self.spbDouble.move(100,80)
        self.spbDouble.setDecimals(5)
        self.spbDouble.setSingleStep(0.01)
        self.spbDouble.setPrefix("Latitude: ")
        self.spbDouble.setSuffix(chr(176))
        self.spbDouble.setRange(-90, 90)
        self.spbDouble.valueChanged.connect(self.evt_spbDble)

    def evt_spbDble(self, val):
        print(self.spbDouble.text())
        print(self.spbDouble.value())




    def evt_spbInt_valChanged(self, val):
        print(val, val % 200)
        if (val % 200):
            self.spbInt.setStyleSheet("color:red")
        else:
            self.spbInt.setStyleSheet("color:black")

    def evt_spbInt_editingFinished(self):
        QMessageBox.critical(self, "Invalid number", "Invalid value entered \n\nMust be divisible by 200" )
        self.spbInt.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main=Main()
    main.show()

    sys.exit(app.exec_())


