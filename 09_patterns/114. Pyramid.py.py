# ---------------------------------------
# Program 86: Pyramid
# Description:A centered triangle with stars expanding symmetrically
# Author: Anugya Agrawal
# ---------------------------------------

LENGTH=int(input('ENTER THE LENGTH -'))
for i in range(1,LENGTH+1):
 print(" "*(LENGTH-i)+'*'*(2*i-1))

# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE LENGTH -5
# ---------------------------------------
#SAMPLE OUTPUT-
'''
    *
   ***
  *****
 *******
*********''' 
