'''Remove punctuation marks from a string. '''

text = input("Enter a string: ")
punctuation = ".,!?;:'\"-()[]{}"
result = ""
for char in text:
    if char not in punctuation:
        result += char
print(result)