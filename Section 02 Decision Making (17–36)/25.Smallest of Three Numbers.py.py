# ---------------------------------------
# Program 25: Smallest of Three Numbers
# Description: Compares three numbers and finds the smallest value.
# Author: Anugya Agrawal
# --------------------------------------

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 == number2 == number3:
 print("All numbers are equal")
elif number1 <= number2 and number1 <= number3:
 print(number1, "Smallest number")
elif number2 <= number1 and number2 <= number3:
 print(number2, "Smallest number")
else:
 print(number3, "Smallest number")

# ---------------------------------------
# SAMPLE INPUT-
# Enter first number:  1
# Enter second number: 2
# Enter third number:  3
#
# SAMPLE OUTPUT-
# 1.0 SMALLEST NUMBER
#
# ---------------------------------------
# SAMPLE INPUT-
# Enter first number:  1
# Enter second number: 1
# Enter third number:  1
#
# SAMPLE OUTPUT-
# ALL NUMBERS ARE EQUAL
# ---------------------------------------
