#!/usr/bin/env python

# Python script to scrape top 5 cryptocurrencies by market cap from CoinMarketCap.com
# Presents data in PrettyTable format

import requests, bs4, prettytable
import datetime

print('Loading...')

# Print current date and time
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Parse the home page
res = requests.get('https://coinmarketcap.com')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Use browser's developer console to find CSS Selector for each item
name = soup.select('.iTmTiC')
marketCap = soup.select('.hVAibX')
price = soup.select('.jFRIev a')
change = soup.find_all('p', {'class':['gQeQTH', 'jRHnTF']})

# Initialize lists
nameList = []
marketCapList = []
priceList = []
changeList = []

# Add top five names and market caps 
for i in range(5):
	nameList.append(name[i].text)
	marketCapList.append(marketCap[i+1].text)
# Add top five prices
for i in range(1,20,4):
	priceList.append(price[i].text)
# Add top five changes
for i in range(0,10,2):
	if any('gQeQTH' in string for string in change[i].get('class')):
		changeList.append('+' + change[i].text)
	if any('jRHnTF' in string for string in change[i].get('class')):
		changeList.append('-' + change[i].text)

# Create and print organized table
t = prettytable.PrettyTable()
t.add_column('Name', nameList)
t.add_column('Market Cap', marketCapList)
t.add_column('Price', priceList)
t.add_column('Change(24h)', changeList)
print(t)