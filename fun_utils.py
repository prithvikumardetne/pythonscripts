import os
import datetime

command="uptime"

def check_uptime(command):
    print(os.system(command))

check_uptime(command)


def show_date():
    return datetime.datetime.today()

today = show_date()

print(today)