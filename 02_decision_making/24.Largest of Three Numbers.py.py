# ---------------------------------------
# Program 24: Largest of Three Numbers
# Description: Compares three numbers and finds the largest value.
# Author: Anugya Agrawal
# ---------------------------------------

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 == number2 == number3:
 print("All numbers are equal")
elif number1 >= number2 and number1 >= number3:
 print(number1, "Largest number")
elif number2 >= number1 and number2 >= number3:
 print(number2, "Largest number")
else:
 print(number3, "Largest number")



# ---------------------------------------
# SAMPLE INPUT-
# Enter first number:  5
# Enter second number: 5
# Enter third number:  3
#
# SAMPLE OUTPUT-
# 5 Largest number
# ---------------------------------------
