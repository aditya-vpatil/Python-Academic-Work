'''Check whether a given character is uppercase or lowercase'''
char = input("Enter a character: ")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
else:
    print("Not an alphabetic character")
