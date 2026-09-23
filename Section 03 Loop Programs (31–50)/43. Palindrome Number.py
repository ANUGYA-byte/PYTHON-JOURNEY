# ---------------------------------------
# Program 53: Palindrome Number  
# Description: Check if a number reads the same both ways using str(num) == str(num)[::-1].
# Author: Anugya Agrawal
# ---------------------------------------

NUMBER=int(input('ENTER NUMBER-'))
REVERSENUMBER=str(NUMBER)[::-1]
print('REVERSE NUMBER-',REVERSENUMBER)
if REVERSENUMBER==str(NUMBER):
 print('Palindrome Number -',NUMBER)
else:
 print('NOT Palindrome Number -',NUMBER)

# ---------------------------------------
#SAMPLE -
'''ENTER NUMBER-3456543
REVERSE NUMBER- 3456543
Palindrome Number - 3456543'''

'''ENTER NUMBER-345
REVERSE NUMBER- 543
NOT Palindrome Number - 345'''
