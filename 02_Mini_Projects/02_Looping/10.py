'''Multiplication Table and Number Analyzer'''

number = int(input("Enter a positive integer for the table: "))
while number <= 0:
    print("Please enter a positive integer.")
    number = int(input("Enter the number again: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
start = int(input("Enter range start: "))
end = int(input("Enter range end: "))
while start > end:
    print("Start must not be greater than end.")
    start = int(input("Enter range start again: "))
    end = int(input("Enter range end again: "))
even_count = 0
odd_count = 0
total = 0
for value in range(start, end + 1):
    total = total + value
    if value % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum of range:", total)