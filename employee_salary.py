employees = [
    ["Anu", 25000],
    ["Ravi", 40000],
    ["Meena", 55000],
    ["John", 28000],
    ["Sara", 60000]
]
total_expense = 0
highest_salary = 0
highest_employee = ""
low_salary_employees = []
print("\nEmployee Salary Details:\n")
for emp in employees:
    name = emp[0]
    basic = emp[1]
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    total_expense += gross
    print("Name:", name)
    print("Basic:", basic)
    print("HRA:", hra)
    print("DA:", da)
    print("Gross Salary:", gross)
    if gross > highest_salary:
        highest_salary = gross
        highest_employee = name
    if gross < 30000:
        low_salary_employees.append(name)
print("\nTotal Company Expense:", total_expense)
print("Highest Paid Employee:", highest_employee)
print("Employees earning less than 30000:", low_salary_employees)
