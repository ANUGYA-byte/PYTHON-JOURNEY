# ---------------------------------------
# Program 39: Divisibility Check
#  Checks whether one number is exactly divisible by another number.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------
number1 = int(input("ENTER NUMBER: "))
number2 = int(input("ENTER DIVISOR: "))

if number2 == 0:
    print("CANNOT DIVIDE BY ZERO")
elif number1 % number2 == 0:
    print(number1, "IS EXACTLY DIVISIBLE BY", number2)
else:
    print(number1, "IS NOT EXACTLY DIVISIBLE BY", number2)

# ---------------------------------------
# SAMPLE OUTPUT
# ENTER NUMBER: 123
# ENTER DIVISOR: 3
# 123 IS EXACTLY DIVISIBLE BY 3
# ---------------------------------------


