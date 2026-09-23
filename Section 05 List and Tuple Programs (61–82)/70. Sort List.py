# ---------------------------------------
# Program 159:Sort List   
# Description: Arrange elements in ascending/descending order
# Author: Anugya Agrawal
# ---------------------------------------
LIST = []
CHOICE=int(input('ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-'))
for i in range(CHOICE):
    
    ELEMENT=input('ENTER  ELEMENT-')
    LIST.append(ELEMENT)
print("LIST-",LIST)
SORTEDLIST=sorted(LIST)
print('SORTED LIST- ',SORTEDLIST)

# ---------------------------------------
#SAMPLE -
'''ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-3
ENTER  ELEMENT-5
ENTER  ELEMENT-3
ENTER  ELEMENT-6
LIST- ['5', '3', '6']
SORTED LIST- ['3', '5', '6']'''
