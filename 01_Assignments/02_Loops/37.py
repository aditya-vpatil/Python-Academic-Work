''' Print numbers until a negative number is entered'''

num = int(input("Enter a number: "))

while num >= 0:
    print(num)
    num = int(input("Enter a number: "))

print("Negative number entered. Stopped.")
