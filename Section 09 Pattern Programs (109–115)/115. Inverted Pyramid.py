
# ---------------------------------------
# Program 87:Inverted Pyramid
# Description:A centered triangle pointing downward, stars shrinking symmetrically
# Author: Anugya Agrawal
# ---------------------------------------

LENGTH = int(input("ENTER THE LENGTH: "))

for i in range(LENGTH, 0, -1):
    print(" " * (LENGTH - i) + "*" * (2 * i - 1))

# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE LENGTH -5
# ---------------------------------------
#SAMPLE OUTPUT-
'''
*********
 *******
  *****
   ***
    *''' 
