import os
from datetime import date
def program():
    Year = input("year of birth:" )
    Month = input("month of birth:" )
    Day = input("day of birth:" )
    Date_of_Birth = (Day + "/" + Month + "/" + Year)
    print('Your Date of Birth is ' + Date_of_Birth)
    d = date.today()
    y = d.year
    os.system("cls")
    age = y - int(Year)
    print('Your age is ' + str(age))

    def zodiac_sign()
        if(int(Month)==12<2)
        print("\n Capricorn")
