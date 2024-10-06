data = [3,3,4,4,4,5,5,2]

data_extend = [8,9,7,6]

#data_set = set(data)

#print(data_set)

most_frequent = max(set(data), key=data.count)

print(most_frequent)

less_frequent = min(set(data),key=data.count)

print(less_frequent)

data.sort(reverse=True)

print(data)

data.sort(reverse=False)

print(data)

data.append(6)

print(data)

print(data.count(4))

data.extend(data_extend)

print(data)

data_index = data.index(9)

print(data_index)

data_pop = data.pop()

print(data)

data.remove(9)

print(data)

del data[2:4]

print(data)

data.insert(5,7)

print(data)