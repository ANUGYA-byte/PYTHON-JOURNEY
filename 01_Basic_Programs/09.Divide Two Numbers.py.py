# ---------------------------------------
# Program 9: Divide Two Numbers
# Description: Divides one number by another.
# Author: Anugya Agrawal
# ---------------------------------------


number1 = float(input("Enter Number 1: "))
number2 = float(input("Enter Number 2: "))

if number2 == 0:
    print("Division by zero is not possible.")
else:
    division = number1 / number2
    print(f"Division of 2 Numbers: {division}")
    
# ---------------------------------------
#SAMPLE -
'''
Enter Number 1: 3
Enter Number 2: 4
Division of 2 Numbers: 0.75
'''
# ---------------------------------------
#SAMPLE -
'''
Enter Number 1: 4
Enter Number 2: 0
Division by zero is not possible.
'''
