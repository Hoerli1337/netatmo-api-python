#!/usr/bin/python3
# encoding=utf-8

import time
import lnetatmo

authorization = lnetatmo.ClientAuth()
weather = lnetatmo.WeatherStationData(authorization)

user = weather.user

print("Station owner : ", user.mail)
print("Data units    : ", user.unit)

# For each station in the account
for station in weather.stations:

	print(weather.stations[station]["station_name"] + " -> " +station)
	continue

