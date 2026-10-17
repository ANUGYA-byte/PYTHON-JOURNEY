# ---------------------------------------
# Program 51: Prime Numbers in a Range 
# Description: Print all prime numbers between a given start and end value by checking each number in the range. A prime number is a number greater than 1 that has exactly two factors: 1 and itself.
# Author: Anugya Agrawal
# ---------------------------------------
# Program 51: 

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")

# ---------------------------------------
#SAMPLE INPUT -
'''
Enter the starting number: 10
Enter the ending number: 50
'''
# ---------------------------------------
#SAMPLE OUTPUT-
'''
Prime numbers between 10 and 50 are:
11 13 17 19 23 29 31 37 41 43 47
'''
