#!/usr/bin/env python

# Add bullet points to the beginning of each line of text in clipboard

import pyperclip

# Set clipboard content to text
text = pyperclip.paste()


lines = text.split('\n')       # Create list of each new line
for i in range(len(lines)):    # Iterate through list
    lines[i] = '* ' + lines[i] # Add asterisk to each line

text = '\n'.join(lines)  # Join list items into string
pyperclip.copy(text)  # Copy new bulleted list to clipboard

print('Your bulleted list is ready to paste:\n' + text)
