'''Check whether a student is eligible for an exam (attendance + marks)'''


attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter internal marks: "))
if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible: Marks too low")
else:
    print("Not eligible: Attendance too low")
