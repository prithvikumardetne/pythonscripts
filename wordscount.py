list1 = ["Semicolons", "are", "one", "of", "the", "most", "misunderstood", "and", "underused", "punctuation", "marks"]

list2 = set(list1)

print(list2)

list3 = []

for word in list2:
    list3.append((word,list1.count(word)))

print(list3)