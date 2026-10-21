''' Add numbers until user enters zero'''

total = 0
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    total = total + num
    num = int(input("Enter a number (0 to stop): "))

print("Sum =", total)
