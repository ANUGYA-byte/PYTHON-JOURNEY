# ---------------------------------------
# Program 32: Electricity Bill Calculator
# Description: Calculates electricity bill based on units consumed.
# Author: Anugya Agrawal
# ---------------------------------------

units = float(input("ENTER ELECTRICITY UNITS: "))

if units < 0:
    print("INVALID UNITS")
elif units <= 100:
    bill = units * 5
    print("ELECTRICITY BILL - ₹", bill)
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    print("ELECTRICITY BILL - ₹", bill)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    print("ELECTRICITY BILL - ₹", bill)

# SAMPLE OUTPUT
# ENTER ELECTRICITY UNITS: 250
# ELECTRICITY BILL - ₹ 1650.0


