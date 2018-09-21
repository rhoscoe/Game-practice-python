# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:37:43 2017

@author: rosie_000

Exercise 25: Guessing Game Two.  You, the user, will have in your head a number between 0 
and 100. The program will guess a number, and you, the user, will say whether it is too 
high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.
"""

import random

guess = 0
a = 0
b = 100

while True:
    x = a + (b - a) // 2
    player = str(raw_input("Is this your number? "+str(x)+". Please enter 'too high', 'too low', or 'yes'."))
    player = player.lower()
    if player == "yes":
        guess +=1
        if guess < 2:
            print "Wow! The computer guessed it in "+str(guess)+ " guess."
            break
        else:
            print "Wow! The computer guessed it in "+str(guess)+ " guesses."
            break
    elif player == "too high":
        guess +=1
        b = x
    elif player == "too low":
        guess +=1
        a = x
    else:
        player = str(raw_input("I'm sorry, the value you entered is invalid. Please enter 'too high', 'too low', or 'yes'."))
    x = random.randint(a,b)