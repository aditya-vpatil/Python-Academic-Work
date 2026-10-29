''' Replace an element at a given index'''


lst = (1,2,3,4,5)

ind=int(input("Enter the inndex: (0-4)" ))
value = int(input("Enter the value: "))

if 0<= ind <len(lst):
    print(lst[ind]) = value
else:
    print("Invalid index")