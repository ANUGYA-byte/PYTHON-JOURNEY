# ---------------------------------------
# Program 118: Student Grade Management System
# Description: Calculates total, percentage, and grade of a student.
# Author: Anugya Agrawal
# ---------------------------------------

name = input("Enter student name: ")

marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
