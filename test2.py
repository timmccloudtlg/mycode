#!/usr/bin/env python3
import random


def play():
    #This function defines the input for the user and uses random.choice fro the computer to choose.
    user = input("Welcome to Rock, Paper, Scissor. Please choose 'r' for rock, 'p' for paper, 's' for scissors.\n")
    computer = random.choice(['r', 'p', 's'])



if user == computer:
    return 'TIE'

if is_win(user, computer):
    return 'you win'

    return 'you lose'

    #The code below is an "if" loop that returns value true if:
                #Player is r and Opponent is s
                #Player is s and Opponent is p
                #Player is p and Opponent is r
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return true
    # r > s, s > p, p > r

    #This function define win for the player
    #This code returns the word tie if the user and the computer choose the same input
    #if user == computer:
        return 'Tie'


    #This code returns the words "You win!!!" if the play/Opponent =  r/s, s/p,p/r
    #if is_win(user, computer):
        return 'You win!!!'

    #return 'You Loose'


print(play()) 
