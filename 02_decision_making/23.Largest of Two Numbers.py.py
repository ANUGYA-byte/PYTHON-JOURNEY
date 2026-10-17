# ---------------------------------------
# Program 23: Largest of Two Numbers
# Description: Compares two numbers and finds the larger one.
# Author: Anugya Agrawal
# ---------------------------------------

number1= int(input("Enter first number: "))
number2= int(input("Enter second number: "))

if number1 > number2:
    print(number1, "Largest number")
elif number2 > number1:
    print(number2, "Largest number")
else:
    print("Both numbers are equal")

# ---------------------------------------
# SAMPLE INPUT-
# Enter first number: 2
# Enter second number: 2
#
# SAMPLE OUTPUT-
# Both numbers are equal
#
# ---------------------------------------
# SAMPLE INPUT-
# Enter first number: 23
# Enter second number: 2
#
# SAMPLE OUTPUT-
# 23.0 Largest number
#
# ---------------------------------------
# SAMPLE INPUT-
# Enter first number: 12
# Enter second number: 14
#
# SAMPLE OUTPUT-
# 14.0 Largest number
# ---------------------------------------
