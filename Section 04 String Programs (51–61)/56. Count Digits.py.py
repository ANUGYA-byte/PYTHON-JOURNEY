# ---------------------------------------
# Program 126: Count Digits  
# Description: Counts how many numeric digits are present in a string.
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH DIGITS NEED TO BE COUNT-")
COUNT=0
for i in STRING:
    if i.isdigit() :
        COUNT=COUNT+1
    else:
        COUNT=COUNT+0
print('Digits Count-',COUNT)

# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE STRING WHICH DIGITS NEED TO BE COUNT-python3.13
# ---------------------------------------
#SAMPLE OUTPUT-
#Digits  Count- 3


