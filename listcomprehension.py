#list = [1,2,3]

list1 = []

list1 = [[x,x ** 2,x ** 3] for x in range(1,4)] 

'''for x in range(1,4):
    list1.append([x,x ** 2,x ** 3])'''

print(list1)

flattened_lists = []

'''for sublists in list1:
    for item in sublists:
        flattened_lists.append(item)
print(flattened_lists)'''

flattened_lists = [item for sublists in list1 for item in sublists]

print(flattened_lists)