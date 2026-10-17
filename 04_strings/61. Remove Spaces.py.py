# ---------------------------------------
# Program 131: Remove Spaces 
#Description:Eliminates all whitespace characters from a string.
# Author: Anugya Agrawal
# ---------------------------------------
STRING=input("ENTER THE STRING WHICH CHARACTERS NEED TO BE FIND-")
REMOVED_SPACE_STRING=""

for i in STRING:
    if i.isspace():
        REMOVED_SPACE_STRING=REMOVED_SPACE_STRING+""
    else:
        REMOVED_SPACE_STRING=REMOVED_SPACE_STRING+i
print("REMOVED SPACE STRING-",REMOVED_SPACE_STRING)


# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE STRING WHICH CHARACTERS NEED TO BE FIND-pyt ho n 3. 13.  14
# ---------------------------------------
#SAMPLE OUTPUT-
#REMOVED SPACE STRING- python3.13.14
