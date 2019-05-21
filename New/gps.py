import os
import time
import serial
import string
import pynmea2

while True:
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.2) #open a port
    datout=pynmea2.NMEAStreamReader()
    newdata=ser.readline()
    time.sleep(1)
    if(newdata.startswith('$GPGGA')):
        newmsg=pynmea2.parse(newdata)
        print("Get Latitude & Longitude")
        lat=newmsg.latitude
        print(lat)
        print(" and ")
        lng=newmsg.longitude
        print(lng)
time.sleep(15)
