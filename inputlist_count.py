#input_list = ["hello","HELLO","AM","am","Prithvi","Kumar","Detne"]

input = input("Enter the text:")

input_list = input.split(" ")

input_list_lower = [word.lower() for word in input_list]

input_set = set(input_list_lower)

result_list = []

for word in input_set:
    result_list.append((word,input_list_lower.count(word)))

print(result_list)