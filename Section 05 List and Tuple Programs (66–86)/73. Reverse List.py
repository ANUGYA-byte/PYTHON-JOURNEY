# ---------------------------------------
# Program 158: .Reverse List  
# Description:Reverse order of elements using list[::-1] or list.reverse()
# Author: Anugya Agrawal
# ---------------------------------------
LIST = []
CHOICE=int(input('ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-'))
for i in range(CHOICE):
    
    ELEMENT=input('ENTER  ELEMENT-')
    LIST.append(ELEMENT)
print("LIST-",LIST)
REVERSELIST=LIST[::-1]
print('REVERSE LIST-',REVERSELIST)

# ---------------------------------------
#SAMPLE -
'''ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-3
ENTER  ELEMENT-5
ENTER  ELEMENT-3
ENTER  ELEMENT-6
LIST- ['5', '3', '6']
REVERSE LIST- ['6', '3', '5']'''
