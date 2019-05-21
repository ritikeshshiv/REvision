import RPi.GPIO as k
from time import sleep
k.setmode(k.BOARD)
k.setwarnings(False)
seg=29
seg1=32
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
count=0
while(count<99):
    k.output(seg,k.HIGH)
    k.output(seg1,l.HIGH)
    for i in range(10):
        for j in range(10):
            k.output(list1[i],k.HIGH)
            k.output(list1[j],k.HIGH)
            sleep(1)
            k.output(list1[j],k.LOW)
            sleep(0.5)
            count+=1
        k.output(list1[i],k.HIGH)
        sleep(0.5)
k.cleanup()

