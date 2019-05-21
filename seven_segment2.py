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
k.output(seg,k.HIGH)
while 1:
    n=int(input("Enter number"))
    k.output(list1[n],k.HIGH)
    sleep(1)
    k.output(list1[n],k.LOW)
k.cleanup()
