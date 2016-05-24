import sys
import Adafruit_DHT
import THSP_Functions

def main():
    testHumidity()
    testCelsius()
    testFarenheight()
    testAllStats()
    
def testHumidity():
    print 'Testing THSP Function getHumidity()'
    humidity = 
    if THSP_Functions.getHumidity 
    
def testCelsius():
    
def testFarenheight():
    
def testAllStats():

    
    
# Query sensor, return Relative Humidity
print '{0} {1:0.1f}%'.format('Relative Humidity:',THSP_Functions.getHumidity())

# Query sensor, return Temperature in Celsius
print '{0} {1:0.1f} degrees'.format('Temperature Celsius:',THSP_Functions.getTempCelsius())

# Query sensor, return Temperature in Farenheight
print '{0} {1:0.1f} degrees'.format('Temperature Fahrenheit:',THSP_Functions.getTempFarenheit())

# Query sensor, return all statistics
print '<------------Accessing all sensors simultaneously (slower) ------------>'
print '{0} {1:0.1f} degrees\n{2} {3:0.1f} degrees\n{4} {5:0.1f}%'.format('Temperature Fahrenheit:',THSP_Functions.getTempFarenheit(),'Temperature Celsius:',THSP_Functions.getTempCelsius(),'Relative Humidity:',THSP_Functions.getHumidity())


