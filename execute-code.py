#!/usr/bin/python3 encoding=utf-8

import time
import os
from os.path import expanduser, exists
import lnetatmo
import json 

config_file = open(expanduser("~/.netatmo.credentials"), "r")
lnetatmo_config = json.loads(config_file.read())

try:
	station_name = lnetatmo_config['STATION']
except:
	station_name = ""

authorization = lnetatmo.ClientAuth()
weather = lnetatmo.WeatherStationData(authorization)

user = weather.user

print("Station owner : ", user.mail)
print("Data units    : ", user.unit)

for module, moduleData in weather.lastData(station=station_name, exclude=3600).items() :

        # Name of the module (or station embedded module)
        # You setup this name in the web netatmo account station management
        print(module)

        # List key/values pair of sensor information (eg Humidity, Temperature, etc...)
        for sensor, value in moduleData.items() :
            # To ease reading, print measurement event in readable text (hh:mm:ss)
            if sensor == "When" : value = time.strftime("%H:%M:%S",time.localtime(value))
            print("%30s : %s" % (sensor, value))
