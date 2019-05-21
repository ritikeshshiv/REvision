from RPLCD import CharLCD
from RPi import GPIO
import time
import RPi.GPIO as a

GPIO.setwarnings(False)
sensor=16

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
time.sleep(2)
lcd.clear()

a.setwarnings(False)
a.setup(sensor,a.IN)

lcd.write_string("Initializing Soil Sensor...")
time.sleep(12)
lcd.clear()
lcd.write_string("Soil sensor READY")
lcd.write_string(" ")

try:
    while 1:
        if a.input(sensor):
            a.output(led,True)
            lcd.clear()
            lcd.write_string("Motion detected")
            time.sleep(0.2)
            lcd.clear()
        else:
            a.output(led,False)

except keyboardInterrupt:
    a.cleanup()


