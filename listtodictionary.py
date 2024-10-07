raw_data  = """E02387 Emily Davis Sr.Manger IT
E04105 Theodore Dinh Technical Architect IT"""


data = raw_data.split("\n")

print(data)

#data_dict = {}

#for x in data:
#    data_dict[x.split(" ")[0]] = tuple(x.split(" ")[1:])
#print(data_dict['E02387'])

data_dict = { x.split(" ")[0] : tuple(x.split(" ")[1:]) for x in data }

print(data_dict)

nested_dict = {}

for key,value in data_dict.items():
    nested_dict[key] = {
        "customer_first_name": value[0],
        "customer_last_name": value[1]
    }
print(nested_dict.get("E04105").get("customer_first_name"))