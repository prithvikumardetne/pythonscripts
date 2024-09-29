#names_list = ["Prithvi","Kumar","Detne"] - It is mutable
#names_tuple = ("Prithvi","Kumar","Detne") - It is immutable
#range =(0-9)

name = "Prithvi Kumar Detne "

ordered_name = name.split(" ")

print(ordered_name)
new_ordered_name = ordered_name[1]="DPK"

print(new_ordered_name)


names = ["A","B","C","D"]

names[2]="E"

print(names)

names_tuple = ("A","B","C","D")

names_list = list(names_tuple)

print(names_list)

names_list.insert(1,'E')

print(names_list)

names_tuple = tuple(names_list)

print(names_tuple)