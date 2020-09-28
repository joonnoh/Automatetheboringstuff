#!/usr/bin/env python

# Opens several search results from pypi.org
# ./searchpypi.py [search term]

import requests, sys, webbrowser, bs4

# Parse the Pypi search results page using command line argument as search term
print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Retrieve results with common CSS Selector
linkElems = soup.select('.package-snippet')

# Number of tabs to open is the lesser of 5 or the number of search results
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	url = 'https://pypi.org' + linkElems[i].get('href')
	print('Opening ', url)
	webbrowser.open(url)