fir se changeimport RPi.GPIO as a
import time as sleep
but=19
led=21
a.setmode(a.BOARD)
a.setwarnings(False)
a.setup(but,a.IN,pull_up_down = a.PUD_DOWN)
a.setup(led,a.OUT)
while 1:
 butstate = a.input(but)
 if (butstate == True):
  a.output(led,True)
  while a.input(but) == False:
    sleep(2)
 else:
  a.output(led,False)
a.output(led,False)
a.cleanup()


