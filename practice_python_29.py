# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:58:34 2017

@author: rosie_000

Exercise 29: Tic Tac Toe Game. Combining all the previous exercises to make a programme
that runs Tic Tac Toe
"""

"""em_game = [[0, 0, 0] for x in range(3)] #empty set of lists which will take players moves then change them to noughts and crosses

def draw_line(width, edge, filling):
	print(filling.join([edge] * (width + 1)))



def start_game():
	return [[0, 0, 0] for x in range(3)]
ga = start_game()
 


def display_game(game):
	d = {2: "O", 1: "X", 0: "_"}
	draw_line(3, " ", "_") #top line of the grid
	for row_num in range(3):
		new_row = []
		for col_num in range(3):
			new_row.append(d[game[row_num][col_num]]) #this part determines whether _, O or X should be in that space
		print("|" + "|".join(new_row) + "|")

display_game(ga)

new = ['X']
print("|" + "".join(new) + "|")"""

em_game = [[0, 0, 0] for x in range(3)] #empty set of lists which will take players moves then change them to noughts and crosses



"""def play1_value():
    play1 = raw_input("Player 1, please enter your move in the format: row, col: ")
    play1_list = play1.split(",")
    row1 = int(play1_list[0]) - 1
    col1 = int(play1_list[1]) - 1
    if em_game[row1][col1] == 0:
        em_game[row1][col1] = 1
    else:
        print "Square taken, try again!" """

def draw_line(width, edge, filling):
	print(filling.join([edge] * (width + 1)))

def display_game(game):
	d = {2: "O", 1: "X", 0: "_"}
	draw_line(3, " ", "_") #top line of the grid
	for row_num in range(3):
		new_row = []
		for col_num in range(3):
			new_row.append(d[game[row_num][col_num]]) #this part determines whether _, O or X should be in that space
		print("|" + "|".join(new_row) + "|")

#check if there's a winner

def ttt_check(game):
        global win
        if game[0][1] == game[1][1] == game[2][1] == 1:
            print "Player 1 has won!"
            win =1
            return win
        elif game[0][1] == game[1][1] == game[2][1] == 2:
            print "Player 2 has won!"
            win=1
            return win
        elif game[0][2] == game[1][2] == game[2][2] == 1:
            print "Player 1 has won!"
            win=1
            return win
        elif game[0][2] == game[1][2] == game[2][2] == 2:
            print "Player 2 has won!"
            win=1
            return win
        elif game[0][0] == game[1][0] == game[2][0] == 1:
            print "Player 1 has won!"
            win=1
            return win
        elif game[0][0] == game[1][0] == game[2][0] == 2:
            print "Player 2 has won!"
            win=1
            return win
        elif game[0][0] == game[1][1] == game[2][2] == 1:
            print "Player 1 has won!"
            win=1
            return win
        elif game[0][0] == game[1][1] == game[2][2] == 2:
            print "Player 2 has won!"
            win=1
            return win
        elif game[0][2] == game[1][1] == game[2][0] == 1:
            print "Player 1 has won!"
            win=1
            return win
        elif game[0][2] == game[1][1] == game[2][0] == 2:
            print "Player 2 has won!"
            win=1
            return win
        else:
            for i in game:
                if i[0] == i[1] == i[2] == 1:
                    print "Player 1 has won!"
                    win=1
                    return win
                elif i[0] == i[1] == i[2] == 2:
                    print "Player 2 has won!"
                    win=1
                    return win



"""def play2_value():
    play2 = raw_input("Player 2, please enter your move in the format: row, col: ")
    play2_list = play2.split(",")
    row2 = int(play2_list[0]) - 1
    col2 = int(play2_list[1]) - 1
    if em_game[row2][col2] == 0:
        em_game[row2][col2] = """

if __name__=="__main__":
    c = 9
    win = ttt_check(em_game)
    while c >= 0:
        if c == 0:
            print "No moves left!"
            break
        elif c%2 == 0:
            play1 = raw_input("Player 2, please enter your move in the format: row, col: ")
            play1_list = play1.split(",")
            row1 = int(play1_list[0]) - 1
            col1 = int(play1_list[1]) - 1
            if em_game[row1][col1] == 0:
                em_game[row1][col1] = 1
                c -=1
                print c
            else:
                print "Square taken, try again!"
            display_game(em_game)        
            ttt_check(em_game)
            if win == 1:
                break
        elif c%2 != 0:
            play2 = raw_input("Player 1, please enter your move in the format: row, col: ")
            play2_list = play2.split(",")
            row2 = int(play2_list[0]) - 1
            col2 = int(play2_list[1]) - 1
            if em_game[row2][col2] == 0:
                em_game[row2][col2] = 2
                c-=1
                print c
            else:
                print "Square taken, try again!"
            display_game(em_game)
            ttt_check(em_game)
            if win == 1:
                break
