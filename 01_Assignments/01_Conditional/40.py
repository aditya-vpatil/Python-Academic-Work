'''Check whether a password is valid using nested if'''


password = input("Enter password: ")
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Valid password")
    else:
        print("Invalid: Must contain at least one digit")
else:
    print("Invalid: Must be at least 8 characters long")
