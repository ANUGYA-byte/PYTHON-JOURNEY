# ---------------------------------------
# Program 157:Second Smallest  
# Description:Find the element that is just larger than the minimum in a list.   
# Author: Anugya Agrawal
# ---------------------------------------
LIST = []
CHOICE=int(input('ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-'))
for i in range(CHOICE):
    
    ELEMENT=input('ENTER  ELEMENT-')
    LIST.append(ELEMENT)
print("LIST-",LIST)
LIST.sort()
MIN2=LIST[1]
print('Second Smaller - ',MIN2)

# ---------------------------------------
#SAMPLE -
'''ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-5
ENTER  ELEMENT-16
ENTER  ELEMENT-17
ENTER  ELEMENT-44
ENTER  ELEMENT-77
ENTER  ELEMENT-45
LIST- ['16', '17', '44', '77', '45']
Second Smaller -  17'''
