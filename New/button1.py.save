#button as a ON and OFF
import RPi.GPIO as a
from time import sleep
a.setmode(a.BOARD)
a.setwarnings(False)
a.setup(19,a.IN)
a.setup(21,a.OUT)
a.setwarnings(False)
count=0
while True:
    if(count==0):
        inputval=a.input(19)
    if(inputval==True):
        a.output(21,a.HIGH)
        count+=1
    if(count==1):
        inputval=a.input(19)
    if(inputval==True):
        a.output(21,a.LOW)
        count-=1
        
a.cleanup()
