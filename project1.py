#!/usr/bin/env python3


month = input("What month were you born?")
month.lower()
day = int(input("What day wery you born?"))
months = ["january", "feburary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

if month in months:
    if month == "january":
        sign = "Capricorn" if (day < 20) else "Aquarius" 
    elif month == "february":
        sign = "Aquarius" if (day < 19) else " Pices"
    elif month == "march":
        sign = " Pices" if (day < 21) else "Aries"
    elif month == "april":
        sign = "Aries" if (day < 20) else "Taurus"
    elif month == "may":
        sign = "Taurus" if (day <21) else "Gemini"
    elif month == "june":
        sign = "Gemini" if (day < 21) else "Cancer"
    elif month == "july":
        sign = "Cancer" if (day < 23) else "Leo"
    elif month == "august":
        sign = "Leo" if (day < 23) else "Virgo"
    elif month == "september":
        sign = "Virgo" if (day < 23) else "Libra"
    elif month == "october":
        sign = "Libra" if (day < 23) else "Scorpio"
    elif month == "november":
        sign = "Scropio" if (day < 23) else "Sagittarius"
    elif month == "december":
        sign = "Sagittarius" if (day < 20) else "Capricorn"

    print("Your zodiac sign is " + sign)
