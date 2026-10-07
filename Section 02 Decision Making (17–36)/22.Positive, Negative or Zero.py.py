# ---------------------------------------
# Program 22: Positive, Negative or Zero
# Description: Determines whether a given number is positive, negative, or zero.
# Author: Anugya Agrawal
# ---------------------------------------

number = float(input("Enter Number: "))

if number > 0:
    print(number, "Number is Positive")
elif number < 0:
    print(number, "Number is Negative")
else:
    print(number, "Number is Zero")

# ---------------------------------------
# SAMPLE INPUT-
# Enter Number: 12
# SAMPLE OUTPUT-
# 12.0 Number is Positive
#
# ---------------------------------------
# SAMPLE INPUT-
# Enter Number: 11
# SAMPLE OUTPUT-
# -11.0 Number is Negative
#
# ---------------------------------------
# SAMPLE INPUT-
# Enter Number: 0
# SAMPLE OUTPUT-
# 0.0 Number is Zero
# ---------------------------------------
