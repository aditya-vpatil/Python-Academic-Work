''' Check whether a number is palindrome'''

num = int(input("Enter a number: "))
original = num
temp = (num)
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num >= 0 and original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
