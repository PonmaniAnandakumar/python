hours = float(input("Enter total hours worked: "))
rate = float(input("Enter rate per hour: "))

if hours <= 40:
    pay = hours * rate
    print("Regular Pay:", pay)
else:
    overtime_hours = hours - 40
    regular_pay = 40 * rate
    overtime_pay = overtime_hours * rate * 1.5
    total_pay = regular_pay + overtime_pay

    print("Regular Pay:", regular_pay)
    print("Overtime Hours:", overtime_hours)
    print("Overtime Pay:", overtime_pay)
    print("Total Pay:", total_pay)
