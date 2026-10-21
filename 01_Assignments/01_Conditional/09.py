'''Check whether a student has passed or failed'''
marks = int(input("Enter marks: "))
if marks <0 or marks >100:
    print("Invald")
elif marks >= 40 and marks <=100:
    print("Passed")
else:
    print("Failed")
