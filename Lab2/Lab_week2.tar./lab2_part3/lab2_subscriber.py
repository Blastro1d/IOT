import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from bluetooth2_ui import *
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
socket.connect("tcp://localhost:6000")


def read(self):
    try:
        message = socket.recv_string(flags=zmq.NOBLOCK)
        lines = message.splitlines()
        for line in lines:
            if line.startswith("Accel all:"):
                values = line[len("Accel all:"):].strip().strip("()").split(", ")
                values = [value.strip("'") for value in values]

                self.accel_x.append(float(values[0]))
                self.accel_y.append(float(values[1]))
                self.accel_z.append(float(values[2]))

            elif line.startswith("Gyro all:"):
                values = line[len("Gyro all:"):].strip().strip("()'").split(", ")
                values = [value.strip("'") for value in values]

                self.gyro_x.append(float(values[0]))
                self.gyro_y.append(float(values[1]))
                self.gyro_z.append(float(values[2]))

            elif line.startswith("Accel x:"):
                value = line[len("Accel x:"):].strip().strip("()'")
                self.accel_x.append(float(value))

            elif line.startswith("Accel y:"):
                value = line[len("Accel y:"):].strip().strip("()'")
                self.accel_y.append(float(value))

            elif line.startswith("Accel z:"):
                value = line[len("Accel z:"):].strip().strip("()'")
                self.accel_z.append(float(value))

            elif line.startswith("Gyro x:"):
                value = line[len("Gyro x:"):].strip().strip("()'")
                self.gyro_x.append(float(value))

            elif line.startswith("Gyro y:"):
                value = line[len("Gyro y:"):].strip().strip("()'")
                self.gyro_y.append(float(value))

            elif line.startswith("Gyro z:"):
                value = line[len("Gyro z:"):].strip().strip("()'")
                self.gyro_z.append(float(value))

    except zmq.Again:
        pass

def unsubscribe_all():
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Accel all:")
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Accel x:")
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Accel y:")
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Accel z:")

    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Gyro all:")
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Gyro x:")
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Gyro y:")
    socket.setsockopt_string(zmq.UNSUBSCRIBE, "Gyro z:")

def update_subscription(self):
    unsubscribe_all()
    self.check = self.switch

    if self.ui.Accel_all.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Accel all:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 1

    elif self.ui.Accel_x.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Accel x:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 2

    elif self.ui.Accel_y.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Accel y:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 3

    elif self.ui.Accel_z.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Accel z:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 4

    elif self.ui.Gyro_all.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro all:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 5

    elif self.ui.Gyro_x.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro x:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 6

    elif self.ui.Gyro_y.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro y:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 7

    elif self.ui.Gyro_z.isChecked() == True:
        socket.setsockopt_string(zmq.SUBSCRIBE, "Gyro z:")
        socket.setsockopt_string(zmq.UNSUBSCRIBE, "nothing")
        self.switch = 8
    else:
        self.switch = 0

def clear_lists(self):
    if self.switch != self.check:
        self.accel_x.clear()
        self.accel_y.clear()
        self.accel_z.clear()
        self.gyro_x.clear()
        self.gyro_y.clear()
        self.gyro_z.clear()

def pop_list(self):
    if self.switch == 1:
        self.accel_x.pop(0)
        self.accel_y.pop(0)
        self.accel_z.pop(0)

    elif self.switch == 2:
        self.accel_x.pop(0)

    elif self.switch == 3:
        self.accel_y.pop(0)

    elif self.switch == 4:
        self.accel_z.pop(0)

    elif self.switch == 5:
        self.gyro_x.pop(0)
        self.gyro_y.pop(0)
        self.gyro_z.pop(0)

    elif self.switch == 6:
        self.gyro_x.pop(0)

    elif self.switch == 7:
        self.gyro_y.pop(0)

    elif self.switch == 8:
        self.gyro_z.pop(0)

def max_list(self):
    return max(len(self.accel_x), len(self.accel_y), len(self.accel_z), len(self.gyro_x), len(self.gyro_y), len(self.gyro_z))

class Bluetooth(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("arduino sensors")

        self.switch = 0
        self.check = 0

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
        self.timer.start(50)

    def timer_event(self):
        self.counter += 1
        socket.setsockopt_string(zmq.SUBSCRIBE, "nothing")
        update_subscription(self)
        read(self)

        max_range = 51
        graph_length = max_list(self)
        if max_range < graph_length:
            pop_list(self)

        clear_lists(self)
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
