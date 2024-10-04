data = """E04332 Luke Martin Finance Male Black 25
E04533 Easton Bailey Accounting Male Caucasian 29"""

data_list = data.split("\n")

print(data_list[0])

last_name = [i.split()[2] for i in data_list]
    
print(last_name)



