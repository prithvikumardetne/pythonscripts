def employee_details(ID):
    switcher = {
        "1004": "Employee Name: Prithvi",
        "1005": "Employee Name: Kumar",
        "1006": "Exployee name: Detne",
    }
    return switcher.get(ID, "nothing")
ID = input("Enter the employee id: ")
print(employee_details(ID))