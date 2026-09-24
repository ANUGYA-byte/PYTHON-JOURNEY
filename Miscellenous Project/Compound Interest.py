# ---------------------------------------
# Program 19: Compound Interest
# Description: Calculates compound interest.
# Author: Anugya Agrawal
# ---------------------------------------

# Program 19: Compound Interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (years): "))
n = int(input("Enter number of times compounded per year: "))

if principal < 0 or rate < 0 or time < 0:
    print("Invalid input.")
elif n <= 0:
    print("Number of compounding times must be greater than 0.")
else:
    amount = principal * (1 + rate / (100 * n)) ** (n * time)
    compound_interest = amount - principal

    print("Compound Interest:", round(compound_interest, 2))
    print("Total Amount:", round(amount, 2))
# ---------------------------------------
# SAMPLE INPUT-
'''
Enter principal amount: 2300
Enter rate of interest: 3
Enter time (Year): 4
Enter number of times compounded per year: 2
'''
# ---------------------------------------
# SAMPLE INPUT-
'''Compound Interest: 290.93
Total Amount - 2590.93
''
