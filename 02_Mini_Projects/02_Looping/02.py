'''Student Marks and Grade Report'''

students = int(input("Enter number of students: "))
total_marks  = 0 
pass_count   = 0
fail_count   = 0

for i in range ( 1, students + 1):
    name = input("Enter students name: ")
    marks = float(input("Enter marks out of 100: "))

    while marks < 0 or marks >100 :
        print("Marks must be between o and 100: ")
        marks = float(input("Enter marks again: "))
    
    total_marks = total_marks + marks

    if marks >= 75 :
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40 :
        grade = "D"
    else :
        grade = "Fail"

    if marks >= 40:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

    print(name, "- Grade: ", grade)

if students > 0:
    average = total_marks / students
else:
    average = 0

print("Class average:", average)
print("pass count:",pass_count)
print("Fail count:" ,fail_count)