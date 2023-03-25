# This Python file uses the following encoding: utf-8
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form_login import Ui_Login
from ui_from_to_create_account import Ui_CreateAccount


class Main(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stack = QStackedWidget(self)


#        self.ui_log = Ui_Login()
#        self.ui_log.setupUi(self)
#        self.login = LoginScreen(self)

        self.login = QDialog(self.stack)
        ui_log = Ui_Login()
        ui_log.setupUi(self.login)
        self.stack.addWidget(self.login)

        self.stack.setCurrentWidget(self.login)

        #self.login.btn_login.clicked.connect(self.login_fun)
#        self.login.btn_create_account.clicked.connect(self.go_to_create)


    def show_log(self):
        self.log.show()

    def login_fun(self):
        email = self.login.ui.led_email.text()
        password = self.login.ui.led_password.text()
        print(f"{email =}, {password =}")

    def go_to_create(self):
        self.account = QDialog(self.stack)
        account_ui = Ui_CreateAccount()
        account_ui.setupUi(self.account)
        self.stack.addWidget(self.account)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    # to put screens on a stack and switch between them
#    widget=QtWidgets.QStackedWidget()
#    widget.addWidget(main)
#    widget.setFixedWidth(500)
#    widget.setFixedHeight(600)
#    widget.show()
    main.show()
    sys.exit(app.exec())
