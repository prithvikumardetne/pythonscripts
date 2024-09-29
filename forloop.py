range_start = int(input("Enter Starting Range: "))
range_ending = int(input("Enter Ending Range: "))
numbers = range(range_start,range_ending)
sum = 0
for i in numbers:
    sum = sum + i
print(sum)