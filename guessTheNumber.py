#!/usr/bin/python3
# Guess the number game in Python

import random

winningNumber = random.randint(1,20)
print("I'm thinking of a number between 1 and 20")

correctGuess = False
while correctGuess == False:
	print('Guess the number: ')
	guess = int(input())
	if guess == winningNumber:
		print('You got it! The number was ' + str(winningNumber))
		correctGuess = True
	elif guess >= winningNumber:
		print('Your guess is too high')
	else:
		print('Your guess is too low')
