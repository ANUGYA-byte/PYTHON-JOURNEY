# ---------------------------------------
# Program 43:Sum of N Numbers
# Description:Finds the sum of the first N natural numbers.
# Author: Anugya Agrawal
# ---------------------------------------
SUM1=0
SUM2=0
NUMBER=int(input('ENTER NUMBER -'))
for i in range(1,NUMBER+1):
    SUM1=SUM1+i
print("SUM-",SUM1)

C=0
while C<(NUMBER):
    C=C+1
    SUM2=SUM2+C
print("SUM-",SUM2)

# ---------------------------------------
#SAMPLE INPUT -
#ENTER NUMBER -3
# ---------------------------------------
#SAMPLE OUTPUT -
#SUM- 6
#SUM- 6

