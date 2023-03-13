# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Dialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btn_login.clicked.connect(self.login_fun)
        self.ui.led_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def login_fun(self):
        email = self.ui.led_email.text()
        password = self.ui.led_password.text()
        print(f"{email =}, {password =}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Dialog()
    widget.show()
    sys.exit(app.exec())
