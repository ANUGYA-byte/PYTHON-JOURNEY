# ---------------------------------------
# Program 10: Find Remainder of Two Numbers
# Description: Finds the remainder using the modulus (%) operator.
# Author: Anugya Agrawal
# ---------------------------------------

number1 = float(input("Enter Number 1: "))
number2 = float(input("Enter Number 2: "))

if number2 == 0:
    print("Division by zero is not possible.")
else:
    remainder = number1 % number2
    print(f"Remainder of 2 Numbers: {remainder}")

# ---------------------------------------
# SAMPLE INPUT
# Enter Number 1: 9
# Enter Number 2: 5
# ---------------------------------------
# SAMPLE OUTPUT
# Remainder of 2 Numbers: 4.0
# ---------------------------------------

