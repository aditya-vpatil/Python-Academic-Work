'''Check user role using match case'''


role = input("Enter user role (admin, user, guest): ").lower()
match role:
    case "admin": print("Access granted to all controls")
    case "user": print("Access granted to standard features")
    case "guest": print("Access granted to view-only mode")
    case _: print("Unknown role")
