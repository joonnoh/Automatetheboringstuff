#!/usr/bin/env python

# Print weather information
# ./getWeather.py [location]

import os, json, requests, sys, datetime
from os.path import join, dirname
from dotenv import load_dotenv

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

weatherAPI = os.getenv('weatherAPI')

# Get location from command line arguments
if len(sys.argv) < 2:
    print('Usage: ./getWeather.py [city, 2 letter country code]')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download JSON data from OpenWeather
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (location, weatherAPI)
response = requests.get(url)
response.raise_for_status()

# Load JSON data in Python variable
weatherData = json.loads(response.text)

# Print weather
w = weatherData['list']
print('Current weather in %s: ' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])

