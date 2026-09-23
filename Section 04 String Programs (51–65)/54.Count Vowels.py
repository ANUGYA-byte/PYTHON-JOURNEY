# ---------------------------------------
# Program 124: Count Vowels  
# Description: Counts the number of vowels (a, e, i, o, u) in a string 
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH VOWELS NEED TO BE COUNT-")
COUNT=0
for i in STRING:
    if i in 'AEIOUaeuio':
        COUNT=COUNT+1
    else:
        COUNT=COUNT+0
print('Vowels Count-',COUNT)

# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE STRING WHICH VOWELS NEED TO BE COUNT-python
# ---------------------------------------
#SAMPLE OUTPUT-
#Vowels Count- 1
