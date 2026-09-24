# ---------------------------------------
# Program 30: Grade Calculator
# Description:Calculates a student's grade based on their marks or percentage
# Author: Anugya Agrawal
# ---------------------------------------

percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("INVALID PERCENTAGE")
elif percentage >= 90:
    print("GRADE - A")
elif percentage >= 80:
    print("GRADE - B")
elif percentage >= 70:
    print("GRADE - C")
elif percentage >= 60:
    print("GRADE - D")
elif percentage >= 50:
    print("GRADE - E")
else:
    print("GRADE - F")

# ---------------------------------------
#SAMPLE -
#Enter your  percentage-  72
#GRADE - C
# ---------------------------------------
#SAMPLE -
#Enter your  percentage-  33
#GRADE - E
