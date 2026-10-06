# ---------------------------------------
# Description: Checks whether a number is a palindrome using a function.
# Author: Anugya Agrawal
# Program 100: Linear Search

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the element to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
