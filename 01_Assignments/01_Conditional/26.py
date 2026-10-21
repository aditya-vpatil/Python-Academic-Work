'''Check month names based on month number'''


month = int(input("Enter month number (1-12): "))
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
if 1 <= month <= 12:
    print(months[month - 1])
else:
    print("Invalid month number")
