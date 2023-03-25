# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox
from PySide6 import QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        todos = ["Walk dog", "Buy groceries", "Send email", "Call bank", "Clean house"]
        for todo in todos:
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.todo_listWidget.addItem(item)

        self.ui.btn_toggle.clicked.connect(self.toggle_all)
        self.ui.btn_add_item.clicked.connect(self.add_item)
#        self.ui.todo_listWidget.itemClicked.connect(self.item_clicked_handler)
        self.ui.todo_listWidget.itemChanged.connect(self.item_changed_handler)

    def item_changed_handler(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            print(item.text())
        else:
            self.ui.todo_listWidget.blockSignals(False)


#    def item_clicked_handler(self, item):
#        print(item.text())


    def add_item(self):
        new_item = self.ui.led_new_item.text()
        if new_item == "":
            msg =QMessageBox()
            msg.setText("Pusty element")

        else:
            new_item_qt = QListWidgetItem(new_item)
            new_item_qt.setCheckState(QtCore.Qt.Unchecked)
            self.ui.todo_listWidget.addItem(new_item_qt)

        self.ui.led_new_item.setText('')


    def toggle_all(self):
        for i in range(self.ui.todo_listWidget.count()):
            item = self.ui.todo_listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
            else:
                item.setCheckState(QtCore.Qt.Checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
