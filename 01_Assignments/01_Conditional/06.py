'''Compare two numbers and print the greater one.'''
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(f"{a} is greater")
elif b > a:
    print(f"{b} is greater")
else:
    print("Both are equal")
