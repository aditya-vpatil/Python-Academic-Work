'''create a list of 10 numbers and remomve duplicates.'''

lst = [1,2,3,2,4,2,3,5,]

duplicates = list(dict.fromkeys(lst))

print(duplicates)