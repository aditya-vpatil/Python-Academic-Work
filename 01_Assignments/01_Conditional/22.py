'''Check salary bonus based on years of service'''


years = float(input("Enter years of service: "))
if years >=5:
    print("Bonus: 10%")

elif years >5 and years <10:
    print("Bonus: 20%")

elif years >10 and years <15:
    print("Bonus: 30%")

else :
    print ("Enter valid years")


