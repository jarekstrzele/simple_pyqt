import sys 
from PyQt5.QtWidgets import *



class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")

        self.lyt_main = QVBoxLayout()
        
        self.btn1 = QPushButton("Button 1")
        self.btn2 = QPushButton("Button 2")
        self.btn3 = QPushButton("Button 3")

        self.chk1 = QCheckBox("Checkbox1")

        self.ed1 = QLineEdit("Editable")
        self.ed2 = QLineEdit("Read only")
        self.ed2.setReadOnly(True)

        self.lst = QListWidget()
        self.lst.addItems(QStyleFactory.keys()) # QStyle returns list of styles on computer
        self.lst.itemDoubleClicked.connect(self.evt_lst_dbl)

        self.lyt_main.addWidget(self.btn1)
        self.lyt_main.addWidget(self.btn2)
        self.lyt_main.addWidget(self.btn3)
        self.lyt_main.addWidget(self.chk1)
        self.lyt_main.addWidget(self.ed1)
        self.lyt_main.addWidget(self.ed2)
        self.lyt_main.addWidget(self.lst)

        # widgets with its own style not overrding
        self.prg = QProgressBar()
        self.prg.setStyle(QStyleFactory.create("Windows"))
        self.prg.setValue(33)
        self.dial = QDial()
        self.dial.setStyle(QStyleFactory.create("Fusion"))

        self.lyt_main.addWidget(self.prg)
        self.lyt_main.addWidget(self.dial)


        self.setLayout(self.lyt_main)

    def evt_lst_dbl(self, item):
        app.setStyle(QStyleFactory.create(item.text()))
        QMessageBox.information(self, "Set Style", f"You selected the {item}, so it is {item.text()} ")




if __name__=="__main__":
    app=QApplication([])
    main=Main()
    main.show()

    sys.exit(app.exec_())