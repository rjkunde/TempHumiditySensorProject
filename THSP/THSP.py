﻿import sys
import Adafruit_DHT
import THSP_Functions

print '{0} {1:0.1f}%'.format('Relative Humidity:',THSP_Functions.getHumidity())
print '{0} {1:0.1f} degrees'.format('Temperature Celsius:',THSP_Functions.getTempCelsius())
print '{0} {1:0.1f} degrees'.format('Temperature Fahrenheit:',THSP_Functions.getTempFarenheit())
print '{0} {1:0.1f} degrees {2} {1:0.1f} degrees {4} {1:0.1f}% {6}'.format('Temperature Fahrenheit:',THSP_Functions.getTempFarenheit(),'Temperature Celsius:',THSP_Functions.getTempCelsius(),'Relative Humidity:',THSP_Functions.getHumidity())
