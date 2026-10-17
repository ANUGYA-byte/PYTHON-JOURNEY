# ---------------------------------------
# Program 29:Uppercase or Lowercase 
# Description:Checks whether a given alphabet is uppercase or lowercase.
# Author: Anugya Agrawal
# ---------------------------------------

character = input("Enter an alphabet: ")

if len(character) != 1 or not character.isalpha():
    print("INVALID INPUT")
elif character.isupper():
    print(character, "is UPPERCASE")
else:
    print(character, "is LOWERCASE") 


# ---------------------------------------
#SAMPLE -
#Enter the alphabet-w
#w is LOWERCASE
# ---------------------------------------
#SAMPLE -
#Enter the alphabet-A
#A is UPPERCASE
