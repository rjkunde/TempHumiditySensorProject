import sys
import Adafruit_DHT
import datetime
import sqlite3
import os
import glob
import configparser

# Read ./config.ini file
try:
    from configparser import ConfigParser
except ImportError:
    from configparser import ConfigParser

# Instantiate
config = ConfigParser()
# Read config.ini
config.read('config.ini')

# Global variable 
errorState = None

# Specify AM203 sensor on Raspberry Pi GPIO pin #4 (physical pin 7)
# Detecting Pi version / beaglebone is handled by Adafruit DHT library
sensor = Adafruit_DHT.AM2302
pin = '4'
   
def getTempFarenheit():
    global errorState
    # Poll sensor, obtain humidity and temperature
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        # Convert Celsius Temperature to Fahrenheit
        tempFahrenheit = temperature * 9/5.0 + 32
        # Reset errorState
        errorState = None
    else:
        errorState = 'Failed to obtain temperature in farenheit; humididty or temperature are NULL'
        return errorState
    return tempFahrenheit

def getTempCelsius():
    global errorState
    if humidity is not None and temperature is not None:
        # Poll sensor, obtain humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    else:
        errorState = 'Failed to obtain temperature in celsius; humidity or temperature are NULL'
        return errorState
    return tempCelsius

def getHumidity():
    global errorState
    if humidity is not None and temperature is not None:
        # Poll sensor, obtain humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    else:
        errorState = 'Failed to obtain humidity; humidity or temperature are NULL'
        return errorState
    return humidity

def getTempHumidity():
    global errorState
    if humidity is not None and temperature is not None:
         # Poll sensor, obtain humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # Convert celsius to farenheit
        tempFahrenheit = temperature * 9/5.0 + 32
        # Change var name for clarity
        tempCelsius = temperature
        tempHumidity = humidity, tempCelsius, tempFahrenheit
    else:
        errorState = 'Failed to obtain temperature and humidity; humidity or temperature are NULL'
        return errorState
    return tempHumidity

# Add explanation comment
def storeLocalDB():
    #store passed reading into local DB structure
    #make sure to include error state in DB
    # get database information from ini file. localdb from.ini
    # see example below

    # Connect to Database
    # connection = sqlite3.connect('/home/pi/Desktop/Python_SI1145-master/production/SensorData.db')
    # cursor = connection.cursor()
    
    # Place values into database
	# cursor.execute("INSERT INTO sensors values(?,?,?,?,?);",(currentTime, vis, IR, UV,uvIndex))
	# connection.commit()
    return 0

# Add explanation comment
def storeRemoteDB():
    #store passed reading into the remote database
    #make sure to include error state in DB
    # LOOK UP LIBRARY / Functions to use SQL server over the network
    return 0

# Add explanation comment
def scanThresholds():
    #determine if temperature or humidity are outside of allowed values for an extended period of time.
    # example: temperature exceeds 74.0 degrees F OR XX Celcius for 2.0 minutes
    # humidity exceeds x %, for X time, etc etc
    # return a value to indicate in thresholds, out of thresholds, or error state
    return 0

# Add explanation comment
def generateAlert():
    # take output from scanThresholds, and do something with it.
    # email & or text the result
    # this will need to call a separate file/library for the email / text message creation
    return 0