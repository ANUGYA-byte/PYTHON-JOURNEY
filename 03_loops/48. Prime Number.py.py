# ---------------------------------------
# Program 50: Prime Number
# Checks whether a number is prime.
# Author: Anugya Agrawal
# ---------------------------------------

NUMBER = int(input("ENTER NUMBER-"))

if NUMBER > 1:
    for i in range(2, NUMBER):
        if NUMBER % i == 0:
            print("NOT A PRIME NUMBER")
            break
    else:
        print("PRIME NUMBER")
else:
    print("NOT A PRIME NUMBER")
