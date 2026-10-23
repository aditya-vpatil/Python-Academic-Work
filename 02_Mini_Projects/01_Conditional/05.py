''' Employee Performance Bonus'''


name = input("Please Enter employee name : ")
salary = float(input("Please Enter monthly salary : "))
experience = float(input("Please Enter years of experience : "))
rating = float(input("Please Enter performance rating 1 to 5 : "))


if salary <0 and experience < 0:
    print("please Enter valid details")
elif rating <1 or rating >5 :
    print("Please enter valid rating")

else:

    
    if experience >=10 and rating >=4:
        bonus_rate = 20
    elif experience >=5 and rating >=4:
        bonus_rate = 15
    elif experience >=2 and rating >=3:
        bonus_rate = 10
    else:
        bonus_rate = 0 
    bonus = salary * bonus_rate / 100
    final_salary = salary + bonus


print("Name: ",name)
print("Bonus percentage: ",bonus_rate)
print("Bonus amount: rs",bonus)
print("Final_salary: rs",final_salary)


if rating == 5:
    print("Excellent Performance")

elif bonus_rate == 0:
    print("No bonus") 

else :
    print("Good work")









    