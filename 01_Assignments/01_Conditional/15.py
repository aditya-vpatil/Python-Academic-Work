'''Check whether a number is divisible by both 3 and 7 or not'''


num = int(input("Enter an integer: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")
