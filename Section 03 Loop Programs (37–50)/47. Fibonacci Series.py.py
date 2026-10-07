# ---------------------------------------
# Program 49: Fibonacci Series 
# Sequence where each term is the sum of the two preceding ones
# Author: Anugya Agrawal
# ---------------------------------------
NUMBER = int(input("ENTER NUMBER - "))

A = 0
B = 1

for i in range(NUMBER):
    print(A, end=" ")
    A, B = B, A + B

print()
    
#ENTER NUMBER-5
#0112
