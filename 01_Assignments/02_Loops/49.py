''' Display a simple menu using while loop'''

choice = 0

while choice != 4:
    print("1. Subtract two numbers")
    print("2. Multiply two numbers")
    print("3. Add two numbers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Answer =", a - b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Answer =", a * b)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Answer =", a + b)

    elif choice == 4:
        print("Program ended")

    else:
        print("Invalid choice")

    print()
