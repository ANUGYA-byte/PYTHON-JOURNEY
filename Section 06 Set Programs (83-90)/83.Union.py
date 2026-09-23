# ---------------------------------------
# Program 191: Union
# Description:Combines all elements from both sets.
# Author: Anugya Agrawal
# ---------------------------------------

A={'python','C','C++'}
B={'CSS','HTML','C++','SQL','C','java'}
print('A-',A)
print('B-',B)
print('UNION-',A|B)
print('UNION-',A.union(B))

#A- {'python', 'C++', 'C'}
#B- {'java', 'SQL', 'C++', 'CSS', 'HTML', 'C'}
#UNION- {'C++', 'SQL', 'python', 'java', 'CSS', 'HTML', 'C'}
#UNION- {'C++', 'SQL', 'python', 'java', 'CSS', 'HTML', 'C'}


