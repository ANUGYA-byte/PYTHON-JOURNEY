# ---------------------------------------
# Program 48:  Factorial  
# Description: Product of all positive integers up to a given number.
# Author: Anugya Agrawal
# ---------------------------------------

NUMBER = int(input("ENTER NUMBER - "))

if NUMBER < 0:
    print("FACTORIAL IS NOT DEFINED FOR NEGATIVE NUMBERS")
else:
    F1 = 1

    for i in range(1, NUMBER + 1):
        F1 *= i

    print("FACTORIAL-", F1)

    F2 = 1
    C = 1

    while C <= NUMBER:
        F2 *= C
        C += 1

    print("FACTORIAL-", F2)
# ---------------------------------------
#SAMPLE 
"""ENTER NUMBER -5
FACTORIAL- 120
FACTORIAL- 120"""
