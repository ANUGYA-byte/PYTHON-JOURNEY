# ---------------------------------------
# Program 90: Set Length and Element Check
# Description: Finds the length of a set and checks whether an element exists.
# Author: Anugya Agrawal
# ---------------------------------------

my_set = {10, 20, 30, 40, 50}

print("Set:", my_set)
print("Length of set:", len(my_set))

element = int(input("Enter an element to check: "))

if element in my_set:
    print("Element is present in the set.")
else:
    print("Element is not present in the set.")
