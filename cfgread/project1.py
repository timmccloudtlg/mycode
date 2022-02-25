#!/usr/bin/env python3

import os
from datetime import date
def program():
    Year = input("year of birth:" )
    Month = input("month of birth:" )
    Day = input("day of birth:" )
    Date_of_Birth = (Day + "/" + Month + "/" + Year)
    print('Your Date of Birth is ' + Date_of_Birth)
    d = date.today()
    y =d.year
    os.system("cls")
    age = y - int(Year)
    print('Your age is ' + str(age))



def zodiac_sign():
    if (int(Month)==12<2):
         print("\n Capricorn")
    elif (int(Month)==1<3):
        print("\n aquarium")
    elif (int(Month)==2<4):
        print("\n Pices")
    elif(int(Month)==3<5):
        print ("\n Aries")
    elif(int(Month)==4<6):
        print("\n Taurus")
    elif(int(Month)==5<7):
        print("\n Gemini")
    elif(int(Month)==6<8):
        print("\n cancer")
    elif(int(Month)==7<9): 
        print ("\n leo")
    elif(int(Month)==8<9): 
        print ("\n virgo")
    elif(int(Month)==9<10):
        print ("\n libra")
    elif(int(Month)==10<12): 
        print ("\n Scorpio")
    elif(int(Month)==11<13):
        print("\n Sagittarius")

input()
program()

