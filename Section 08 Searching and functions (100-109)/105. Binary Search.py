# ---------------------------------------
# Program 102: Binary Search
# Description: Searches for an element in a sorted list using binary search.
# Author: Anugya Agrawal
# ---------------------------------------

LIST = [10, 20, 30, 40, 50, 60, 70]
print('LIST-',LIST)

SEARCH = 50
LOW = 0
HIGH = len(LIST) - 1
FOUND = False

while LOW <= HIGH:
    MID = (LOW + HIGH) // 2

    if LIST[MID] == SEARCH:
        FOUND = True
        break
    elif LIST[MID] < SEARCH:
        LOW = MID + 1
    else:
        HIGH = MID - 1

if FOUND:
    print('ELEMENT FOUND-',SEARCH)
else:
    print('ELEMENT NOT FOUND-',SEARCH)



# SAMPLE -
# LIST- [10, 20, 30, 40, 50, 60, 70]
# ELEMENT FOUND- 50
