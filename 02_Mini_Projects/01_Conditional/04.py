'''Student Scholarship Eligibility'''

name = input("Please Enter student name: ")
percentage = float(input("Please Enter percentage: "))
income = float(input("Please Enter annual family income: rs "))
attendance= float(input("Please Enter attendance percentage: "))

print("Student name:", name)


if percentage < 0 or percentage > 100 or attendance < 0 or attendance > 100 or income < 0 :
    print("Please enter valid details")
elif percentage > 75 and income <= 400000 and attendance >= 75:
    print("Eligibility status : Eligible")
else:
    print("Eligibility status: Not Eligible")

 
if percentage >= 90:       
    print("Scholarship category: Full Scholarship") 
else:
    print("Scholarship category: Partial Scholarship")


if percentage  <75:
    print("Reason: Percentage is below 75%")
elif income > 400000:
    print("Reason: Family income is above rs 400000")
elif attendance <75 : 
    print("Reason: Attendance is below 75%")










