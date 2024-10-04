names = ["A","B","C","A","B","C"]

names_unique = []

for i in names:
    if i in names_unique:
        continue
    else:
        names_unique.append(i)
    
print(names_unique)