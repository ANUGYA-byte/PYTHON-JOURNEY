# ---------------------------------------
# Program 35: Voting Eligibility 
# Description:— Checks whether a person is eligible to vote based on their age.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------

age = int(input("ENTER YOUR AGE: "))

if age < 0:
    print("INVALID AGE")
elif age >= 18:
    print("AGE -", age)
    print("STATUS - VOTING ELIGIBLE")
else:
    print("AGE -", age)
    print("STATUS - NOT VOTING ELIGIBLE")
    
# ---------------------------------------
#SAMPLE -
#ENTER YOUR AGE-33
#AGE- 33.0 STATUS- VOTING ELIGIBLE

# ---------------------------------------
#SAMPLE -
#ENTER YOUR AGE-17
#AGE- 17.0 STATUS- SORRY , YOU ARE NOT VOTING ELIGIBLE

