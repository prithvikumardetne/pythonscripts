name = "Prithvi Kumar Detne"

index = name.find(" ")

print (name[:index])#printing string until first place 

print(name[0:9:2]) # printing string alternatively

print(name[::-1]) # reversing a string

print(name.find("K")) # will print the indexing of first occurrence of K

print( name.find("S")) # Printing -1 since it didnt find indexing of the string

print(name.endswith("r")) #endswith is a method which will help in finding last word or last index

print(name.replace("Prithvi","DPK")) # replace method