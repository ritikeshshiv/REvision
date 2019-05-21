import serial
import RPi.GPIO as a
import time
import string

a.setmode(a.BOARD)
port=serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

port.write("AT"+"\r")
rcv=port.read(10)
print(rcv)
time.sleep(1)