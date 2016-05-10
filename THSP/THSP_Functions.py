import sys
import Adafruit_DHT
import datetime
import sqlite3
import os
import glob

# Add explanation comment    
def getTempFarenheit():
    if humidity is not None and temperature is not None:
        #TODO Get Temp
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        # Convert celsius temperature to Fahrenheit
        tempFahrenheit = temperature * 9/5.0 + 32
    else:
        errorState = 1
        return errorState
    return tempFahrenheit

# Add explanation comment
def getTempCelsius():
    if humidity is not None and temperature is not None:
        #TODO Get Temp
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    else:
        errorState = 1
        return errorState
    return temperature

# Add explanation comment
def getHumidity():
    if humidity is not None and temperature is not None:
        #TODO Get Humididty
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    else:
        errorState = 1
        return errorState
    return humidity

# Add explanation comment
def getTempHumidity():
    if humidity is not None and temperature is not None:
        #TODO Get Humididty
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    else:
        errorState = 1
        return errorState
    return humidity, temperature

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