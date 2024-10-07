name = "Prithvi Kumar Detne"

name_list = list(name.split(" "))

print(name_list)

name_list.reverse()

print(name_list)

reverse_name = ''

for element in name_list:
    reverse_name += element + "."

print(reverse_name)

reverse_new = reverse_name.rstrip(".")

print(reverse_new)


