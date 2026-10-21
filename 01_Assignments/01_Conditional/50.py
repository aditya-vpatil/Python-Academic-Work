'''Build a simple ATM menu using match cas'''


choice = int(input("1. Check Balance\n2. Deposit\n3. Withdraw\nEnter choice: "))
match choice:
    case 1: print("Your balance is 10000")

    case 2: print("Deposit successful")

    case 3: print("Please collect your cash")
    
    case _: print("Invalid ATM choice")
