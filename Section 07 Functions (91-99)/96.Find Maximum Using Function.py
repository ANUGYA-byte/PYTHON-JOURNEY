# ---------------------------------------
# Program 97: Find Maximum Using Function
# Description: Finds the maximum of three numbers using a function.
# Author: Anugya Agrawal

def maximum(a, b, c):
    return max(a, b, c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum =", maximum(a, b, c))
