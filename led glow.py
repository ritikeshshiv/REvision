import RPi.GPIO as a #import the library to acess GPIO
from time import sleep
led=4                #variable for pin on which you are connecting the led
a.setmode(a.BCM)     #tell os which numbering system we are going to use
a.setwarnings(False) #To ignore warnings
a.setup(led,a.OUT)
print("Led glow")
a.output(led,a.HIGH) #send the high logic level/ a.output(led,False)
sleep(1)
a.output(led,a.LOW) #a.output(led,False)
a.cleanup()
