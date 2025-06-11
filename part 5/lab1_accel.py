import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from lab1_ui_45 import *
import numpy as np
import csv

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0.1)

start_time = 0
time_limit = 0

def read():
  data = arduino.read(arduino.in_waiting)
  lines = data.split(b'\n')

  return lines[-2].decode('utf-8')


def mean(axis):
  return sum(axis) / len(axis)


def std_dev(axis):
  summation = 0
  for i in range(len(axis)):
    summation += pow(axis[i] - mean(axis), 2)

  return summation / len(axis)


class Lab1(QMainWindow):
  def __init__(self, *args):
    QMainWindow.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.setWindowTitle("arduino sensors")

    self.ui.pushButton.clicked.connect(self.timer_control)
    self.ui.Table_button.clicked.connect(self.write_csv)

    self.counter = 0
    self.x = []
    self.y = []
    self.z = []

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.timer_event)
    self.timer_on = False


  def timer_control(self):
    if self.timer_on:
      self.timer.stop()
      self.timer_on = False

      self.ui.pushButton.setText("Start")
      self.ui.pushButton.setStyleSheet("background-color: green; color: white; font-weight: bold;")

    else:
      interval = self.ui.spinBox.value()
      self.time_limit = self.ui.spinBox_3.value()

      self.timer.start(interval)
      self.timer_on = True

      self.start_time = time.time()

      self.ui.pushButton.setText("Stop")
      self.ui.pushButton.setStyleSheet("background-color: red; color: white; font-weight: bold;")


  def timer_event(self):
    self.ui.time_left.display(time.time() - self.start_time)
    self.counter += 1

    data = read()
    split = data.split('\t')

    self.x.append(float(split[0]))
    self.y.append(float(split[1]))
    self.z.append(float(split[2]))

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

    self.ui.mean_X.display(mean(self.x))
    self.ui.mean_Y.display(mean(self.x))
    self.ui.mean_Z.display(mean(self.x))

    self.ui.Standard_dev_X.display(std_dev(self.x))
    self.ui.Standard_dev_Y.display(std_dev(self.x))
    self.ui.Standard_dev_Z.display(std_dev(self.x))

    if (time.time() - self.start_time >= self.time_limit):
      print("Time limit: " + str(self.time_limit) + " exceeded")
      self.timer_control()

  @property
  def x_value(self):
    return self.x

  @property
  def y_value(self):
    return self.y

  @property
  def z_value(self):
    return self.z

  def write_csv(self):
    name = self.ui.plainTextEdit.toPlainText()
    with open(name+".csv", 'w', newline='') as csvfile:
      fieldnames = ['x', 'y', 'z']


      write = csv.writer(csvfile)
      write.writerow(fieldnames)
      for i in range(len(self.x)):
        write.writerow([self.x[i], self.y[i], self.z[i]])

if __name__ == "__main__":
  app = QApplication([])
  form = Lab1()
  form.show()
  sys.exit(app.exec_())
