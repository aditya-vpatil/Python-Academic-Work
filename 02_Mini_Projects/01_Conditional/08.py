'''Movie Ticket Booking'''

C_name = input("Please enter your name: ")
Age = int(input("Please enter your age: "))
S_type = input("Morning or Evening: ").lower()
Day_type = input("Weekday or weekend: ").lower()


if Age <0 :
    print("PLease enter valid Age")

elif S_type != "morning" and S_type != "evening":
    print("Invalid show type ")

elif Day_type != "weekday" and Day_type != "weekend":
    print("Invalid show type")

else:
    price = 200 
    discount = 0
    surcharge = 0 
    if Age <12:
        discount = 100 

    elif Age >= 60 :
        discount = 60

    if S_type == "morning":
        discount = discount  + 30 

    if Day_type == "weekday" :
        surcharge = 50 
    else:
        surcharge = 0
                
    final_price = price - discount + surcharge 

print("C_name: ",C_name)
print("original Ticket price: rs:",price)
print("Discount: rs",discount)
print("Weekday surcharge: rs",surcharge)
print("Final price: rs",final_price)