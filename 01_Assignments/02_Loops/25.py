''' Count consonants in a string'''

text = input("Enter a string: ")
count = 0

for ch in text:
    if (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z"):
        if ch not in "aeiouAEIOU":
            count = count + 1

print("Number of consonants =", count)
