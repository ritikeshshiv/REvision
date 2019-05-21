import RPi.GPIO as a #import the library to acess GPIO
from time import sleep
led=4  		     #variable for pin on which you are connecting the led
blinkcount=3
count=0
a.setmode(a.BCM)     #tell os which numbering system we are going to use
a.setwarnings(False) #To ignore warnings
a.setup(led,a.OUT)   #to tell os it is input pin or output pin
while(1):
	print("Led on")
	a.output(led,a.HIGH) #send the high logic level
	sleep(0.1)
	a.output(led,a.LOW)
	print("Led off")
	sleep(0.1)
	count=count+1
a.cleanup()
