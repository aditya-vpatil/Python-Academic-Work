''' Mobile Data Plan Bill '''

C_name = input("Please enter your name: ")
P_type = input("Please select Plan type (Basic, Standard, Premium): ").lower()
Extra_Data = float(input("Please enter the extra data you used in GB: "))


if Extra_Data <0 :
    print("Data usage cannot be negative")

elif P_type == "basic":
    base_charge = 299 
    Extra_charge = Extra_Data * 20
    if Extra_Data >10:
        surcharge = 100
    else:
        surcharge = 0  

    total_bill = base_charge + Extra_charge + surcharge


elif P_type == "standard":
    base_charge = 499
    Extra_charge = Extra_Data * 20
    if Extra_Data >10:
        surcharge = 100
    else:
        surcharge = 0  
    total_bill = base_charge + Extra_charge + surcharge

elif P_type == ("premium"):
    base_charge = 799
    Extra_charge = Extra_Data * 20
    if Extra_Data >10:
        surcharge = 100
    else:
        surcharge = 0  
    total_bill = base_charge + Extra_charge + surcharge

else:
    print("Invalid plan type")



print("Customer name: ", C_name)
print("Plan type: ",P_type) 
print("Base plan charge: rs",base_charge)
print("Extra data charge: rs",Extra_charge)
print("Surcharge: rs", surcharge)
print("Final bill: rs", base_charge + Extra_Data + surcharge)







    



