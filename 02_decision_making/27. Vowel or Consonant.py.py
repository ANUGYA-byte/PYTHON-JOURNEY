# ---------------------------------------
# Program 27: Vowel or Consonant
# Description: Checks whether a given alphabet character is a vowel or consonant.
# Author: Anugya Agrawal
# ---------------------------------------

character = input("Enter a character: ")

if len(character) != 1 or not character.isalpha():
    print("INVALID INPUT")
elif character.lower() in "aeiou":
    print(character, "is a VOWEL")
else:
    print(character, "is a CONSONANT")
# ---------------------------------------
# SAMPLE INPUT-
# ENTER THE ALPHABET: W
#
# SAMPLE OUTPUT-
# W CONSONANT
#
# ---------------------------------------
# SAMPLE INPUT-
# ENTER THE ALPHABET: E
#
# SAMPLE OUTPUT-
# E is a VOWEL
# ---------------------------------------
