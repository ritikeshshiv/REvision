from RPLCD import CharLCD
from RPi import GPIO

import time
GPIO.setwarnings(False)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
time.sleep(2)
lcd.write_string('Hello\n\rWorld')
time.sleep(2)
lcd.clear()
