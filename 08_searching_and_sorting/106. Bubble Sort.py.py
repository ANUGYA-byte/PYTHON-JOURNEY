# ---------------------------------------
# Program 103: Bubble Sort
# Description: Sorts the elements of a list using bubble sort.
# Author: Anugya Agrawal
# ---------------------------------------

LIST = [50, 20, 40, 10, 30]
print('LIST-',LIST)

for i in range(len(LIST)):
    for j in range(0, len(LIST)-i-1):
        if LIST[j] > LIST[j+1]:
            LIST[j], LIST[j+1] = LIST[j+1], LIST[j]

print('SORTED LIST-',LIST)



# SAMPLE -
# LIST- [50, 20, 40, 10, 30]
# SORTED LIST- [10, 20, 30, 40, 50]
