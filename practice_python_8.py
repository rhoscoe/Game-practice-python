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
    player = str(raw_input("Choose rock, scissors or paper, or q to quit: ")) #asks for user input
    comp = random.choice(options) #chooses a random option from rock, scissors or paper
    if player == comp:
        print "Same move! Try again."
    elif player == "rock" and comp == "scissors": #this and the following two elif statements only cover when the player wins
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
    else: #all situations in which the player can win or draw are covered above
        print "The computers wins this time. Try again."
    



