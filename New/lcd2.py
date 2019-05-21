from RPLCD import CharLCD
from RPi import GPIO
import time
GPIO.setwarnings(False)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.cursor_pos=(1,3)
time.sleep(2)
lcd.write_string('Hello World')
time.sleep(2)
lcd.clear()
