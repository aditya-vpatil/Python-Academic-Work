'''Count the number of vowels in a string. '''

vowels = "Python is easy,Java is not easy"
count = 0
for char in vowels :
    if char.lower() in "aeiouAEIOU":
        count +=1
print("The total number of vowels is: ",count)