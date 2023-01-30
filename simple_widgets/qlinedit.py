import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit")
        self.ledTitle = QLineEdit(self.windowTitle(), self)
        self.ledTitle.setPlaceholderText("Enter a new dialog title")
        #self.ledTitle.setReadOnly(True)
        self.ledTitle.setEchoMode(QLineEdit.Password)
        self.ledTitle.setAlignment(Qt.AlignRight)
        self.ledTitle.move(50,50)
        self.btnChange = QPushButton("Update title", self)
        self.btnChange.move(50,80)
        self.btnChange.clicked.connect(self.evt_btn_clicked)
        self.ledTitle.textChanged.connect(self.evt_ledTitle_textChanged)


    def evt_btn_clicked(self):
        res = QMessageBox.question(self, "Line Edit",
                                         "Are you sure you want to change the window title to '" + 
            self.ledTitle.text() + "'" )
        if res == QMessageBox.Yes:
            self.setWindowTitle(self.ledTitle.text())
    
    def evt_ledTitle_textChanged(self, title):
        self.setWindowTitle(title)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())

