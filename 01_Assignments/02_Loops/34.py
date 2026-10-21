''' Check whether a string is palindrome'''

text = input("Enter a string: ")
reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")
