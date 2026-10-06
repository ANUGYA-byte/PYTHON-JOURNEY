# ---------------------------------------
# Program 99: Factorial Using Recursion
# Description: Finds the factorial of a number using recursion.
# Author: Anugya Agrawal

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))

print("Factorial =", factorial(n))
