# ---------------------------------------
# Program 5: Print ASCII Values
# Description:
# This program accepts a single character from the user and displays its corresponding ASCII value using the built-in ord() function.
# Author: Anugya Agrawal
# Date: July 2026
# ---------------------------------------

character = input("Enter a character: ")

if len(character) == 1:
    print(f"ASCII value of '{character}' is {ord(character)}")
else:
    print("Please enter only one character.")

# ---------------------------------------
#SAMPLE INPUT AND OUTPUT
# ---------------------------------------
'''
Enter a character: A
ASCII value of 'A' is 65

Enter a character: AA
Please enter only one character.

Enter a character: e
ASCII value of 'e' is 101

Enter a character: 3
ASCII value of '3' is 51
'''

