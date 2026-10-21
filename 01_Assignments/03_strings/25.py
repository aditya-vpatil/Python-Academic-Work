''' Extract only alphabets from a string'''

text = input("Please enter the text: ")
char = " "

for i in text:
    if i.isalpha():
        char += i
print(char)