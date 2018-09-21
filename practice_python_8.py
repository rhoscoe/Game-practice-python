# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:39:55 2017

@author: rosie_000

Exercise 8: Rock, Paper, Scissors
"""
import random

win = 0

options = ["rock", "scissors", "paper"]

while True:
    player = str(raw_input("Choose rock, scissors or paper, or q to quit: "))
    comp = random.choice(options)
    if player == comp:
        print "Same move! Try again."
    elif player == "rock" and comp == "scissors":
        print "The player wins! Let's play again."
        win +=1.0
        print ("Wins: "+str(win))
    elif player == "scissors" and comp == "paper":
        print "The player wins! Let's play again."
        win +=1.0
        print ("Wins: "+str(win))
    elif player == "paper" and comp == "rock":
        print "The player wins! Let's play again."
        win +=1.0
        print ("Wins: "+str(win))
    elif player == "q":
        break
    else:
        print "The computers wins this time. Try again."
    



