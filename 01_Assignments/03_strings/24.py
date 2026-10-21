''' Extract only digits from a string.'''

text = input("Please enter the string: ")
digit = " "

for char in text :
    if char.isdigit():
        digit += char
print(digit)