import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("web engine Q")
        self.resize(1000, 400)

        self.lyt_main = QHBoxLayout()
        self.lyt_left = QVBoxLayout()
        self.lyt_right = QVBoxLayout()
        self.lyt_main.addLayout(self.lyt_left)
        self.lyt_main.addLayout(self.lyt_right)
        self.setLayout(self.lyt_main)

        self.wev=QWebEngineView()
        self.lyt_left.addWidget(self.wev)
        self.wev.resize(100,200)


        html = """
            <h1>My header </h1>
            <p>This is <b>BOLD</b> and <i>Itallic</i> type </p>
            <ul>
                <li> lit item 1 </li>
                <li> list item  2 </li>
                <li> lit item 1 </li>
                <li> list item  2 </li>
                <li> lit item 1 </li>
                <li> list item  2 </li>
            </ul>
        """

        self.wev.setHtml(html)
        self.wev.repaint()
         
        self.ledHtml = QLineEdit("qwebengineview")
        self.lyt_left.addWidget(self.ledHtml)
        
        self.btnHtml = QPushButton("Load html")
        self.lyt_right.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btnHtml_clicked)

        self.btnForward = QPushButton(">>")
        self.lyt_right.addWidget(self.btnForward)
        self.btnForward.clicked.connect(self.wev.forward)

        self.backWard = QPushButton("<<")
        self.lyt_right.addWidget(self.backWard)
        self.backWard.clicked.connect(self.wev.back)

        self.btnHistory = QPushButton("Show History ")
        self.lyt_right.addWidget(self.btnHistory)
        self.btnHistory.clicked.connect(self.evt_btnHistory_clicked)

        self.tblHistory = QTableWidget(3,4)
        self.tblHistory.resize(400,200)
        self.tblHistory.hide()
        self.lyt_right.addWidget(self.tblHistory)
        self.tblHistory.setColumnWidth(0, 100)
        self.tblHistory.setColumnWidth(1, 100)
        self.tblHistory.setColumnWidth(2, 100)
        self.tblHistory.setColumnWidth(3, 100)
        self.tblHistory.setHorizontalHeaderLabels(["Class", "Module", "URL", "Last Visited" ])
        



    def evt_btnHistory_clicked(self):
        if self.tblHistory.isHidden():
            self.tblHistory.show()
            self.btnHistory.setText("Hide History")
            
            history = self.wev.history()
            cnt = history.count()
            self.tblHistory.setRowCount(cnt)
            for idx in range(cnt):
                itm = history.itemAt(idx)
                print(list(itm.title()))
                print("*"*10)
                print(type(itm))
                sClass= itm.title()
                print(sClass, itm.url().toString(), itm.lastVisited().toString)
        else:
            self.tblHistory.hide()
            self.btnHistory.setText("Show Hisotry")

    def evt_btnHtml_clicked(self):

        url = f"https://doc.qt.io/qt-5/{self.ledHtml.text().lower()}.html"
        # somelocal.html
        # self.wev.setUrl(QUrl.fromLocalFile(<path somelocale.html>))
        self.wev.setUrl(QUrl.fromUserInput(url))
        self.wev.repaint()






if __name__=="__main__":
    app=QApplication([])
    main=Main()
    main.show()

    sys.exit(app.exec_())
