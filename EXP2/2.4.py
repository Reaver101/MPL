emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

da = 0.80 * basic_salary
hra = 0.40 * basic_salary

gross_salary = basic_salary + da + hra

pf = 0.12 * basic_salary

if gross_salary > 50000:
    tax = 0.05 * gross_salary
else:
    tax = 0

net_salary = gross_salary - (pf + tax)

print("\n------ Employee Payroll ------")
print("Employee ID :", emp_id)
print("Employee Name :", name)
print("Basic Salary :", basic_salary)
print("DA :", da)
print("HRA :", hra)
print("Gross Salary :", gross_salary)
print("PF :", pf)
print("Tax :", tax)
print("Net Salary :", net_salary)