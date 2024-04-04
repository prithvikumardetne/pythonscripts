n = int(input('Enter any natural Number: '))

print(n)

if (n < 0):
    print('Enter a valid number')
else:
    total_sum = 0
    while n > 0:
        total_sum = total_sum + n
        n = n - 1
        print(f"The sum of natural numbers is: {total_sum}")
    
