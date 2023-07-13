first, second, third = input('>>> ').split(" ", 2)
a = float(first)
b = float(second)
c = float(third)

discriminant = (b * b) - (4 * a * c)
r1 = (-b + (discriminant ** 0.5)) / (2 * a)
r2 = (-b - (discriminant ** 0.5)) / (2 * a)

if discriminant > 0:
    print("The equation has two roots", r1, "and", r2)
elif discriminant == 0:
    print("The equation has one root which is ", r1)
else:
    print('The equation has no real root')
