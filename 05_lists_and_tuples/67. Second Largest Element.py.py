# ---------------------------------------
# Program 156:Second Largest  
# Description:  Find the element that is just smaller than the maximum in a list.
# Author: Anugya Agrawal
# ---------------------------------------
LIST = []
CHOICE=int(input('ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-'))
for i in range(CHOICE):
    
    ELEMENT=input('ENTER  ELEMENT-')
    LIST.append(ELEMENT)
print("LIST-",LIST)
LIST.sort()
MAX2=LIST[-2]
print('Second Largest - ',MAX2)

# ---------------------------------------
#SAMPLE -
'''ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-5
ENTER  ELEMENT-2
ENTER  ELEMENT-44
ENTER  ELEMENT-5
ENTER  ELEMENT-66
ENTER  ELEMENT-777
LIST- ['2', '44', '5', '66', '777']
['2', '44', '5', '66', '777']
Second Largest -  ['66']'''
