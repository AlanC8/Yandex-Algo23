import math
# 1
# x = round(math.radians(int(input("Input degree: "))), 6)
# print(f"Output radian: {x}")

# 2

# def area(height, base1, base2):
#     return (height * base1 + height * base2) / 2


# a = area(int(input("Height: ")), int(input("Base, first value: ")),
#          int(input("Base, second value: ")))
# print(f"Expected Output: {a}")

# 3
side = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))


def polygon_area(sides, length):
    perimeter = sides * length
    length /= 2
    degree_polygon = 360 / (sides * 2)
    a = math.cos(degree_polygon) * length / math.sin(degree_polygon)
    area = (a * length) / 2
    return sides * area


if (side == 4):
    print(f"The area of the polygon is: {length ** 2}")
else:
    print(f"The area of the polygon is: {polygon_area(side, length)}")
# 4


# def parallelogram_area(base, height):
#     return base * height


# area_parallelogram = parallelogram_area(
#     int(input("Length of base: ")), int(input("Height of parallelogram: ")))

# print(f"Expected Output: {area_parallelogram}")
