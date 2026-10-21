'''Check ticket price based on age'''


age = int(input("Enter age: "))
if age <0:
    print("Enter valid age") 
elif age <5 and age >0:
    print("Free ticket")
elif age <= 12:
    print("Child ticket: $5")
elif age <= 59:
    print("Adult ticket: $10")
elif age >=75:
    print("Free ticket for senior citizen")
   
else:
    print("Senior ticket: $7")
