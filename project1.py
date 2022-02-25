#!/usr/bin/env python3

def zodiac_sign(day, month):
   #Checks the
   # of a specified zodiac
   if month == 'january':
      zodiac_sign = 'Capricorn' if (day < 20) else 'aquarius'
      animal_sign = "You are the Goat" if (day <20) else "You are the Water Bearer"
   elif month == 'february':
      zodiac_sign = 'Aquarius' if (day < 19) else 'pisces'
      animal_sign = "You are the Water Bearer" if (day <20) else "You are the Fish"
   elif month == 'march':
      zodiac_sign = 'Pisces' if (day < 21) else 'aries'
      animal_sign = "You are the Fish" if (day <20) else "You are the Ram"
   elif month == 'april':
      zodiac_sign = 'Aries' if (day < 20) else 'taurus'
      animal_sign = "You are the Ram" if (day <20) else "You are the Bull"
   elif month == 'may':
      zodiac_sign = 'Taurus' if (day < 21) else 'gemini'
      animal_sign = "You are the Bull" if (day <20) else "You are the Twins"
   elif month == 'june':
      zodiac_sign = 'Gemini' if (day < 21) else 'cancer'
      animal_sign = "You are the Twins" if (day <20) else "You are the Crab"
   elif month == 'july':
      zodiac_sign = 'Cancer' if (day < 23) else 'leo'
      animal_sign = "You are the Crab" if (day <20) else "You are the Lion"
   elif month == 'august':
      zodiac_sign = 'Leo' if (day < 23) else 'virgo'
      animal_sign = "You are the Lion" if (day <20) else "You are the Virgin"
   elif month == 'september':
      zodiac_sign = 'Virgo' if (day < 23) else 'libra'
      animal_sign = "You are the Virgin" if (day <20) else "You are the Balance"
   elif month == 'october':
      zodiac_sign = 'Libra' if (day < 23) else 'scorpio'
      animal_sign = "You are the Balance" if (day <20) else "You are the Scorpion"
   elif month == 'november':
      zodiac_sign = 'scorpio' if (day < 22) else 'sagittarius'
      animal_sign = "You are the Scorpion" if (day <20) else "You are the Archer"
   elif month == 'december':
      zodiac_sign = 'Sagittarius' if (day < 22) else 'capricorn'
      animal_sign = "You are the Archer" if (day <20) else "Aquarius"
   print(zodiac_sign)
       print(animal_sign)
# Driver code
if __name__ == '__main__':
d = int(input("Enter Day ::>"))
m = input("Enter the Month ::>")
zodiac_sign(d, m)

