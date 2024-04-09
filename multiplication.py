def print_multiplication_table(number):
    print("Multiplication table of {number}:")
    for i in range(1,11):
        result = number*i
        print(f"{number}x{i}={result}")

num = int(input("Enter a number:"))
print_multiplication_table(num)