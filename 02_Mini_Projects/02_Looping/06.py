'''Electricity Usage Analyzer '''

days = int(input("Enter number of days: "))
total_units = 0
high_usage_days = 0
maximum = 0
for day in range(1, days + 1):
    units = float(input("Units used on day " + str(day) + ": "))
    total_units = total_units + units
    if units > 10:
        high_usage_days = high_usage_days + 1
    if day == 1 or units > maximum:
        maximum = units
if days > 0:
    average = total_units / days
else:
    average = 0
print("Total units:", total_units)
print("Average units per day:", average)
2
print("Days above 10 units:", high_usage_days)
print("Maximum daily usage:", maximum)
if total_units > 300:
    print("High Usage")
else:
    print("Usage is within 300 units")