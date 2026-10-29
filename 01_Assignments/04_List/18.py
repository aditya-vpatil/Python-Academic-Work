'''Take user input to create a list'''

lst = input("Enter the numbers seprating by space: ").split()

lst = [int(lst) for lst in lst]

print(lst)