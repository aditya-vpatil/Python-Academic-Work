''' Check whether a number is Armstrong'''

num = int(input("Enter a number: "))
temp = num
digits = 0
total = 0

if temp == 0:
    digits = 1
else:
    while temp > 0:
        digits = digits + 1
        temp = temp // 10

temp = num

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if num >= 0 and total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
