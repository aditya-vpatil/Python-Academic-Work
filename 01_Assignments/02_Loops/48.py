''' Check whether a number is a strong number'''

num = int(input("Enter a number: "))
temp = num
total = 0

if temp == 0:
    total = 1
else:
    while temp > 0:
        digit = temp % 10
        factorial = 1

        for i in range(1, digit + 1):
            factorial = factorial * i

        total = total + factorial
        temp = temp // 10

if num >= 0 and total == num:
    print("Strong number")
else:
    print("Not a strong number")
