import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor, QColor
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("web engine Q")

        self.lyt_main = QVBoxLayout()
        self.setLayout(self.lyt_main)

        self.wev=QWebEngineView()
        self.lyt_main.addWidget(self.wev)


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
        self.lyt_main.addWidget(self.ledHtml)

        self.btnHtml = QPushButton("Load html")
        self.lyt_main.addWidget(self.btnHtml)
        self.btnHtml.clicked.connect(self.evt_btnHtml_clicked)

        self.btnForward = QPushButton(">>")
        self.lyt_main.addWidget(self.btnForward)
        self.btnForward.clicked.connect(self.wev.forward)

        self.backWard = QPushButton("<<")
        self.lyt_main.addWidget(self.backWard)
        self.backWard.clicked.connect(self.wev.back)





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
