# ---------------------------------------
# Program 11: Swap Two Numbers
# Description: Swaps two numbers using a third variable.
# Author: Anugya Agrawal
# ---------------------------------------

number1 = float(input("Enter Number 1: "))
number2 = float(input("Enter Number 2: "))

print("Before:", number1, number2)

c = number1
number1 = number2
number2 = c

print("After swap:", number1, number2)

# ---------------------------------------
# SAMPLE INPUT
# Enter Number 1: 6
# Enter Number 2: 7
# ---------------------------------------

# SAMPLE OUTPUT
# Before: 6.0 7.0
# After swap: 7.0 6.0
# ---------------------------------------
