from gpiozero import MCP3208, LED
from time import sleep
deg = chr(176)+'C'
tmp = MCP3208(channel=0, device=0)
red = LED(19)
 
while True:
    temperature = (tmp.value * 3.3 - 0.5)*100
    print(temperature)
    #temperature=tmp.value/0.02793
    #if temperature >24:
       # red.on()
    #else:
       # red.off()
    #print('{:.1f}'.format(temperature), deg, 10 * ' ')
    sleep(0.1)
 
############
#  This would show you the voltage from the TMP36
#    print(tmp.value * 3.3, " V")   # Voltage
#  This would show you the temperature to lots of dp
#    print((tmp.value * 3.3 - 0.5)*100, " C ")

