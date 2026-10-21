'''Find the ASCII value of each character in a string. '''

text = input("Enter a string: ")
for char in text:
    print(char, ":", ord(char))