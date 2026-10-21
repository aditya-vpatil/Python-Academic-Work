'''Check grade based on marks'''


marks = float(input("Enter marks: "))
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
elif marks <0:
    print("Invalid marks please enter valid marks")
else:
    print("Fail")
