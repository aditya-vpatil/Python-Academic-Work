''' Print a number triangle pattern'''

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for t in range(1, i + 1):
        print(t, end=" ")
    print()
