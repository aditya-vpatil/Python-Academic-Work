''' Calculate power without using pow ()'''

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))
answer = 1

for i in range(power):
    answer = answer * base

print("Answer =", answer)
