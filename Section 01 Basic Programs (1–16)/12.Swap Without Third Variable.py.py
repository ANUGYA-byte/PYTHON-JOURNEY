# ---------------------------------------
# Program 12: Swap Without Third Variable
# Description: Swaps two numbers without using a third variable.
# Author: Anugya Agrawal
# ---------------------------------------

number1 = float(input("Enter Number 1: "))
number2 = float(input("Enter Number 2: "))

print("Before:", number1, number2)

number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2

#number1, number2 = number2, number1

print("After swap:", number1, number2)

# ---------------------------------------
# SAMPLE INPUT
# Enter Number 1: 12
# Enter Number 2: 14
# ---------------------------------------

# SAMPLE OUTPUT
# Before: 12.0 14.0
# After swap: 14.0 12.0
# ---------------------------------------
