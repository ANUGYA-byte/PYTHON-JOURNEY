# ---------------------------------------
# Program 47:  Reverse Multiplication Table 
# Description: Show multiplication results in descending order
# Author: Anugya Agrawal
# ---------------------------------------
NUMBER = int(input("ENTER NUMBER - "))

# Using for loop
for i in range(10, 0, -1):
    print(NUMBER, "X", i, "=", NUMBER * i)

# Using while loop
C = 10
while C >= 1:
    print(NUMBER, "X", C, "=", NUMBER * C)
    C -= 1

# ---------------------------------------
#SAMPLE
"""ENTER NUMBER -5
5 X 10 = 50
5 X 9 = 45
5 X 8 = 40
5 X 7 = 35
5 X 6 = 30
5 X 5 = 25
5 X 4 = 20
5 X 3 = 15
5 X 2 = 10
5 X 1 = 5
5 X 10 = 50
5 X 9 = 45
5 X 8 = 40
5 X 7 = 35
5 X 6 = 30
5 X 5 = 25
5 X 4 = 20
5 X 3 = 15
5 X 2 = 10
5 X 1 = 5"""
