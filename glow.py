import RPi.GPIO as a
from time import sleep
a.setmode(a.BOARD)
a.setwarnings(False)
red=5
a.setup(red,a.OUT)
while 1:
 a.output(red,True)
 sleep(2)
 print("ON")
 a.output(red,False)
 sleep(2)
 print("OFF")
 break;
a.cleanup()
