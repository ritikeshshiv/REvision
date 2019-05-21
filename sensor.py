import RPi.GPIO as a
from time import sleep
sensor=23
led=18

a.setmode(a.BCM)
a.setwarnings(False)
a.setup(sensor,a.IN)
a.setup(led,a.OUT)

a.output(led,False)
print("Initializing PIR Sensor...")
sleep(12)
print("PIR READY")
print (" ")

try:
    while 1:
        if a.input(sensor):
            a.output(led,True)
            print("Motion detected")
            while a.input(sensor):
                sleep(0.2)
        else:
            a.output(led,False)

except keyboardInterrupt:
    a.cleanup()
