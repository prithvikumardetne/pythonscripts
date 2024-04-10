x = {"Honda","Nissan","Toyota"}

y = {"car"}

thisdict = dict.fromkeys(x,y)

print(thisdict)

z = thisdict.get("Honda")

print(z)