#!/usr/bin/env python3
# import random module
import random
import time 
import spinning
 
# Print instruction
# performstring concatenation of string
print("\n\n\nYou are about to play Rock, Paper, Scissor? The rules for the game are as follows:")
time.sleep(3)
print("Rock vs Paper !!PAPER Wins!! ")
time.sleep(3)
print("Rock vs Scissor !!ROCK Wins!! ")
time.sleep(3)
print("Paper vs Scissor !!SCISSOR Wins!!")
time.sleep(6)

while True:
    print("\nEnter one of the following choices 1 for Rock, 2 for Paper, and 3 for Scissor.")
     
    # This is where the user enter his choice 
    choice = int(input("Your turn. Enter 1, 2, or 3: "))
    spinning.spin(3)
 
    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value
     
    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
         
 
    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
        time.sleep(3)
         
    # print user choice
    print("You have enterd: " + choice_name)
    time.sleep(3)
    print("\nNow its computer turn.......")
    time.sleep(3)
 
    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)
     
    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
 
    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
         
    print("The Computer's choice is: " + comp_choice_name)
    time.sleep(3)
 
    print("\nThe challenge is " + choice_name + " verses " + comp_choice_name)
    print("!!!FIGHT!!!")
    spinning.spin()
    spinning.spin()
 
    # condition for winning
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        print("\nPAPER WINS!!! => ", end = "")
        result = "Paper"
        time.sleep(2)
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("\nROCK WINS!!! =>", end = "")
        result = "Rock"
        time.sleep(2)
    else:
        print("\nSCISSOR WINS!!! =>", end = "")
        result = "Scissor"
        time.sleep(2)
 
    # Printing either user or computer wins
    if result == choice_name:
        print("<== !!!You Win!!! ==>")
        time.sleep(3)
    else:
        print("<== COMPUTER Wins ==>")
        time.sleep(3)

    print("\nDo you want to play again? (Y/N)")
    ans = input()
 
 
    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break
     
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")
