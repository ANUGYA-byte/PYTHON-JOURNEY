# ---------------------------------------
# Program 28: Alphabet, Digit or Special Character
# Description: Determines whether the entered character is an alphabet, digit, or special character.
# Author: Anugya Agrawal
# ---------------------------------------
character = input("Enter a character: ")

if len(character) != 1:
    print("ENTER ONLY ONE CHARACTER")
elif character.isalpha():
    print(character, "is an ALPHABET")
elif character.isdigit():
    print(character, "is a DIGIT")
else:
    print(character, "is a SPECIAL CHARACTER")


# ---------------------------------------
# SAMPLE 1
# ENTER THE CHARACTER: w
# w is an ALPHABET
# ---------------------------------------

# ---------------------------------------
# SAMPLE 2
# ENTER THE CHARACTER: 3
# 3 is a DIGIT
# ---------------------------------------

# ---------------------------------------
# SAMPLE 3
# ENTER THE CHARACTER: @
# @ is a SPECIAL CHARACTER

# ---------------------------------------

