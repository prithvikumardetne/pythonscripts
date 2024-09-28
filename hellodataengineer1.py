import math

name="prithvi"

print(type(name))

age="37"

print(type(age))

amount=100.52


print(type(amount))

is_male=True
print(type(is_male))

print(amount + 50)

print (int(age) + (int(age) * .1))

d = 115.46

print(math.ceil(d))

marks = int(input("Enter the Marks: "))

if marks > 35:
    print("Pass")
elif marks > 35 & marks < 70:
    print ("First Grade")
else:
    print("failed")