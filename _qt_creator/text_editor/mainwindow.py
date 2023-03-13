# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

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
        self.current_path = None
        self.current_fontsize = 8
        self.setWindowTitle("Untitled")

        self.ui.actionNew.triggered.connect(self.newFile)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionSave.triggered.connect(self.saveFile)
        self.ui.actionSave_as.triggered.connect(self.saveFileAs)

        self.ui.actionUndo.triggered.connect(self.undo)
        self.ui.actionRedo.triggered.connect(self.redo)
        self.ui.actionCut.triggered.connect(self.cut)
        self.ui.actionCopy.triggered.connect(self.copy)
        self.ui.actionPaste.triggered.connect(self.paste)

        self.ui.actionSet_Dark_Mode.triggered.connect(self.setDarkMode)
        self.ui.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.ui.actionIncrease_Font_Size.triggered.connect(self.incFontSize)
        self.ui.actionDecrease_Font_Size.triggered.connect(self.decFontSize)




    def newFile(self):
        self.ui.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\Users\\jaros\\Desktop\\Prog\\simple_pyqt\\_qt_creator\\text_editor', 'Text files (*.*)')
        self.setWindowTitle(fname[0])
        with open(fname[0],'r') as f:
            filetext = f.read()
            self.ui.textEdit.setText(filetext)
        self.current_path = fname[0]

    def saveFile(self):
        if self.current_path is not None:
            filetext = self.ui.textEdit.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(filetext)
        else:
            self.saveFileAs()

    def saveFileAs(self):
        # QFileDialog.getSaveFileName returns a tuple with path and file type option

        pathname = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\jaros\\Desktop\\Prog\\simple_pyqt\\_qt_creator\\text_editor', 'Text files (*.*)')[0]
        filetext = self.ui.textEdit.toPlainText()
        print(f"{pathname =}, type: {type(pathname)}")
        with open(pathname, 'w') as f:
            f.write(filetext)
        self.setWindowTitle(pathname)


    def undo(self):
        self.ui.textEdit.undo()

    def redo(self):
        self.ui.textEdit.redo()

    def cut(self):
        self.ui.textEdit.cut()

    def copy(self):
        self.ui.textEdit.copy()

    def paste(self):
        self.ui.textEdit.paste()

    def setDarkMode(self):
        self.setStyleSheet('''
        QWidget{
            background-color: rgb(22,22,22);
            color: #FFFFFF
        }
        QTextEdit {
            background-color: rgb(50,50,50);
        }
        QMenuBar::item::selected  {
            color: #000000
        }

        ''')

    def setLightMode(self):
        self.setStyleSheet('')

    def changeFontSize(self):
        print("font size changer")

    def incFontSize(self):
        self.current_fontsize +=1
        self.ui.textEdit.setFontPointSize(self.current_fontsize)

    def decFontSize(self):
        self.current_fontsize -=1
        self.ui.textEdit.setFontPointSize(self.current_fontsize)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
