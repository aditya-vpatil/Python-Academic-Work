'''Smart Electricity Bill Calculator'''

name = input("Please Enter customer name: ")
units = float(input("Please Enter units consumed: "))




if units < 0:
        print("Units cannot be negative")

elif units <= 100:
        units_charge = units * 3    
        bill = units_charge + 150    
        print("Customer name:", name)
        print("Units consumed:", units)
        print("units charge: rs", units_charge)
        print("Service charge: rs150")
        print("Final bill: rs", bill)
        if bill > 2000:
            print("High Usage Bill")
        else:   
            print("Normal usage bill")


elif units <= 200:
    units_charge = 100 * 3 + (units - 100) * 5
    bill = units_charge + 150
    print("Customer name:", name)
    print("Units consumed:", units)
    print("units charge: rs", units_charge)
    print("Service charge: rs150")
    print("Final bill: rs", bill)  
    if bill > 2000:        
        print("High Usage Bill")
    else:        
        print("Normal usage bill")


else:
    units_charge = 100 * 3 + 100 * 5 + (units - 200) * 7
    bill = units_charge + 150
    print("Customer name:", name)
    print("Units consumed:", units)
    print("units charge: rs", units_charge)
    print("Service charge: rs150")
    print("Final bill: rs", bill)
    if bill > 2000:        
        print("High Usage Bill")
    else:        
        print("Normal usage bill")