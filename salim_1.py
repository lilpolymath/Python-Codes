rate = float(input("Enter the hourly pay rate: "))
hours_worked = float(input("Enter the number of hours you worked: "))

if hours_worked > 0 and hours_worked < 41:
    pay = rate*hours_worked
elif hours_worked > 40.0 and hours_worked < 51.0:
    overtime = hours_worked - 40
    pay = rate*40 + overtime*rate*1.5
else:#elif hours_worked not in range(0,51):
    pay = rate*40 + 10*rate*1.5

pay = format(pay,'.2f')
print("Your Weekly Pay is: {}".format(pay))
