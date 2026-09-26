# ---------------------------------------
# Program 189:Tuple Slicing
# Description:Use [start:end:step] to access a range of elements.
# Author: Anugya Agrawal
# ---------------------------------------

TUPLE=(2,4,5,77,88,55,33,2,5,7,8,9,3,-2 )
START=int(input("ENTER STARTING INDEX-"))
END=int(input("ENTER ENDING INDEX-"))
STEP=int(input("ENTER STEP-"))
RANGE=TUPLE[START:END:STEP]
print('TUPLE-',TUPLE)
print('RANGE-',RANGE)

# ---------------------------------------
#SAMPLE -
'''ENTER STARTING INDEX-1
ENTER ENDING INDEX-7
ENTER STEP-2
TUPLE- (2, 4, 5, 77, 88, 55, 33, 2, 5, 7, 8, 9, 3, -2)
RANGE- (4, 77, 55)'''
