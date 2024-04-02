# Define a dictionary
customers = {'05453':'Ram','04457':'Krishna',
'02834':'Vishnu','01655':'Shiva', '07559':'David'}

# Append a new data
customers['06934'] = 'Salomon'

print("The customer names are:")
# Print the values of the dictionary
for customer in customers:
    print(customers[customer])

# Take customer ID as input to search
name = input("Enter customer ID:")

# Search the ID in the dictionary
for customer in customers:
    if customer == name:
        print(customers[customer])
        break