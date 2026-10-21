'''Check exam results (Distinction, First Class, Pass, Fail)'''


marks = float(input("Enter marks: "))
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
elif marks <0:
    print("Invalid marks please enter valid marks")
else:
    print("Fail")
