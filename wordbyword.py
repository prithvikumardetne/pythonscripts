with open('dpk.txt','r') as file:
    for line in file:
        for word in line.split():
            print(word)