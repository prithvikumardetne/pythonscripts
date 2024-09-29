bill_amount = [100,200,300,400,500,600]

'''bill_after_gst = []

for x in bill_amount:
    bill_after_gst.append(x+x*.18)


print(bill_after_gst)'''

'''bill_after_gst = [x+x*.18 for x in bill_amount]

print(bill_after_gst)'''

bill_amount = [(100,5),(200,8),(300,6),(400,5),(500,5),(600,8)]

bill_amount_with_gst = [(x[0],x[1],x[0] + x[0] * x[1]/100)  for x in bill_amount]

"""bill_amount_with_gst = []
for x in bill_amount:
    bill_amount_with_gst.append(x[0] + x[0] * x[1]/100)"""

print(bill_amount_with_gst)
