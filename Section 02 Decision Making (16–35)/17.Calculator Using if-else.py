# ---------------------------------------
# Program 37: Calculator Using if-else
# Performs basic arithmetic operations using if-else statements.
# Author: Anugya Agrawal
# ---------------------------------------

print("---------------------------------------")
print("                 MENU")
print("---------------------------------------")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. REMAINDER")
print("6. EXPONENT")
print("---------------------------------------")

CHOICE = int(input("ENTER YOUR CHOICE - "))

if CHOICE == 1:
    NUMBER1 = float(input("ENTER NUMBER 1 - "))
    NUMBER2 = float(input("ENTER NUMBER 2 - "))
    RESULT = NUMBER1 + NUMBER2
    print("ANSWER -", RESULT)

elif CHOICE == 2:
    NUMBER1 = float(input("ENTER NUMBER 1 - "))
    NUMBER2 = float(input("ENTER NUMBER 2 - "))
    RESULT = NUMBER1 - NUMBER2
    print("ANSWER -", RESULT)

elif CHOICE == 3:
    NUMBER1 = float(input("ENTER NUMBER 1 - "))
    NUMBER2 = float(input("ENTER NUMBER 2 - "))
    RESULT = NUMBER1 * NUMBER2
    print("ANSWER -", RESULT)

elif CHOICE == 4:
    NUMBER1 = float(input("ENTER NUMBER 1 - "))
    NUMBER2 = float(input("ENTER NUMBER 2 - "))

    if NUMBER2 == 0:
        print("ERROR: CANNOT DIVIDE BY ZERO")
    else:
        RESULT = NUMBER1 / NUMBER2
        print("ANSWER -", RESULT)

elif CHOICE == 5:
    NUMBER1 = float(input("ENTER NUMBER 1 - "))
    NUMBER2 = float(input("ENTER NUMBER 2 - "))

    if NUMBER2 == 0:
        print("ERROR: CANNOT FIND REMAINDER WITH ZERO")
    else:
        RESULT = NUMBER1 % NUMBER2
        print("ANSWER -", RESULT)

elif CHOICE == 6:
    NUMBER1 = float(input("ENTER NUMBER 1 - "))
    NUMBER2 = float(input("ENTER NUMBER 2 - "))
    RESULT = NUMBER1 ** NUMBER2
    print("ANSWER -", RESULT)

else:
    print("INVALID CHOICE")
