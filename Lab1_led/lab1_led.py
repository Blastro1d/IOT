import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=0.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    num = input("command > ")  # Taking input from user
    value = write_read(num)
    res = value.decode().replace("\n", "")
    print(res)
