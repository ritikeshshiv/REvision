import RPi.GPIO as a
import time
a.setmode(a.BOARD)

trig=7
echo=11

print("Distance Measurement in Progress")

a.setup(trig,a.OUT)
a.setup(echo,a.IN)

a.output(trig,False)
print("Waiting for sensor to settle")

while True:
    time.sleep(2)
    a.output(trig,True)
    time.sleep(0.00001)
    a.output(trig,False)

    while a.input(echo)==0:
        pulse_start=time.time()

    while a.input(echo)==1:
        pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("Distance",distance,"cm")
a.cleanup()
