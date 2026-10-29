'''Shopping Cart Total'''


products = int(input("Enter number of products: "))
subtotal = 0

for i in range (1 , products + 1):
    price = float (input("Enter product price: Rs "))
    quantity = int (input("Enter quantity: "))

    while price < 0 or quantity < 0 :
        print("Price and quality cannot be negative. ")
        price = float(input("Enter product price again: Rs "))
        quantity = int (input("Enter quantity again: "))

    subtotal = subtotal + (price * quantity)

if subtotal >= 3000:
    discount = subtotal * 0.10
else:
    discount = 0

amount = subtotal - discount

if amount < 1500:
    delivery = 100
else:
    delivery = 0

final_amount = amount + delivery

print("Subtotal: Rs", subtotal)
print("Discount: Rs", discount)
print("Delivery charge: Rs", delivery)
print("Final payable amount: ", final_amount ) 