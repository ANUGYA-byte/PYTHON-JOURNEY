# ---------------------------------------
# Description: Finds the GCD of two numbers using a function.
# Author: Anugya Agrawal
# Program 101: Binary Search

numbers = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter the element to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Element found at index:", mid)
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
