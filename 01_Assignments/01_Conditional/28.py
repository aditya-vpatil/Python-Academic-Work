'''Calculate discounts based on total shopping amount'''


amount = float(input("Enter total shopping amount: "))
if amount > 5000:
    discount = amount * 0.2
elif amount > 2000:
    discount = amount * 0.1
else:
    discount = 0
print(f"Discount amount: {discount}")
