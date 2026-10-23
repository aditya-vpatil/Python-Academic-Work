'''Insurance Premium Calculator'''


C_name = input("Please enter customer name: ")
Age = int(input("Please enter age: "))
Risk = input("Occupation Risk (Low/Medium/High): ").lower()
Smoker = input("Are you a Smoker? (Yes/No): ").lower()


if Age < 0:
    print("Age cannot be negative")
elif Age < 18:
    print("Customer name:", C_name)    
    print("Eligibility: Not eligible")
elif Risk != "low" and Risk != "medium" and Risk != "high":
        print("Invalid occupation Risk")
elif Smoker != "yes" and Smoker != "no":   
    print("Please enter Yes or No for Smoker")

    
else:    
    base_premium = 10000    
    extra = 0    
    if Age > 50:        
        extra = extra + 5000    
    if Risk == "high":        
        extra = extra + 7000    
    elif Risk == "medium":
        extra = extra + 3000    
    if Smoker == "yes":        
        extra = extra + 5000  
print("Customer name:", C_name)    
print("Eligibility: Eligible")   
print("Base premium: rs", base_premium)  
print("Additional charges: rs", extra)
print("Final premium: rs", base_premium + extra)    
if extra >= 10000:        
    print("High Risk Policy")    
else:        
    print("Normal Risk Policy")