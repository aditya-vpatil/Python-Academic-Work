''' Print ASCII values of characters'''

text = input("Enter a string: ")

for ch in text:
    print(ch, "=", ord(ch))
