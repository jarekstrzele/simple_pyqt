import sys   
from PyQt5.QtWidgets import *  
  
app = QApplication(sys.argv)  
dlgMain = QDialog() # a container for all widgets that will be added
#  dlgMain     = QMainWindow()
#  dlgMain      = QWidget()
dlgMain.setWindowTitle("My GUI")  
dlgMain.show() # show the GUI  
  
sys.exit(app.exec_()) # execute the app

