# ---------------------------------------
# Program 89: Set Difference Update
# Description: Demonstrates set difference and difference_update operations.
# Author: Anugya Agrawal
# ---------------------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Set 1:", set1)
print("Set 2:", set2)

difference = set1 - set2
print("Difference:", difference)

set1.difference_update(set2)
print("Set 1 after difference_update:", set1)
