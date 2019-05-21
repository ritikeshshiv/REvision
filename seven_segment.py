import RPi.GPIO as k
from time import sleep
k.setmode(k.BOARD)
k.setwarnings(False)
seg=29
a=31
b=33
c=35
d=36
e=37
f=38
g=40
list=[a,b,c,d,e,f,g]
k.setup(seg,k.OUT)
k.setup(list,k.OUT)
list1=[(a,b,c,d,e,f),(b,c),(a,b,g,e,d),(a,b,c,d,g),(b,c,f,g),(a,f,g,c,d),(a,c,d,e,f,g),(a,b,c),(a,b,c,d,e,f,g),(a,b,c,f,g)]
while 1:
    k.output(seg,k.HIGH)
    for i in range(10):
        k.output(list1[i],k.HIGH)
        sleep(1)
        k.output(list1[i],k.LOW)
        sleep(0.5)
k.cleanup()

