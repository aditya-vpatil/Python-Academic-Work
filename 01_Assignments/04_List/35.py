'''Create a list and remove all even numbers'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)