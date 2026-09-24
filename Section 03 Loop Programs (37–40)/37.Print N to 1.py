# ---------------------------------------
# Program 42:Print N to 1
# Description:Prints numbers from N down to 1 using a loop.
# Author: Anugya Agrawal
# ---------------------------------------

NUMBER=int(input('ENTER NUMBER -'))
for i in range(NUMBER,0,-1):
    print(i)
    
while 0<NUMBER:
     print(NUMBER)
     NUMBER=NUMBER-1
   

# ---------------------------------------
#SAMPLE -
#ENTER NUMBER -3
#3
#2
#1
#3
#2
#1
