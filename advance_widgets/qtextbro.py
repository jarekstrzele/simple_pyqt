import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtCore import QUrl


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit")

        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)

        self.tbr = QTextBrowser()
       

        self.lyt_main.addWidget(self.tbr)

    
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

        self.tbr.setHtml(html)
        self.tbr.repaint()

        self.btnHtml = QPushButton("lead HTML")
        self.lyt_main.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btnhtml_clicked)

    def evt_btnhtml_clicked(self):
        url = "html/test.html"
        self.tbr.setSource(QUrl.fromLocalFile(url))




        

if __name__=="__main__":
    app=QApplication([])
    main=Main()
    main.show()

    sys.exit(app.exec_())