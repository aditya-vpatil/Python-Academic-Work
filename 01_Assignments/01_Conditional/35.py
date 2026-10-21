'''Check whether a number is divisible by 3 and 5'''


num = int(input("Enter an integer: "))
if num % 3 == 0:
    if num % 5 == 0:
        print("Divisible by both 3 and 5")
    else:
        print("Divisible by 3 only")
else:
    print("Not divisible by 3")
