# ---------------------------------------
# Program 130: Count Frequency 
#Description:Characters  Counts how many times each character appears in a string.
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH CHARACTERS NEED TO BE FIND-")
CHARACTER=input("ENTER THE CHARACTER WHICH COUNT NEED TO BE FIND-")
COUNT=0
for i in STRING:
    if CHARACTER==i:
        COUNT=COUNT+1
    else:
        COUNT=COUNT+0
print('Frequency  Count-',COUNT)


# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE STRING WHICH CHARACTERS NEED TO BE FIND-python 3.13.14
# ---------------------------------------
#SAMPLE OUTPUT-
#ENTER THE CHARACTER WHICH COUNT NEED TO BE FIND-3
#Frequency  Count- 2
