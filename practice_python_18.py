# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:08:49 2017

@author: rosie_000

Exercise 18: Generate a random 4 digit number and play cows and bulls with the user.
For each number the user inputs, for a correct digit in the right place, there is a cow.
For a correct number in the wrong place, there is a bull
"""

import random

def cnb():
    count = 0
    cows = 0
    bulls = 0
    comp = str(random.randint(0,9999)).zfill(4)
    print comp
    while True:
        cows = 0
        bulls = 0
        player = str(raw_input("Please enter any four digit number: "))
        for x in range(0,4):
            if player[x] == comp[x]:
                print player[x]
                print comp[x]
                cows = cows + 1
                print "cows "+str(cows)
            elif player[x] in comp:
                print player[x]
                print comp[x]
                bulls = bulls +1
                print "bulls " + str(bulls)
        if cows == 4:
            count= count +1
            print "You guessed correctly! Well done. You made "+str(count)+" guesses."
            break
        if player == "exit":
            break
        if cows != 4:
            count = count + 1
            print "You have "+str(cows)+" cows and "+str(bulls)+" bulls. Try again. You've made "+str(count)+" guesses."
 
if __name__ == "__main__":
     print "let's play Cows and Bulls!"
     cnb()
    
    