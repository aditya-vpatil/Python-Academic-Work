'''ATM Withdrawal System'''


name = input("Please Enter account holder name: ")
balance = float(input("Please Enter current balance: rs "))
amount = float(input("Please Enter withdrawal amount: rs "))


print("Account holder:", name)
if balance < 0:    
    print("Invalid account balance")
elif amount <= 0:    
    print("Transaction rejected:-- amount must be greater than zero")
elif amount > 20000:
    print("Transaction rejected:-- maximum withdrawal is rs 20000")
elif amount > balance:    
    print("Transaction rejected:-- insufficient balance")



else:    
    remaining = balance - amount    
print("Transaction status: Successful")    
print("Withdrawn amount: rs", amount)
print("Remaining balance: rs", remaining)
if remaining < 1000:        
    print("Low Balance Warning")