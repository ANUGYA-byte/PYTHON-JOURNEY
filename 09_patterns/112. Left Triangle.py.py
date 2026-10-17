# ---------------------------------------
# Program 84: Left Triangle
# Description:A triangle aligned to the right, stars shifted with spaces.
# Author: Anugya Agrawal
# ---------------------------------------

LENGTH=int(input('ENTER THE LENGTH '))
for i in range(1,LENGTH+1):
 print(" "*(LENGTH-i)+"*"*i)

# ---------------------------------------
#SAMPLE INPUT-
#ENTER THE LENGTH 5
# ---------------------------------------
#SAMPLE OUTPUT-
'''
    *
   **
  ***
 ****
*****'''
