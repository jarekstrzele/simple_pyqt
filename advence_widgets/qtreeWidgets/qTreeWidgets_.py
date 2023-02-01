import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeQidget")
        self.resize(600,400)

        ## create widgets
        self.trwQt = QTreeWidget()
        self.trwQt.setColumnCount(3)
        self.trwQt.setHeaderLabels(["Qt Class", "Methods", "Signals"])
        self.trwQt.itemDoubleClicked.connect(self.evt_trwQt_dblClicked)

        self.populateTree()

        self.trwQt.sortItems(0, Qt.AscendingOrder)
        self.trwQt.setColumnWidth(0,200) #(colNum, width)
        self.trwQt.expandItem(self.twiQWidget)

        self.cmbParents = QComboBox()
        lstClasses = get_all_items(self.trwQt)
        lstClasses.sort()
        for cls in lstClasses:
            self.cmbParents.addItem(cls.text(0))

        self.ledClassName = QLineEdit("Q")

        self.btnAddClass = QPushButton("Add Class")
        self.btnAddClass.clicked.connect(self.evt_btnAddClass_clicked)


        ### setup layout
        self.lytMain=QVBoxLayout()
        self.lytMain.addWidget(self.trwQt)
        self.lytMain.addWidget(self.cmbParents)
        self.lytMain.addWidget(self.ledClassName)
        self.lytMain.addWidget(self.btnAddClass)

        self.setLayout(self.lytMain)
    
    def populateTree(self):
        # create top level items
        self.twiQWidget = QTreeWidgetItem(self.trwQt, ["QWidget Module"])
        self.twiQGui  = QTreeWidgetItem(self.trwQt, ["QGui Module"])
        self.twiQCore = QTreeWidgetItem(self.trwQt, ["QCore Module"])

        # add subItems to QWidget Module
        lstQtWidget = ["QDialog", "QLabel", "QLine", "QTextEdit", "QGroupBox", "QFrame"]
        for cls in lstQtWidget:
            self.twiQWidget.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))]))

        # add subitem to QGui
        lstQtGui = ["QBitmap", "QColor", "QFont", "QIcon", "QImage"]
        for cls in lstQtGui:
            self.twiQGui.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))]))

         # add subitem to QGui
        lstQtCore = ["QTHread", "QDateTime", "QPixmap", "QUrl", "QFile"]
        for cls in lstQtCore:
            self.twiQCore.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))]))

        ## add subitem to QDialog but we have no variable to act with these objects
        ## so we use findTime method
        twi = self.trwQt.findItems("QDialog", Qt.MatchRecursive)[0]
        lstQDialog = ["QFileDialog", "QColorDialog", "QFontDialog", "QMessageBox"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))]))

        ## add subitem to QFrame but we have no variable to act with these objects
        ## so we use findTime method
        twi = self.trwQt.findItems("QFrame", Qt.MatchRecursive)[0]
        lstQDialog = ["QLabel", "QLCDNumbet", "QStackWidget", "QToolBox"]
        for cls in lstQDialog:
            twi.addChild(QTreeWidgetItem([cls, str(random.randrange(25)), str(random.randrange(8))]))

    # event handler
    def evt_trwQt_dblClicked(self, twi, col):
        print(col)
        QMessageBox.information(self, "Qt classes", f"You choose the {twi.text(0)} class" )

    def evt_btnAddClass_clicked(self):
        className = self.ledClassName.text()
        cmbParents = self.cmbParents.currentText()
        ans = QMessageBox.question(self,
            "Add Class",
            f"Are you shire that you want to add {className} to {cmbParents} ")
        if ans == QMessageBox.Yes:
            twi = self.trwQt.findItems(self.cmbParents.currentText(), Qt.MatchRecursive)[0]
            twi.addChild(QTreeWidgetItem([    className 
                                            , str(random.randrange(25))
                                            , str(random.randrange(8))
                                        ]
            ))


def get_subtree_nodes(tree_widget_item):
    """Returns all QTreeWidgetItems in the subtree rooted at the fiven node."""
    nodes = []
    nodes.append(tree_widget_item)
    for i in range(tree_widget_item.childCount()):
        nodes.extend(get_subtree_nodes(tree_widget_item.child(i)))
    return nodes

def get_all_items(tree_widget):
    """Returns all QTreeWidgetItems in the given QTreeWidget."""
    all_items = []
    for i in range(tree_widget.topLevelItemCount()):
        top_item = tree_widget.topLevelItem(i)
        all_items.extend(get_subtree_nodes(top_item))
    
    return all_items


if __name__ == "__main__":
    app = QApplication([])
    main=Main()
    main.show()
    sys.exit(app.exec_())