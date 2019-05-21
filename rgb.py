import RPi.GPIO as a
from time import sleep
red=15
a.setmode(a.BCM)
a.setwarnings(False)
a.setup(red,a.OUT)
a.output(red,a.HIGH)
sleep(2)
a.output(red,a.LOW)
a.cleanup()
