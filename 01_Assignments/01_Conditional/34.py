'''Check whether a year is a leap year and century year'''


year = int(input("Enter year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("Century year and a leap year")
    else:
        print("Century year but not a leap year")
else:
    print("Not a century year")
