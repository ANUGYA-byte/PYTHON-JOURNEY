# ---------------------------------------
# Program 123: Palindrome String  
# Description: Checks if a string reads the same forward and backward.
# Author: Anugya Agrawal
# ---------------------------------------

STRING=input("ENTER THE STRING WHICH PALINDROME NEED TO BE CHECK-")
REVERSESTRING=STRING[::-1]
if REVERSESTRING==STRING:
    print("IT IS Palindrome String  ")
else:
    print("IT IS NOT Palindrome String ")

    
# ---------------------------------------
#SAMPLE
#ENTER THE STRING WHICH PALINDROME NEED TO BE CHECK-QWEWQ
#IT IS Palindrome String 
# ---------------------------------------
#SAMPLE
#ENTER THE STRING WHICH PALINDROME NEED TO BE CHECK-QWE
#IT IS NOT Palindrome String 
