import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCombobox")

        self.cmbStates = QComboBox(self)
        self.cmbStates.move(50,50)

        # self.cmbStates.addItems(['Al', 'AR', 'Ma', 'Mo', 'Mi']) # you can have the same values in the list

        
        # self.cmbStates.addItem("Alabama", "AL")
        # self.cmbStates.addItem("Alaska", "AK")
        # self.cmbStates.addItem("Michigan", "MI")
        # self.cmbStates.addItem("Minnesota", "MN")
        # self.cmbStates.addItem("Missouri", "MI")
        # self.cmbStates.currentTextChanged.connect(self.evt_cmbStates_changed)
        # self.cmbStates.currentIndexChanged.connect(self.evt_cmbStates_changed)

        # instead of string for idx, you can use any data type
        # for example we use dictionery; 'ab' abbreviation, 'pop' - population
        self.cmbStates.addItem("Alabama", {"ab":"AL", "pop":40000})
        self.cmbStates.addItem("Alaska", {"ab":"AK", "pop":50000})
        self.cmbStates.addItem("Michigan", {"ab":"MI", "pop":70000})
        self.cmbStates.addItem("Minnesota", {"ab":"MN", "pop":30000})
        self.cmbStates.addItem("Missouri", {"ab":"MO", "pop":100000})
        self.cmbStates.currentIndexChanged.connect(self.evt_cmbStates_changed)
        self.cmbStates.highlighted.connect(self.evt_cmbStates_highligted)

        self.lblPop = QLabel("Population: 40000", self)
        self.lblPop.move(180, 55)


    # When you .currentTextChanged.connect
    # def evt_cmbStates_changed(self, txt):
    #     QMessageBox.information(self, "Combobox", f"you selected {txt}")

    # When you .currentIndexChanged.connect
    # idx: "AL", "AK", "MI" ...
    def evt_cmbStates_changed(self, idx):
        # QMessageBox.information(self, "Combobox", f"you selected {self.cmbStates.itemData(idx)}")
        data = self.cmbStates.itemData(idx)
        QMessageBox.information(self, "Combobox", f" You selected{data['ab']}\npupulation: {data['pop'] } ")

    def evt_cmbStates_highligted(self, idx):
        self.lblPop.setText(f"Population: { self.cmbStates.itemData(idx)['pop']} ")



if __name__ == "__main__":
    app = QApplication([])
    main = Main()
    main.show()

    sys.exit(app.exec_())

