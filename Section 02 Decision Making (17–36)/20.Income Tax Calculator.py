# ---------------------------------------
# Program 33: Income Tax Calculator
# Description:Calculates income tax based on the given annual income and applicable tax rules.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------

income = float(input("ENTER ANNUAL INCOME: "))

if income < 0:
    print("INVALID INCOME")
else:
    tax = 0

    if income > 1000000:
        tax += (income - 1000000) * 0.30
        income = 1000000

    if income > 500000:
        tax += (income - 500000) * 0.20
        income = 500000

    if income > 250000:
        tax += (income - 250000) * 0.05

    print("INCOME TAX - ₹", tax)
# ---------------------------------------
#SAMPLE -
#ENTER YOUR INCOME-1287622
#TAX- ₹ 193143.3

# ---------------------------------------
#SAMPLE -
#ENTER YOUR INCOME-222222
#TAX- ₹ 0

