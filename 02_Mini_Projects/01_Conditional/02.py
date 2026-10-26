'''Online Shopping Checkout'''
name = input("Please Enter customer name: ")
amount = float(input("Please Enter purchase amount: rs"))
customer_type = input("Please Enter Customer type (Regular/Premium): ").lower()



if amount < 0:
    print("Purchase amount cannot be negative")
elif customer_type != "regular" and customer_type != "premium":
    print("Invalid customer type")
else:
    if amount >= 5000:   
        discount_rate = 20
    elif amount >= 4000:
        discount_rate = 10
    elif amount >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0


if customer_type == "regular":
    discount_rate = discount_rate
    discount = amount * discount_rate / 100
    amount_after_discount = amount - discount
if amount_after_discount >= 2000:
    delivery = 0

       
if customer_type == "premium":
    discount_rate = discount_rate + 5
    discount = amount * discount_rate / 100
    amount_after_discount = amount - discount
if amount_after_discount >= 2000:
    delivery = 0
else:
    delivery = 100


final_amount = amount_after_discount + delivery
print("Customer name:", name)
print("Discount amount: rs", discount)
print("Delivery charge: rs", delivery)
print("Final payable amount: rs", final_amount)