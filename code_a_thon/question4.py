import math


def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))

    area = math.pi * (radius ** 2)

    print(f"The area  of the circle is {area:.3f}")


area_of_circle()
