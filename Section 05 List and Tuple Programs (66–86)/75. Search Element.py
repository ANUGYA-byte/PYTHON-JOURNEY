# ---------------------------------------
# Program 160:Search Element  
# Description: Find presence with in or locate position
# Author: Anugya Agrawal
# ---------------------------------------
LIST = []
CHOICE=int(input('ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-'))
SEARCH=input('ENTER ELEMENT TO BE SEARCHED-')
for i in range(CHOICE):
    
    ELEMENT=input('ENTER  ELEMENT-')
    LIST.append(ELEMENT)
print("LIST-",LIST)
LOCATION=list.index(SEARCH)
print('LOCAION- ',LOCAION)

# ---------------------------------------
#SAMPLE -
'''ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-3
ENTER  ELEMENT-5
ENTER  ELEMENT-3
ENTER  ELEMENT-6
LIST- ['5', '3', '6']
SORTED LIST- ['3', '5', '6']'''
