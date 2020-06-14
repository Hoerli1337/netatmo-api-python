#!/usr/bin/python3
# encoding=utf-8
#
# This File show all Stations, that are connectet to your Account
# For the query to work, a valid API key and login must be entered in the .netatmo-credentials

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

# Output example
# Station owner : Your E-Mail
# Data units : metric
# Station-Name1 : AA:BB:CC:DD:EE:FF
# Station-Name2 : GG:HH:II:JJ:KK:LL
