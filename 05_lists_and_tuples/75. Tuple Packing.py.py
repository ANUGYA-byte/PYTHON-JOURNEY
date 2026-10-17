# ---------------------------------------
# Program 183: Tuple Packing  
# Description:Assign multiple values into a single tuple without explicit parentheses.
# Author: Anugya Agrawal
# ---------------------------------------
TUPLE = ()
CHOICE=int(input('ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-'))
for i in range(CHOICE):
    
    ELEMENT=input('ENTER  ELEMENT-')
    TUPLE=TUPLE+(ELEMENT,)
print("TUPLE-",TUPLE) 

# ---------------------------------------
#SAMPLE INPUT-
'''ENTER NUMBER OF ELEMENTS YOU WANT TO ENTER-2
ENTER  ELEMENT-C
ENTER  ELEMENT-C++'''

# ---------------------------------------
#SAMPLE  OUTPUT-
#TUPLE- ('C', 'C++')



