# ---------------------------------------
# Program 34: BMI Calculator
# Description: Calculates BMI using weight and height.
# Author: Anugya Agrawal
# ---------------------------------------

weight = float(input("ENTER YOUR WEIGHT IN kg: "))
height = float(input("ENTER YOUR HEIGHT IN m: "))

if weight <= 0 or height <= 0:
    print("INVALID INPUT")
else:
    bmi = weight / (height ** 2)

    print("BMI -", round(bmi, 2))

    if bmi <= 18.5:
        print("STATUS - UNDERWEIGHT")
    elif bmi <= 24.9:
        print("STATUS - NORMAL RANGE")
    elif bmi <= 29.9:
        print("STATUS - OVERWEIGHT")
    else:
        print("STATUS - OBESITY")

# ---------------------------------------
# SAMPLE OUTPUT
# ---------------------------------------
# ENTER YOUR WEIGHT IN kg: 60
# ENTER YOUR HEIGHT IN m: 1.70
# BMI - 20.76
# STATUS - NORMAL RANGE

