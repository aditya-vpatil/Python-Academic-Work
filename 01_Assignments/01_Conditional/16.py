'''Find the greatest of three numbers'''

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print(f"{a} is greatest")
elif b >= a and b >= c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
