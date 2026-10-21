'''Check whether a number is positive and even using nested if'''


num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but not even")
else:
    print("Not a positive number")  