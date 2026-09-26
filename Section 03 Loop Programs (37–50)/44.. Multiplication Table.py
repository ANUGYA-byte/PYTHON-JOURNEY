# ---------------------------------------
# Program 46:  Multiplication Table 
# Description: Display products of a number with integers in sequence.
# Author: Anugya Agrawal
# ---------------------------------------
NUMBER=int(input('ENTER NUMBER -'))
for i in range (1,11):
    print(NUMBER,'X',i,'=',NUMBER*i)

C=1
while C<11:
    print(NUMBER,'X',C,'=',NUMBER*C)
    C=C+1

# ---------------------------------------
#SAMPLE
"""ENTER NUMBER -3
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30

3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
3 X 10 = 30"""
