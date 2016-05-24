import sys
import Adafruit_DHT
import THSP_Functions

def main():
    testFarenheight()
    testHumidity()
    testCelsius()
    testAllStats()
    testSpecificStat()

def testFarenheight():
    print ('Testing THSP Function getTempFarenheit')
    tempFarenheight = THSP_Functions.getTempFarenheit()
    if tempFarenheight is not None:
        print ('Test Passed! The sensor value is: ', tempFarenheight)
    else:
        print ('Test Failed!, the sensor value returned was: ', tempFarenheight)    

def testCelsius():
    print ('Testing THSP Function getTempCelsius')
    tempCelsius = THSP_Functions.getTempCelsius()
    if tempCelsius is not None:
        print ('Test Passed! The sensor value is: ', tempCelsius)
    else:
        print ('Test Failed!, the sensor value returned was: ', tempCelsius)

def testHumidity():
    print ('Testing THSP Function getHumidity')
    humidity = THSP_Functions.getHumidity()
    if humidity is not None:
        print ('Test Passed! The sensor value is: ', humidity)
    else:
        print ('Test Failed!, the sensor value returned was: ', humidity)

def testAllStats():
    print ('Testing THSP Function getAllStats')
    allStats = THSP_Functions.getAllStats()
    if allStats is not None:
        print ('Test Passed! The sensor value is: ', allStats)
    else:
        print ('Test Failed!, the sensor value returned was: ', allStats)

def testSpecificStat():
    print ('Testing THSP Function getSpecificStat, this may take a while...\n')
    
    print('Testing THSP Function getSpecificStat w/ parameter: tempFarenheight')
    tempFahrenheit  = THSP_Functions.getSpecificStat(tempFahrenheit)
    if tempFahrenheit is not None:
        print ('testSpecicStat test for tempFahrenheit passed!, with value:', tempFahrenheit)
    else:
        print ('testSpecicStat test for tempFahrenheit failed!, with value:', tempFahrenheit)

    print('Testing THSP Function getSpecificStat w/ parameter: tempCelsius')
    tempCelsius  = THSP_Functions.getSpecificStat(tempCelsius)
    if tempCelsius is not None:
        print ('testSpecicStat test for tempCelsius passed!, with value:', tempCelsius)
    else:
        print ('testSpecicStat test for tempCelsius failed, with value:', tempCelsius)

    print('Testing THSP Function getSpecificStat w/ parameter: humidity')
    humidity  = THSP_Functions.getSpecificStat(humidity)
    if humidity is not None:
        print ('testSpecicStat test for humidity passed!, with value:', humidity)
    else:
        print ('testSpecicStat test for humidity failed, with value:', humidity)

#Execute Test
if __name__ == "__main__":
	main()
