''' Find smallest digit in a number'''

num = (int(input("Enter a number: ")))
smallest = 9

if num == 0:
    smallest = 0
else:
    while num > 0:
        digit = num % 10

        if digit < smallest:
            smallest = digit

        num = num // 10

print("Smallest digit =", smallest)
