# ---------------------------------------
# Program 38: Calculator Using match-case
# Performs basic arithmetic operations using Python's match-case statement.
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

match CHOICE:

    case 1:
        NUMBER1 = float(input("ENTER NUMBER 1 - "))
        NUMBER2 = float(input("ENTER NUMBER 2 - "))
        RESULT = NUMBER1 + NUMBER2
        print("ANSWER -", RESULT)

    case 2:
        NUMBER1 = float(input("ENTER NUMBER 1 - "))
        NUMBER2 = float(input("ENTER NUMBER 2 - "))
        RESULT = NUMBER1 - NUMBER2
        print("ANSWER -", RESULT)

    case 3:
        NUMBER1 = float(input("ENTER NUMBER 1 - "))
        NUMBER2 = float(input("ENTER NUMBER 2 - "))
        RESULT = NUMBER1 * NUMBER2
        print("ANSWER -", RESULT)

    case 4:
        NUMBER1 = float(input("ENTER NUMBER 1 - "))
        NUMBER2 = float(input("ENTER NUMBER 2 - "))

        if NUMBER2 == 0:
            print("ERROR: CANNOT DIVIDE BY ZERO")
        else:
            RESULT = NUMBER1 / NUMBER2
            print("ANSWER -", RESULT)

    case 5:
        NUMBER1 = float(input("ENTER NUMBER 1 - "))
        NUMBER2 = float(input("ENTER NUMBER 2 - "))

        if NUMBER2 == 0:
            print("ERROR: CANNOT FIND REMAINDER WITH ZERO")
        else:
            RESULT = NUMBER1 % NUMBER2
            print("ANSWER -", RESULT)

    case 6:
        NUMBER1 = float(input("ENTER NUMBER 1 - "))
        NUMBER2 = float(input("ENTER NUMBER 2 - "))
        RESULT = NUMBER1 ** NUMBER2
        print("ANSWER -", RESULT)

    case _:
        print("INVALID CHOICE")

# ---------------------------------------
#SAMPLE -
#---------------------------------------# ---------------------------------------
#                                            MENU                                                 
#---------------------------------------# ---------------------------------------
#1.ADDITION
#2.SUBTRACTION
#3.MULTIPLICATION
#4.DIVISION
#5.REMAINDER
#6.EXPONENT
#ENTER YOUR CHOICE-1
#ENTER NUMBER 1-3
#ENTER NUMBER 2-2
#ANSWER- 5.0

#ENTER YOUR CHOICE-3
#ENTER NUMBER 1-3
#ENTER NUMBER 2-4
#ANSWER- 12.0
