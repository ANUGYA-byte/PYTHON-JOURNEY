# ---------------------------------------
# Program 194:Symmetric Difference  
# Description:Elements in either set but not in both. 
# Author: Anugya Agrawal
# ---------------------------------------

A={'python','C','C++'}
B={'CSS','HTML','C++','SQL','C','java'}
print('A-',A)
print('B-',B)
print('SYMMETRIC DIFFERENCE-',A^B)
print('SYMMETRIC DIFFERENCE-',A.symmetric_difference(B))

#A- {'C++', 'python', 'C'}
#B- {'HTML', 'java', 'C', 'C++', 'CSS', 'SQL'}
#SYMMETRIC DIFFERENCE- {'CSS', 'java', 'python', 'HTML', 'SQL'}
#SYMMETRIC DIFFERENCE- {'CSS', 'java', 'python', 'HTML', 'SQL'}'}

