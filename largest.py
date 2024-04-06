a = int(input("Enter number a:"))
b = int(input("Enter number b:"))
c = int(input("Enter number c:"))

if (a>b ) and ( b>c ):
    print(a)
elif (b>c) and (b>a):
    print(b)
else:
    print(c)
    