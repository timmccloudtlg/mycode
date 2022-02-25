#!/usr/bin/env python3

import csv

with open("pokedex.txt", "r") as pokemon:
    for x in csv.DictReader (pokemon):
        print(f'{x["Name"]} is a {x["Type 1"]} type Pokemon.')
        print(f'{x["Defense"]} Defense') 
        print(f'{x["Attack"]} Attack')

               

