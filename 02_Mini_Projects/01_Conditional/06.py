'''Hotel Room Booking System'''


G_name = input("Please enter your name: ")
R_type = input("Please select Room type (Standard / Deluxe / Suite): ")
N_nights = int(input("Please select number of nights you want to stay: "))



if N_nights <=0:
    print(" Number of nights must be greater than 0")


elif R_type == "Standard":
    price = 2000
    room_charge = price * N_nights

    if N_nights >=10 :
        discount = room_charge * 20 / 100
    elif N_nights >=5 :
        discount = room_charge * 10 / 100
    else :
        discount = 0
else:
    print("Invalid room type")





if N_nights <=0:
    print(" Number of nights must be greater than 0")

elif R_type == "Deluxe":
    price = 3500
    room_charge = price * N_nights

    if N_nights >=10 :
        discount = room_charge * 20 / 100
    elif N_nights >=5 :
        discount = room_charge * 10 / 100
    else :
        discount = 0
else: 
    print("Invalid room type")




if N_nights <=0:
    print(" Number of nights must be greater than 0")

elif R_type == "Suite":
    price = 6000
    room_charge = price * N_nights

    if N_nights >=10 :
        discount = room_charge * 20 / 100
    elif N_nights >=5 :
        discount = room_charge * 10 / 100
    else :
        discount = 0
else :
    print("Invalid Room type")


print("Guest name: ",G_name)
print("Room type: Standard")
print("Number of nights: ",N_nights)
print("Room charge: rs",room_charge)
print("Discount: rs",discount)
print("Final booking amount: rs",room_charge - discount)


