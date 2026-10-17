# ---------------------------------------
# Program 186:Count Elements
# Description:  Use tuple.count(value) to count occurrences of an item
# Author: Anugya Agrawal
# ---------------------------------------
COUNT=0
TUPLE=('python', 'C', 'C++', 'java',('C', 'C++'),'python', 'C','C', 'C++', )
print('TUPLE-',TUPLE)
ELEMENT=input("ENTER ELEMENT WHICH IS TO BE SEARCHED-")
for i in TUPLE:
       if i==ELEMENT:
        COUNT=COUNT+1
       else:
         COUNT=COUNT+0
print('COUNT OF ELEMENT-',COUNT)

# ---------------------------------------
#SAMPLE -
#TUPLE- ('python', 'C', 'C++', 'java', ('C', 'C++'))
#ENTER ELEMENT WHICH IS TO BE SEARCHED-C
#COUNT OF ELEMENT- 3
