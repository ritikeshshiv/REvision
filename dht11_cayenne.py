

#!/usr/bin/python


import Adafruit_DHT
import cayenne.client
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "d46a22d0-785c-11e8-861b-e79eceb83d4e"
MQTT_PASSWORD  = "e2326fba9b2b18ba982dd3690f54a58a983ce022"
MQTT_CLIENT_ID = "741b6b30-7962-11e8-861b-e79eceb83d4e"

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 14

while True:
  client.loop()

  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    client.celsiusWrite(1, temperature)
    client.luxWrite(2, humidity)
  else:
    print('Failed to get reading. Try again!')
