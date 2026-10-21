'''Print grade description using match case'''


grade = input("Enter grade (A, B, C, F): ").upper()
match grade:
    case "A": print("Excellent")
    case "B": print("Good")
    case "C": print("Average")
    case "F": print("Fail")
    case _: print("Invalid grade")
