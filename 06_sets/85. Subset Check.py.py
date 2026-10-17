
# ---------------------------------------
# Program 195:Subset Check
# Description: Use set1.issubset(set2) to verify if all elements of set1 exist in set2.
# Author: Anugya Agrawal
# ---------------------------------------
A={'Java','python', 'C', 'CSS', 'java', 'sql', 'C++','Html'}
B={'Java','python', 'C', 'CSS'}
print('A-',A)
print('B-',B)
if B.issubset(A):
   print('YES')
else:
    print('NO')

# ---------------------------------------
#SAMPLE -
'''A- {'Java', 'java', 'C', 'C++', 'sql', 'CSS', 'python', 'Html'}
B- {'CSS', 'python', 'C', 'Java'}
YES'''
