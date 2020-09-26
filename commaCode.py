#!/usr/bin/env python

# commaCode script takes list and returns readable string

# Initialize the list
yourList = ['spam', 'eggs', 'apple', 'banana']

# Initialize the final string to be returned
finalString = ''

if not yourList: # If the list is empty, let the user know 
    print("List is empty")
else:
    for n in range(0,len(yourList)):  # Iterate through the list and append item and comma to finalString
        if n == len(yourList)-1:      # At the end of the list, add 'and' before the last item
            finalString += "and " + yourList[n]
        else:
            finalString += yourList[n] + ", "
print(finalString) # Prints "spam, eggs, apple, and banana"
