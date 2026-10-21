'''Check traffic signal actions using match case'''


signal = input("Enter traffic light color (Red, Yellow, Green): ").capitalize()
match signal:
    case "Red": print("Stop")
    case "Yellow": print("Get Ready")
    case "Green": print("Go")
    case _: print("Invalid signal color")
