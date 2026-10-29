'''Create a list and find common elements between two lists'''

lst = [1,2,3,4,5,8]
lst_1 = [6,5,8,3,2,9]

common = list(dict.fromkeys(item for item in lst if item in lst_1))
print(common)