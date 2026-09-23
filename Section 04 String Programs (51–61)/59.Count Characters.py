# ---------------------------------------
# Program 129: Count Characters  
#Description:Counts all characters including letters, digits, and symbols.
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH CHARACTERS NEED TO BE FIND-")
COUNT=0
for i in STRING:
    if i.isspace():
        COUNT=COUNT+0
    else:
        COUNT=COUNT+1
print('Characters Count-',COUNT)


# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE STRING WHICH CHARACTERS NEED TO BE FIND-python 3.13.14
# ---------------------------------------
#SAMPLE OUTPUT-
#Characters Count- 13
