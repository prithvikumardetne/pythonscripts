order_amounts =[100,200,300,400,"INVALID",True,900]

i = 0
sum = 0

while type(order_amounts[i]) < len(order_amounts):
    if type(order_amounts[i]) == int:
        sum = sum + order_amounts[i]
        continue
    i = i + 1
    print(sum)
