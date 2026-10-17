# ---------------------------------------
# Program 45:Sum of N Odd Numbers
# Description:Calculates the sum of odd numbers up to N.
# Author: Anugya Agrawal
# ---------------------------------------
SUM1=0
SUM2=0
NUMBER=int(input('ENTER NUMBER -'))
for i in range(1,NUMBER+1):
    if i%2==0:
      SUM1=SUM1+0
    else:
        SUM1=SUM1+i
print("SUM-",SUM1)

C=0
while C<(NUMBER):
    C=C+1
    if C%2==0:
        SUM2=SUM2+0 
    else:
        SUM2=SUM2+C
    
print("SUM-",SUM2)

# ---------------------------------------
#SAMPLE INPUT -
#ENTER NUMBER -5
#SAMPLE OUTPUT -
#SUM- 9
#SUM- 9
