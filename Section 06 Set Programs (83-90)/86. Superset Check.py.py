
# ---------------------------------------
# Program 196:Superset Check
# Description: Use set1.issuperset(set2) to verify if all elements of set1 exist in set2.
# Author: Anugya Agrawal
# ---------------------------------------
A={'Java','python', 'C', 'CSS', 'java', 'sql', 'C++','Html'}
B={'Java','python', 'C', 'CSS'}
print('A-',A)
print('B-',B)
if A.issuperset(B):
   print('YES SUPERSET')
else:
    print('NO')

# ---------------------------------------
#SAMPLE -
'''A- {'Java', 'java', 'C', 'C++', 'sql', 'CSS', 'python', 'Html'}
B- {'CSS', 'python', 'C', 'Java'}
YES SUPERSET'''
