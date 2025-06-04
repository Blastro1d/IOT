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

import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0.1)


def read():
  data = arduino.read(arduino.in_waiting)
  lines = data.split(b'\n')

  return lines[-2].decode('utf-8')


class Lab1(QMainWindow):
  def __init__(self, *args):
    QMainWindow.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    # window = loadUi("lab1.ui", self)
    self.setWindowTitle("arduino sensors")

    self.ui.pushButton.clicked.connect(self.mybuttonfunction)

    self.counter = 0
    self.x = []
    self.y = []
    self.z = []

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.timer_event)
    self.timer_on = False

  def mybuttonfunction(self):
    if self.timer_on:
      self.timer.stop()
      self.timer_on = False
    else:
      interval = self.ui.spinBox.value() * 100
      self.timer.start(interval)
      self.timer_on = True

  def timer_event(self):
    self.counter += 1

    data = read()
    split = data.split('\t')
    
    values = [split[0], split[1], split[2][:-2]]

    print(values)
    self.x.append(float(values[0]))
    self.y.append(float(values[1]))
    self.z.append(float(values[2]))

    max_range = self.ui.spinBox_2.value()

    while max_range < len(self.x):
      self.x.pop(0)
      self.y.pop(0)
      self.z.pop(0)

    self.ui.MplWidget.canvas.axes.clear()
    self.ui.MplWidget.canvas.axes.plot(range(len(self.x)), self.x, 'b', linewidth=0.5)
    self.ui.MplWidget.canvas.axes.plot(range(len(self.y)), self.y, 'r', linewidth=0.5)
    self.ui.MplWidget.canvas.axes.plot(range(len(self.z)), self.z, 'g', linewidth=0.5)
    self.ui.MplWidget.canvas.draw()

  @property
  def x_value(self):
    return self.x

  @property
  def y_value(self):
    return self.y

  @property
  def z_value(self):
    return self.z

if __name__ == "__main__":
  app = QApplication([])
  form = Lab1()
  form.show()
  sys.exit(app.exec_())
