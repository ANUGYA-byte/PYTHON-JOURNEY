# ---------------------------------------
# Program 31: Percentage Calculator
# Description: Calculates total marks and percentage.
# Author: Anugya Agrawal
# ---------------------------------------

marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))
marks4 = float(input("Enter marks in subject 4: "))
marks5 = float(input("Enter marks in subject 5: "))

marks = [marks1, marks2, marks3, marks4, marks5]

if any(mark < 0 or mark > 100 for mark in marks):
    print("INVALID MARKS")
else:
    total = sum(marks)
    percentage = total / 5

    print("TOTAL MARKS -", total)
    print("PERCENTAGE -", percentage, "%")

# SAMPLE OUTPUT
# Enter marks in subject 1: 85
# Enter marks in subject 2: 90
# Enter marks in subject 3: 78
# Enter marks in subject 4: 88
# Enter marks in subject 5: 92
# TOTAL MARKS - 433.0
# PERCENTAGE - 86.6 %

