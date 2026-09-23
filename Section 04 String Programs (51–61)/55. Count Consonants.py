# ---------------------------------------
# Program 125: Count Consonants
# Description: Counts the number of Consonants in a string 
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH CONSONANTS NEED TO BE COUNT-")
COUNT=0
for i in STRING:
    if i in 'AEIOUaeuio':
        COUNT=COUNT+0
    else:
        COUNT=COUNT+1
print('Consonants Count-',COUNT)

# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE STRING WHICH CONSONANTS NEED TO BE COUNT-python
# ---------------------------------------
#SAMPLE OUTPUT-
#Consonants Count- 5
