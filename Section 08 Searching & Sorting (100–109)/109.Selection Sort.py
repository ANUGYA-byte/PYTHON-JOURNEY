# ---------------------------------------
# Program 104: Selection Sort
# Description: Sorts the elements of a list using selection sort.
# Author: Anugya Agrawal
# ---------------------------------------

LIST = [50, 20, 40, 10, 30]
print('LIST-',LIST)

for i in range(len(LIST)):
    MIN_INDEX = i

    for j in range(i+1, len(LIST)):
        if LIST[j] < LIST[MIN_INDEX]:
            MIN_INDEX = j

    LIST[i], LIST[MIN_INDEX] = LIST[MIN_INDEX], LIST[i]

print('SORTED LIST-',LIST)



# SAMPLE -
# LIST- [50, 20, 40, 10, 30]
# SORTED LIST- [10, 20, 30, 40, 50]
