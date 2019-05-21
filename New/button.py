import RPi.GPIO as a
from time import sleep
a.setmode(a.BOARD)
a.setwarnings(False)
a.setup(19,a.IN)
a.setup(21,a.OUT)
a.setwarnings(False)

while True:
    inputval=a.input(19)
    if(inputval==True):
        a.output(21,a.HIGH)
    else:
        sleep(0.1)
        a.output(21,a.LOW)
a.cleanup()
