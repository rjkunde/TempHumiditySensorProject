import sys
import Adafruit_DHT
import THSP_Functions

def main():
   
    print
    print
    print 'THSP_Functions Unit Tests'
    print
    print

    testFarenheight()
    testCelsius()
    testHumidity()
    testAllStats()
    testSpecificStat()

def testFarenheight():
    print 'Testing THSP_Function getTempFarenheit():'
    tempFarenheight = THSP_Functions.getTempFarenheit()
    if tempFarenheight is not None:
        print 'Test PASSED! The sensor value is: ', tempFarenheight
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', tempFarenheight
        print
   
def testCelsius():
    print 'Testing THSP_Function getTempCelsius():'
    tempCelsius = THSP_Functions.getTempCelsius()
    if tempCelsius is not None:
        print 'Test PASSED! The sensor value is: ', tempCelsius
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', tempCelsius
        print

def testHumidity():
    print 'Testing THSP_Function getHumidity():'
    humidity = THSP_Functions.getHumidity()
    if humidity is not None:
        print 'Test PASSED! The sensor value is: ', humidity
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', humidity
        print

def testAllStats():
    print 'Testing THSP_Function getAllStats():'
    allStats = THSP_Functions.getAllStats()
    if allStats is not None:
        print 'Test PASSED! The sensor value is: ', allStats
        print
    else:
        print 'Test FAILED!, the sensor value returned was: ', allStats
        print

def testSpecificStat():  
    print 'Testing THSP_Function getSpecificStat() w/ parameter: tempFarenheight'
    tempFahrenheit  = THSP_Functions.getSpecificStat('tempFahrenheit')
    if tempFahrenheit is not None:
        print 'Test for tempFahrenheit PASSED!, with value: ', tempFahrenheit
        print
    else:
        print 'Test for tempFahrenheit FAILED!, with value: ', tempFahrenheit
        print

    print 'Testing THSP Function getSpecificStat() w/ parameter: tempCelsius'
    tempCelsius  = THSP_Functions.getSpecificStat('tempCelsius')
    if tempCelsius is not None:
        print 'Test for tempCelsius PASSED!, with value: ', tempCelsius
        print
    else:
        print 'Test for tempCelsius FAILED, with value: ', tempCelsius
        print

    print 'Testing THSP Function getSpecificStat() w/ parameter: humidity'
    humidity  = THSP_Functions.getSpecificStat('humidity')
    if humidity is not None:
        print 'Test for humidity PASSED!, with value: ', humidity
        print
        print
    else:
        print 'Test for humidity FAILED, with value: ', humidity
        print
        print

#Execute Test
if __name__ == "__main__":
	main()
