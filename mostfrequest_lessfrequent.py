data = [3,3,4,4,4,5,5,2]

#data_set = set(data)

#print(data_set)

most_frequent = max(set(data), key=data.count)

print(most_frequent)

less_frequent = min(set(data),key=data.count)

print(less_frequent)