# ---------------------------------------
# Program 26: Leap Year Check
# Description:Checks whether a given year is a leap year.
# Author: Anugya Agrawal
# ---------------------------------------

year = int(input("ENTER YEAR: "))

if year % 400 == 0:
    print(year, "IS A LEAP YEAR")
elif year % 100 == 0:
    print(year, "IS NOT A LEAP YEAR")
elif year % 4 == 0:
    print(year, "IS A LEAP YEAR")
else:
    print(year, "IS NOT A LEAP YEAR")
    
# ---------------------------------------
#SAMPLE -
#ENTER YEAR: 1200
#1200 IS A LEAP YEAR

# ---------------------------------------
#SAMPLE -
#ENTER YEAR: 1300
#1300 IS NOT A LEAP YEAR

# ---------------------------------------
#SAMPLE -
#ENTER YEAR: 2099
#2099 IS NOT A LEAP YEAR 
