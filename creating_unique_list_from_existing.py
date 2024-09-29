order = [50,40,60,20,50,80,50]

order_unique = []

for x in order:
    if x in order_unique:
        continue
    else:
        order_unique.append(x)
print(order_unique)