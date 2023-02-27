# Layouts:
# QVBoxLaout
#   QHBoxLayout
#       QListBox1
#       QListBox2
#       QVBoxLayout
#           stretch - > btnAdd, tbnRemove ->stretch
#   btnDoSomthing

import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget")

        ## create widgets
        self.lbxLanguages = QListWidget()
        self.lbxLanguages.addItems(['C','C++','C#','JavaScript','Python', 'PHP', 'Java', 'COBOL', 'Ruby',
        'Visual Basic', 'Rust', 'Julia', 'Go', 'Haskell'])
        self.lbxLanguages.sortItems()
        # to select multiple items; without that only one item you can select
        self.lbxLanguages.setSelectionMode(QAbstractItemView.ExtendedSelection)
        # to select btn add
        self.lbxLanguages.itemSelectionChanged.connect(self.evt_lbxLanguages_selection)

        self.lbxLanguagesIKnow = QListWidget()
        self.lbxLanguagesIKnow.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lbxLanguagesIKnow.itemSelectionChanged.connect(self.evt_lbxLanguagesIKnow_selection)


        ## Buttons
        self.btnAddLanguage = QPushButton("--->")
        self.btnAddLanguage.clicked.connect(self.evt_btnAdd_clicked)
        self.btnRemoveLanguage = QPushButton("<---")
        self.btnRemoveLanguage.clicked.connect(self.evt_btnRemove_clicked)

        self.btnDoSomeThing =QPushButton("Do Something")
        self.btnDoSomeThing.clicked.connect(self.evt_btnDoSomething_clicked)

        self.setupLayout()

    def setupLayout(self):
        self.lytMain = QVBoxLayout()
        self.lytLists = QHBoxLayout()
        self.lytButtons = QVBoxLayout()

        ### add widgets to lytLists
        self.lytLists.addWidget(self.lbxLanguages)
        self.lytLists.addLayout(self.lytButtons)
        self.lytLists.addWidget(self.lbxLanguagesIKnow)

        ### add widgets to lytMain
        self.lytMain.addLayout(self.lytLists)
        self.lytMain.addWidget(self.btnDoSomeThing)

        ### add widgets to lytButtons
        self.lytButtons.addStretch()
        self.lytButtons.addWidget(self.btnAddLanguage)
        self.lytButtons.addWidget(self.btnRemoveLanguage)
        self.lytButtons.addStretch()

        self.setLayout(self.lytMain)
    
    ### event handlers
    def evt_btnAdd_clicked(self):
        listItem = self.lbxLanguages.selectedItems()
        for itm in listItem:
            QLWI = self.lbxLanguages.takeItem(self.lbxLanguages.row(itm))
            self.lbxLanguagesIKnow.addItem(QLWI)
            # print(f"{itm =}")
            # print(f"{QLWI =}")
        #self.repaint()
        # self.lbxLanguagesIKnow.repaint()
        # print(self.lbxLanguagesIKnow.count())
        self.btnDoSomeThing.setDefault(True)

    def evt_btnRemove_clicked(self):
        listItem = self.lbxLanguagesIKnow.selectedItems()
        for itm in listItem:
            QLWI = self.lbxLanguagesIKnow.takeItem(self.lbxLanguagesIKnow.row(itm))
            self.lbxLanguages.addItem(QLWI)
        self.btnDoSomeThing.setDefault(True)
        self.repaint()


    def evt_lbxLanguages_selection(self):
        self.btnAddLanguage.setDefault(True)
        self.repaint()
    
    def evt_lbxLanguagesIKnow_selection(self):
        self.btnRemoveLanguage.setDefault(True)
        self.repaint()

    def evt_btnDoSomething_clicked(self):
        if self.lbxLanguagesIKnow.count() == 0:
            QMessageBox.information(self, "Languages", "You don't know any languages!")
        else:
            sLangs = ""
            for row in range(self.lbxLanguagesIKnow.count()):
                sLangs += self.lbxLanguagesIKnow.item(row).text() + "\n"
            QMessageBox.information(self, "Languages",
             f"You know {self.lbxLanguagesIKnow.count()} languages\n they are \n {sLangs}")
        




        



if __name__=="__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())

