'''Print menu-based food selection using match case'''


choice = int(input("1. Burger\n2. Pizza\n3. Pasta\nEnter choice: "))
match choice:
    case 1: print("You selected Burger")
    case 2: print("You selected Pizza")
    case 3: print("You selected Pasta")
    case _: print("Invalid menu choice")
