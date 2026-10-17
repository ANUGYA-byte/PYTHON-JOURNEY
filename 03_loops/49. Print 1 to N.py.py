# ---------------------------------------
# Program 41:Print 1 to N
# Description:Prints numbers from 1 to N using a loop.
# Author: Anugya Agrawal
# ---------------------------------------

NUMBER = int(input("ENTER NUMBER - "))

# Using for loop
for i in range(1, NUMBER + 1):
    print(i)

# Using while loop
C = 1
while C <= NUMBER:
    print(C)
    C += 1

# ---------------------------------------
#SAMPLE -
#ENTER NUMBER -3
#1
#2
#3
#1
#2
#3
