raw_data = """E00163 Bella Powell Director Finance Research Female
E00884 Camila Silva Sr. Manger Marketing Speciality Female"""

data = raw_data.split("\n")

print(data)

data_dict = {}

for i in data:
    data_dict[i.split(" ")[0]] = tuple(i.split(" ")[1:])

print(data_dict)

nested_dict = {}

for key,value in data_dict.items():
    nested_dict[key] = {
     "customer_first_name" : value[0],
     "customer_last_name" : value[1]
    }

print(nested_dict.get("E00884").get("customer_first_name"))