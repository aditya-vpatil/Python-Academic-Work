'''Restaurant Bill and Service Charge'''


name = input("Enter customer name: ")
bill = float(input("Enter food bill amount: rs"))
member = input("Are you a member? (Yes/No): ").lower()


if bill < 0:
    print("Bill amount cannot be negative")
elif member != "yes" and member != "no":  
    int("Please enter Yes or No for membership")

else:

    if bill >= 5000:
        discount_rate = 15
    elif bill >= 3000:        
        discount_rate = 10    
    elif bill >= 1000:        
        discount_rate = 5    


    if member == "yes":            
        discount_rate = 5    


    else:
        discount_rate = discount_rate + 5    
        discount = bill * discount_rate / 100    
        amount_after_discount = bill - discount    
        service_charge = amount_after_discount * 5 / 100    
        final_amount = amount_after_discount + service_charge    



print("Customer name: ", name)
print("Original bill: rs ", bill)    
print("Discount: rs ", discount)    
print("Service charge: rs ", service_charge)    
print("Final payable amount: rs ", final_amount)  


if final_amount >= 5000:        
    print("Thank you for being a valued customer")