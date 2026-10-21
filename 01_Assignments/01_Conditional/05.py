'''Check whether a given year is a leap year or not.'''
year = int(input("Enter year: "))
if (year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")
