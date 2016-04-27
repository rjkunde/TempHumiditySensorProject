import sys
import Adafruit_DHT

# Specify AM203 Sensor on Raspberry Pi GPIO pin #4 (Physical Pin 7)
sensor = Adafruit_DHT.AM2302
pin = '4'

# Attempt to read sensor.  Uses read_retry method, trying up to 15 times. 
# Store results as variables.
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Convert celsius temperature to Fahrenheit
tempFahrenheit = temperature * 9/5.0 + 32 

# Check for valid inputs before displaying results
# Print result to screen
if humidity is not None and temperature is not None and tempFahrenheit is not None:
    print('Temp Celsius = {0:0.1f} degrees  \nTemp Fahrenheit = {0:0.1f}  degrees \nRelative Humidity = {1:0.1f}%'.format(temperature, tempFahrenheit, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
