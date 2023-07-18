first, second, third = input('>>> ').split(" ", 2)
a = float(first)
b = float(second)
c = float(third)

discriminant = (b * b) - (4 * a * c)
radius1 = (-b + (discriminant ** 0.5)) / (2 * a)
radius2 = (-b - (discriminant ** 0.5)) / (2 * a)

if discriminant > 0:
    print("The equation has two roots", radius1, "and", radius2)
elif discriminant == 0:
    print("The equation has one root which is ", radius1)
else:
    print('The equation has no real root')
