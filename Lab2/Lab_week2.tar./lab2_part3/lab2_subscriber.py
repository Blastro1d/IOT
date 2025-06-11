import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from bluetooth_ui import *
import numpy as np
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

def read():
    print("TEst read1")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    message = socket.recv_string()
    print("TEst read2")
    print(message)

class Bluetooth(QMainWindow):
  def __init__(self, *args):
    QMainWindow.__init__(self)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.setWindowTitle("arduino sensors")
    
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
    print("TEST$")

  def timer_event(self):
    self.counter += 1

    print("TEstr")
    read()
    max_range = 20

    while max_range < len(self.accel_x):
      self.x.pop(0)
      self.y.pop(0)
      self.z.pop(0)

    # self.ui.MplWidget.canvas.axes.clear()
    # self.ui.MplWidget.canvas.axes.plot(range(len(self.x)), self.x, 'b', linewidth=0.5)
    # self.ui.MplWidget.canvas.axes.plot(range(len(self.y)), self.y, 'r', linewidth=0.5)
    # self.ui.MplWidget.canvas.axes.plot(range(len(self.z)), self.z, 'g', linewidth=0.5)
    # self.ui.MplWidget.canvas.draw()

    # if (time.time() - self.start_time >= self.time_limit):
    #   print("Time limit: " + str(self.time_limit) + " exceeded")
    #   self.timer_control()


if __name__ == "__main__":
  app = QApplication([])
  form = Bluetooth()
  form.show()
  sys.exit(app.exec_())
