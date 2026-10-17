# ---------------------------------------
# Description: Finds the factorial of a number using recursion.
# Author: Anugya Agrawal
# Program 103: Selection Sort

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

for i in range(len(numbers)):
    min_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted list:", numbers)
