#!/usr/bin/env python

# Python script that opens first three search results from Google search 
# in new tabs using given arguments
# ./googleSearch.py [search term]

import requests, sys, webbrowser, bs4, re

# Parse the Google search results page using command line argument as search term
print('Searching...')
res = requests.get('https://google.com/search?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Retrieve top search result links
linkElems = soup.select('div#main > div > div > div > a')

# Iterate through search results and open first three links
# (not additional search results)
count = 0
for i in range(len(linkElems)):
	if count == 3:  # Change this value to however many links you want open
		break
	search = linkElems[i].get('href')
	if 'url' in search:
		url = re.findall(r'q=(.+?)&sa', search)
		print('Opening ', url)
		webbrowser.open(url[0])
		count += 1