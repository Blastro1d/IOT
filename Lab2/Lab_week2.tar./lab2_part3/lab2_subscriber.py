import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from bluetooth_ui import *
import numpy as np
import zmq
import time

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5666")

def read():
    try:
        message = socket.recv_string(flags=zmq.NOBLOCK)
        print(message)
    except zmq.Again:
        pass

def update_subscription(self):
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "")
    if self.ui.Accel_all.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Accel all")
    else:
        if self.ui.Accel_x.isChecked() == True:
            socket.setsockopt_string(zmq.SUBSCRIBE, "Accel x")
        if self.ui.Accel_y.isChecked() == True:
            socket.setsockopt_string(zmq.SUBSCRIBE, "Accel y")
        if self.ui.Accel_z.isChecked() == True:
            socket.setsockopt_string(zmq.SUBSCRIBE, "Accel z")

    if self.ui.Gyro_all.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro all")
    else:
        if self.ui.Gyro_x.isChecked() == True:
            socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro x")
        if self.ui.Gyro_y.isChecked() == True:
            socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro y")
        if self.ui.Gyro_z.isChecked() == True:
            socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro z")

class Bluetooth(QMainWindow):
  def __init__(self, *args):
    QMainWindow.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.setWindowTitle("arduino sensors")
    socket.setsockopt_string(zmq.SUBSCRIBE, "Accel all")


    self.counter = 0
    self.accel_x = []
    self.accel_y = []
    self.accel_z = []

    self.gyro_x = []
    self.gyro_y = []
    self.gyro_z = []

    self.timer_on = True
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.timer_event)
    self.timer.start(1000)



  def timer_event(self):
    self.counter += 1
    update_subscription(self)

    print("timer")
    read()
    max_range = 20

    self.accel_x.append(0.1)
    self.accel_y.append(0.2)
    self.accel_z.append(0.3)

    self.gyro_x.append(0.1)
    self.gyro_y.append(0.2)
    self.gyro_z.append(0.3)

    while max_range < self.counter:
      self.accel_x.pop(0)
      self.accel_y.pop(0)
      self.accel_z.pop(0)

      self.gyro_x.pop(0)
      self.gyro_y.pop(0)
      self.gyro_z.pop(0)
      self.counter -= 1

    self.ui.Mplwidget.canvas.axes.clear()
    self.ui.Mplwidget.canvas.axes.plot(range(len(self.accel_x)), self.accel_x, 'b', linewidth=0.5)
    self.ui.Mplwidget.canvas.axes.plot(range(len(self.accel_y)), self.accel_y, 'r', linewidth=0.5)
    self.ui.Mplwidget.canvas.axes.plot(range(len(self.accel_z)), self.accel_z, 'g', linewidth=0.5)
    self.ui.Mplwidget.canvas.axes.plot(range(len(self.gyro_x)), self.gyro_x, 'y', linewidth=0.5)
    self.ui.Mplwidget.canvas.axes.plot(range(len(self.gyro_y)), self.gyro_y, 'm', linewidth=0.5)
    self.ui.Mplwidget.canvas.axes.plot(range(len(self.gyro_z)), self.gyro_z, 'c', linewidth=0.5)
    self.ui.Mplwidget.canvas.draw()


if __name__ == "__main__":
  app = QApplication([])
  form = Bluetooth()
  form.show()
  sys.exit(app.exec_())
