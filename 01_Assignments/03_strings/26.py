'''.Find the first and last occurrence of a character'''

text = input("Enter a string: ")
char = input("Enter one character: ")

print("First occurrence:", text.find(char))
print("Last occurrence:", text.rfind(char))