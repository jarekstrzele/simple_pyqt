import sys
from PySide6.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication([])
    main = Main()
    main.show()

    sys.exit(app.exec_())