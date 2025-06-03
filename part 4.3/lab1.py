import sys
from PyQt5.QtCore import Qt, QTimer
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

    self.xcounter = 0
    self.x = []
    self.y = []

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.timer_event)
    self.timer_on = False

  def mybuttonfunction(self):
    if self.timer_on:
      self.timer.stop()
      self.timer_on = False
    else:
      interval = self.ui.spinBox.value()
      self.timer.start(interval)
      self.timer_on = True

  def timer_event(self):
    self.xcounter += 1
    self.x.append(self.xcounter)
    self.y.append(np.random.rand())

    range = self.ui.spinBox_2.value()

    while range < len(self.x):
      self.x.pop(0)
      self.y.pop(0)

    self.ui.MplWidget.canvas.axes.clear()
    self.ui.MplWidget.canvas.axes.plot(self.x, self.y, 'r', linewidth=0.5)
    self.ui.MplWidget.canvas.draw()

if __name__ == "__main__":
  app = QApplication([])
  form = Lab1()
  form.show()
  sys.exit(app.exec_())
