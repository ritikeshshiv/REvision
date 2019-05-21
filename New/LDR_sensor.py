import RPi.GPIO as a
from time import sleep
sensor=23

a.setmode(a.BCM)
a.setwarnings(False)
a.setup(sensor,a.IN)

print("Initializing LDR Sensor...")
sleep(1)
print("LDR READY")
print (" ")

try:
    while 1:
        if a.input(sensor):
            print("Light ON")
        else:
            print("Light OFF")

except keyboardInterrupt:
    a.cleanup()

