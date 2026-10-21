'''Perform calculator operations using match case'''


a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
match op:
    case '+': print(f"Result: {a + b}")
    case '-': print(f"Result: {a - b}")
    case '*': print(f"Result: {a * b}")
    case '/': print(f"Result: {a / b}")
    case _: print("Invalid operator")
