'''Count words in a string'''

text = input("Enter a sentence: ")
count = 0
inside_word = False

for ch in text:
    if ch != " " and not inside_word:
        count = count + 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Number of words =", count)
