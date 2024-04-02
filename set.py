numbers = {10,12,15,17,85,96}

numbers.add(63)

numbers.remove(17)

print(numbers)

message = "Number is not found"

search_number = int(input("Enter a number:"))

for val in numbers:
    if val == search_number:
        message = " Number is found"
        break

print(message)