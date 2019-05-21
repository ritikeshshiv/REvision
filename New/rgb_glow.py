import RPi.GPIO as a
from time import sleep
a.setmode(a.BOARD)
a.setwarnings(False)
red=31
green=32
blue=33
a.setup(red,a.OUT)
a.setup(green,a.OUT)
a.setup(blue,a.OUT)
print("Press 1: For glow all LED\nPress 2: For glow particular LED\n")
n=int(input("Enter Your Choice: "))
if(n==1):
    while(n==1):
        a.output(red,True)
        sleep(1)
        a.output(red,False)
        a.output(green,True)
        sleep(1)
        a.output(green,False)
        a.output(blue,True)
        sleep(1)
        a.output(blue,False)
        n=int(input("Press 1 to continue and for exit press any numeric key: "))
elif(n==2):
    while(1):
        print("\nPress 1: For RED LED\nPress 2: For GREEN LED\nPress 3: For BLUE LED\n")
        K=int(input("Enter Your Choice: "))
        if(K==1):
            a.output(red,True)
            sleep(2)
            a.output(red,False)
        elif(K==2):
            a.output(green,True)
            sleep(2)
            a.output(green,False)
        elif(K==3):
            a.output(blue,True)
            sleep(2)
            a.output(blue,False)
        else:
            print("Enter a wrong choice, Try Again...\n")
            break;
else:
    print("\nEnter Wrong Choice\nGood Bye...")          
a.cleanup()