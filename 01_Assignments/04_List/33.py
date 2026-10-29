''' Find the second largest number'''

numbers = [10, 40, 20, 50, 30]
unique_numbers = sorted(set(numbers))
if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("Second largest number does not exist")