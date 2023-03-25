import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Tworzenie i konfiguracja wykresu
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.setCentralWidget(self.canvas)
        self.addToolBar(self.toolbar)
        self.axes = self.figure.add_subplot(111)

        # Tworzenie danych do wykresu
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)

        # Rysowanie wykresu
        self.axes.plot(x, y)
        self.axes.set_title('Wykres funkcji sin(x)')
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')

        # Konfiguracja rozmiaru wykresu
        self.figure.tight_layout()
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()

        # Konfiguracja okna
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Wykres funkcji sin(x)')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
