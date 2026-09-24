# ---------------------------------------
# Program 36: Age Category 
# Description:— Determines a person's age category based on their age.
# Author: Anugya Agrawal
# ---------------------------------------# ---------------------------------------

AGE=int(input('Enter your age-'))

if AGE<=10:
    print ("AGE-",AGE, 'Category- A')
    
elif 10<AGE<=20:
    print ("AGE-",AGE, 'Category- B')

elif 20<AGE<=30:
    print ("AGE-",AGE, 'Category- C')

elif 30<AGE<=40:
    print ("AGE-",AGE, 'Category- D')

elif 40<AGE<=50:
    print ("AGE-",AGE, 'Category- E')
    
elif AGE>50:
    print ("AGE-",AGE, 'Category- F')


# ---------------------------------------
#SAMPLE -
#ENTER YOUR AGE-22
#AGE- 22 Category- C

# ---------------------------------------
#SAMPLE -
#ENTER YOUR AGE-44
#AGE- 44 Category- E


