''' Daily Expense Tracker'''

days = int(input(" Enter number of days: "))
total = 0
highest = 0

for day in range(1, days + 1):
    expense = float(input("Expense for day " + str(day) + ": rs "))
    total = total + expense
    if day == 1 or expense > highest:
        highest = expense


if days > 0 :
    average = total / days
else:
    average = 0

print("Total expense : rs", total)
print("Average daily expense: rs ", average)
print("Highest daily expense: rs ", highest)

if total > 5000:
    print("Budget Alert")
else:
    print("Budget is within rs 5000")