import sys
import Adafruit_DHT
import THSP_Functions

def main():
    THSP_Functions.importConfig()
    testAllSensors()

    
    
def testAllSensors():
    print '{0} {1:0.1f}%'.format('Relative Humidity:',THSP_Functions.getHumidity())
    print '{0} {1:0.1f} degrees'.format('Temperature Celsius:',THSP_Functions.getTempCelsius())
    print '{0} {1:0.1f} degrees'.format('Temperature Fahrenheit:',THSP_Functions.getTempFarenheit())
    print '<------------Accessing all sensors simultanesouly (slower) ------------>'
    print '{0} {1:0.1f} degrees\n{2} {3:0.1f} degrees\n{4} {5:0.1f}%'.format('Temperature Fahrenheit:',THSP_Functions.getTempFarenheit(),'Temperature Celsius:',THSP_Functions.getTempCelsius(),'Relative Humidity:',THSP_Functions.getHumidity())
    sys.exit()
#Execute Test
if __name__ == "__main__":
	main()
