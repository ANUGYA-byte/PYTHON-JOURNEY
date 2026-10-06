# ---------------------------------------
# Program 93: Palindrome Using Function
# Description: Checks whether a number is a palindrome using a function.
# Author: Anugya Agrawal

def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = int(input("Enter a number: "))

if is_palindrome(n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
