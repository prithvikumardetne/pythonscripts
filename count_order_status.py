data = """EEID	Full Name	Department	Gender	Ethnicity	Age
E02387 Emily IT Female Black 55
E04105 Theodore IT Male Asian 59
E02572 Luna Finance Female Caucasian 50
E02832 Penelope IT Female Caucasian 26
E01639 Austin Finance Male Asian 55"""

lines = data.split("\n")[1:]

#print(lines)

lines_tuple = [tuple(line.split(" ")) for line in lines]

#print(lines_tuple)

age = [age[4] for age in lines_tuple]

print(age)

age_set = set(age)

print(age_set)

#order_status_count = [(status,status_list.count(status)) for status in status_list_set]
#print(order_status_count)


for age_count in age:
    age_set_count = [(age,age.count(age))]
print(age_set_count)