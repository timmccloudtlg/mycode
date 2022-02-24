#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main(x):
    num= random.randint(1,100)
    main = 0
    while True:
        guess= int(input("Guess a number between 1 and 100 __"))

        if guess > num:
            print("Too high, try again!. __")

        elif guess < num:
            print("Too low, try again!")

        else:
            print("Correct!")
            break

main(3)
