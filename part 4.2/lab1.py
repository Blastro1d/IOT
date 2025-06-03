import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from lab1_ui import *
import numpy as np

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Lab1(QMainWindow):
  def __init__(self, *args):
    QMainWindow.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    # window = loadUi("lab1.ui", self)
    self.setWindowTitle("arduino sensors")

    self.ui.pushButton.clicked.connect(self.mybuttonfunction)

    self.x = np.array([1, 2, 3, 4, 5])
    self.y = np.array([0.1, 0.6, 0.8, 0.3, 0.1])

  def mybuttonfunction(self):
    self.ui.MplWidget.canvas.axes.clear()
    self.ui.MplWidget.canvas.axes.plot(self.x, self.y, 'r', linewidth=0.5)
    self.ui.MplWidget.canvas.draw()

if __name__ == "__main__":
  app = QApplication([])
  form = Lab1()
  form.show()
  sys.exit(app.exec_())
