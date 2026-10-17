# Program 93: Check whether a number is an Armstrong number using a function

def is_armstrong(number):
    original = number
    digits = len(str(number))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    return total == original


num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
```
