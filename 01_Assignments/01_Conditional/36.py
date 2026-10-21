'''Check whether a person is eligible for a driving license'''


age = int(input("Enter age: "))
passed_test = input("Passed driving test? (yes/no): ").lower()
if age >= 18:
    if passed_test == "yes":
        print("Eligible for driving license")
    else:
        print("Not eligible: Driving test not passed")
else:
    print("Not eligible: Age below 18")
