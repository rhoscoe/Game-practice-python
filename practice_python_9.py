# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 22:35:50 2017

@author: rosie_000

Exercise 9: Guessing game one
"""

import random

a = random.randint(1,9)



usr = raw_input("Make a guess between 1 and 9: ")

if int(usr) > a:
    print "Too big."
elif int(usr) < a:
    print "Too small."
else:
    print "Correct!"


"""Extra 1: keep going until the player types exit & Extra 2: keep count of the guesses made and print how many until the player exits"""

count = 0
comp = random.randint(1,9)
#print comp - for checking purposes

while True:
    player = (raw_input("Make a guess between 1 and 9, or type 'exit' to leave the game: "))
    if player == "exit":
        print("You made "+str(count)+" guesses.") #should fix grammar if 1 guess using an if statement
        break #break the loop and finish the game
    if int(player) > comp:
        print "Too big. Try again."
        count += 1 #add to count
        print("You made "+str(count)+" guesses.")#print count
    elif int(player) < comp:
        print "Too small. Try again."
        count += 1
        print("You made "+str(count)+" guesses.")
    else:
        print "You did it!"
        count += 1
        print("You made "+str(count)+" guesses.")
        playagain = (raw_input("Would you like to play again? Type 'yes', otherwise type 'exit' to leave the game: "))
        if playagain.lower() == "yes":
            count = 0 #reset count
            comp = random.randint(1,9) #get new random number and stay in the loop
        else:
            break #break the loop and finish the game
