from datetime import date

current_date = date.today()

print( "Today is :%d-%d-%d" % (current_date.day,current_date.month,current_date.year))

custom_date = date(2026, 12, 26)

print( "The date is:", custom_date)