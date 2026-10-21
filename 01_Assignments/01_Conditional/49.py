'''Print result status using match case'''


status = input("Enter status (Pass, Fail, Absent): ").capitalize()
match status:
    case "Pass": print("Congratulations, you passed!")
    case "Fail": print("Better luck next time.")
    case "Absent": print("You were absent for the examination.")
    case _: print("Invalid status entered")
