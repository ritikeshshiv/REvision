import sys
from Adafruit_Python_DHT-master import AdafruitDHT
from RPLCD import CharLCD
from RPi import GPIO
import time
GPIO.setwarnings(False)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
while True:
    humaidity, temperature=Adafruit_DHT.read_retry(11,4)
    time.sleep(2)
    lcd.write_string('Temp:{O:O.1f} C Humidity: {1:O.1f}%'.format(temperature,humidity))
    time.sleep(2)
    lcd.clear()
