''' Print a string in reverse order'''

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reverse string =", reverse)
