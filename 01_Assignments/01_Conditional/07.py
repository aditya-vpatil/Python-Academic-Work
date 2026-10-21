'''To check whether a character is a vowel or consonant'''

char = input("Enter a character: ").lower()
if char in 'aeiou' :
    print("The character is a vowel")
else:
    print ("The character is consonant")