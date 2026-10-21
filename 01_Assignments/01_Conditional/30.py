"""Check the type of number (single, double, or three digit)."""


num = int(input("Enter a positive integer: "))
if 0 <= num <= 9:
    print("Single-digit number")
elif 10 <= num <= 99:
    print("Double-digit number")
elif 100 <= num <= 999:
    print("Three-digit number")
else:
    print("Number has more than three digits")
