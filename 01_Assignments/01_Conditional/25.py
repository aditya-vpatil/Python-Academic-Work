'''Check whether a triangle is equilateral, isosceles, or scalene'''


a = float(input("Enter side no 1: "))
b = float(input("Enter side no 2: "))
c = float(input("Enter side no 3: "))
if a == b == c:
    print("Equilatral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Sclene triangle")
