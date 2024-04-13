import math

PI = 3.14


def calculate_circle_area(radius):
    area = PI * radius**2
    # area = math.pi * (radius**2)
    return area


radius = float(input("Enter the radius :"))


print(calculate_circle_area(radius))
