'''Employee Payroll Summary'''

employees = int(input("Enter number of employees: "))
total_net_payroll = 0
for i in range(1, employees + 1):
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: Rs "))
    overtime_hours = float(input("Enter overtime hours: "))
    overtime_pay = overtime_hours * 200
    gross_salary = basic_salary + overtime_pay
    if gross_salary >= 50000:
        deduction = gross_salary * 0.10
    else:
        deduction = gross_salary * 0.05
    net_salary = gross_salary - deduction
    total_net_payroll = total_net_payroll + net_salary
    print("Employee:", name)
    print("Gross salary: Rs", gross_salary)
    print("Deduction: Rs", deduction)
    print("Net salary: Rs", net_salary)
print("Employee count:", employees)
print("Total net payroll: Rs", total_net_payroll)