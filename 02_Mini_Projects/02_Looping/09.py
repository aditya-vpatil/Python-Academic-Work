'''Bank trasaction history'''

balance = float(input("Enter opening balance: Rs "))
transactions = int(input("Enter number of transactions: "))
deposits = 0
successful_withdrawals = 0
rejected_withdrawals = 0
for i in range(1, transactions + 1):
    transaction_type = input("Enter deposit or withdraw: ").strip().lower()
    amount = float(input("Enter amount: Rs "))
    if amount < 0:
        print("Amount cannot be negative.")
    elif transaction_type == "deposit":
        balance = balance + amount
        deposits = deposits + 1
        print("Deposit successful")
    elif transaction_type == "withdraw":
        if amount <= balance:
            balance = balance - amount
            successful_withdrawals = successful_withdrawals + 1
            print("Withdrawal successful")
        else:
            rejected_withdrawals = rejected_withdrawals + 1
            print("Insufficient balance")
    else:
        print("Invalid transaction type")
print("Final balance: Rs", balance)
print("Deposits:", deposits)
print("Successful withdrawals:", successful_withdrawals)
print("Rejected withdrawals:", rejected_withdrawals)
if balance < 1000:
    print("Warning: Balance below Rs 1,000")