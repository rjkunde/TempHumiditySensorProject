import sys
import Adafruit_DHT
import THSP_Functions

def main():   
    print('\n' * 2)
    print 'THSP_Functions Unit Tests'
    print('\n' * 2)

    testFarenheight()
    testCelsius()
    testHumidity()
    testAllStats()
    testSpecificStat()

def testFarenheight():
    print 'Testing THSP_Function getTempFarenheit():'
    tempFarenheight = THSP_Functions.getTempFarenheit()
    if tempFarenheight is not None and tempFarenheight > 30.0 and tempFarenheight < 120.0:
        print 'Test PASSED! The sensor value is: ', tempFarenheight
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', tempFarenheight
        print 'Sensor value must be between 30.0 and 120.0 degrees farenheight'
        print
   
def testCelsius():
    print 'Testing THSP_Function getTempCelsius():'
    tempCelsius = THSP_Functions.getTempCelsius()
    if tempCelsius is not None and tempCelsius > -5.0 and tempCelsius < 56.0:
        print 'Test PASSED! The sensor value is: ', tempCelsius
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', tempCelsius
        print 'Sensor value must be between -5.0 and 56.0 degrees celsius'
        print

def testHumidity():
    print 'Testing THSP_Function getHumidity():'
    humidity = THSP_Functions.getHumidity()
    if humidity is not None and humidity > 0.0 and humidity < 100.0:
        print 'Test PASSED! The sensor value is: ', humidity
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', humidity
        print 'Sensor value must be between 0.1 and 99.9 %'
        print

def testAllStats():
    print 'Testing THSP_Function getAllStats():'
    allStats = THSP_Functions.getAllStats()
    if (
         allStats is not None and
         allStats[0] < 120.0 and allStats[0] > 0.0 and
         allStats[1] < 56.0 and allStats[1] > -5.0 and
         allStats[2] > 0.0 and allStats[2] < 100.0
        ):
        print 'Test PASSED! The sensor value is: ', allStats
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', allStats
        print 'Sensor values must be 0.0-120.0, -5.0-56.0, 0.01-99.9 respectively'

def testSpecificStat():  
    print 'Testing THSP_Function getSpecificStat() w/ parameter: tempFarenheight'
    tempFahrenheit  = THSP_Functions.getSpecificStat('tempFahrenheit')
    if tempFahrenheit is not None and tempFahrenheit > 30.0 and tempFahrenheit < 120.0:
        print 'Test PASSED! The sensor value is: ', tempFahrenheit
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', tempFahrenheit
        print 'Sensor value must be between 30.0 and 120.0 degrees farenheit'
        print

    print 'Testing THSP Function getSpecificStat() w/ parameter: tempCelsius'
    tempCelsius  = THSP_Functions.getSpecificStat('tempCelsius')
    if tempCelsius is not None and tempCelsius > -5.0 and tempCelsius < 56.0:
        print 'Test PASSED! The sensor value is: ', tempCelsius
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', tempCelsius
        print 'Sensor value must be between -5.0 and 56.0 degrees celsius'
        print

    print 'Testing THSP Function getSpecificStat() w/ parameter: humidity'
    humidity  = THSP_Functions.getSpecificStat('humidity')
    if humidity is not None and humidity > 0.0 and humidity < 100.0:
        print 'Test PASSED! The sensor value is: ', humidity
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', humidity
        print 'Sensor value must be between 0.1 and 99.9 %'
        print

#Execute Test
if __name__ == "__main__":
	main()
