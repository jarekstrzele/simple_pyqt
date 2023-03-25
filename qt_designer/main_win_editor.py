import sys 

from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5.uic import loadUi 

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main_win_editor.ui", self)

        # look at the qt designer action editpr
        self.actionNew.triggered.connect(self.new_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_as.triggered.connect(self.save_as_file)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCut.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionSet_Dark_Mode.triggered.connect(self.setDarkMode)
        self.actionSet_Light_Mode.triggered.connect(self.setLightMode)
        self.actionChange_Font_Size.triggered.connect(self.changeFontSize)


    def new_file(self):
        print("new file")
    
    def open_file(self):
        print("open file")
    
    def save_file(self):
        print("save")

    def save_as_file(self):
        print("save as")
    
    def undo(self):
        print("undo")
    
    def redo(self):
        print("redo")
    
    def copy(self):
        print("copy")
    
    def cut(self):
        print("cut")
    
    def paste(self):
        print("paste")
    
    def setDarkMode(self):
        print("dark mode")

    def setLightMode(self):
        print("light mode")

    def changeFontSize(self):
        print("change font")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()

    app.exec_()


