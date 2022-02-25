#!/usr/bin/env python3

import csv

with open("pokedex.txt", "r") as pokemon:
    for x in csv.DictReader (pokemon):
        print(f'{x["Name"]} is a {x["Type 1"]} type Pokemon.')
        print(f'\t{x["Defense"]} Defense') 
        print(f'\t{x["Attack"]} Attack')
        print(f'\t{x["Defense"]}+{x["Attack"]} I am a Powerful Pokemon')
        # Change the sum into integers
        # if sum =<150 print("I am a powerful Pokemon.")
        # else print("I am a weak Pokemon.") 
        print("\n")



               

