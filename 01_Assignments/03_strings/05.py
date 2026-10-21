'''Count the number of consonants in a string. '''


text = "Python is easy,Java is not easy"
count = 0
for char in text:
    if char.isalpha() and char.lower() not in "aeiou":
        count += 1
print("Consonants:", count)