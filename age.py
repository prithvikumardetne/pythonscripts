age = int(input("Enter the age: "))
crime_record = str(input("Are there any criminal records: "))

if age > 18 and crime_record == "No":
    print ("Person is eligible")
else: 
    print("Person is not eligible")