# ---------------------------------------
# Program 127: Count Spaces
# Description: Counts the number of whitespace characters in a string.  
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH LENGTH NEED TO BE FIND-")
COUNT=0
for i in STRING:
    if i.isspace():
        COUNT=COUNT+1
    else:
        COUNT=COUNT+0
print('Spaces Count-',COUNT)

# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE STRING WHICH LENGTH NEED TO BE FIND-python 3.13.14
# ---------------------------------------
#SAMPLE OUTPUT-
#Spaces Count- 1
