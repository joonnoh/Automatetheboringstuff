#! /usr/bin/env python

# Python script to launch a map in the browser using address as argument
# in command line or clipboard

import webbrowser, sys, pyperclip

# If an argument is given when running the script with command line
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])  # Address is string of arguments
 # If no arguments are given in the command line, copy clipboard content to address
else:
	address = pyperclip.paste()
# Print the address and ask user if web browser should open location in Google Maps
print('The address is: "' + address + '"')
openSite = input('Open Google Maps in web browser? (y/n): ')
if openSite == 'y':
	webbrowser.open("https://www.google.com/maps/place/" + address)