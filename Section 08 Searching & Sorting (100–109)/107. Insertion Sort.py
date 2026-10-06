# ---------------------------------------
# Program 105: Insertion Sort
# Description: Sorts the elements of a list using insertion sort.
# Author: Anugya Agrawal
# ---------------------------------------

LIST = [50, 20, 40, 10, 30]
print('LIST-',LIST)

for i in range(1, len(LIST)):
    KEY = LIST[i]
    j = i - 1

    while j >= 0 and LIST[j] > KEY:
        LIST[j+1] = LIST[j]
        j = j - 1

    LIST[j+1] = KEY

print('SORTED LIST-',LIST)



# SAMPLE -
# LIST- [50, 20, 40, 10, 30]
# SORTED LIST- [10, 20, 30, 40, 50]
