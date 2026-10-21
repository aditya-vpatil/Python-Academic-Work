'''Check whether a student passed all subjects'''


s1 = float(input("Marks in subject 1: "))
s2 = float(input("Marks in subject 2: "))
s3 = float(input("Marks in subject 3: "))
if s1 >= 40 and s2 >= 40 and s3 >= 40:
    print("Passed all subjects")
else:
    print("Failed in one or more subjects")
