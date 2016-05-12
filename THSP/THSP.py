import sys
import Adafruit_DHT
import THSP_Functions

print('Relative Humidity: {2:0.1f}%'.format(THSP_Functions.getHumidity))
print('Temperature Celsius: {0:0.1f} degrees'.format(THSP_Functions.getTempCelsius))
print('Temperature Fahrenheit: {1:0.1f} degrees'.format(THSP_Functions.getTempFarenheit))
print('Relative Humidity: {2:0.1f}%'.format(THSP_Functions.getTempHumidity))
print('Temperature Celsius: {0:0.1f} degrees  \nTemperature Fahrenheit: {1:0.1f} degrees \nRelative Humidity: {2:0.1f}%'.format(THSP_Functions.getTempCelsius, THSP_Functions.getTempFarenheit, THSP_Functions.getTempHumidity))
