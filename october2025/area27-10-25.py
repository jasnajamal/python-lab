

from area_module import area_rectangle, area_circle


length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))


radius = float(input("Enter radius of circle: "))

rect_area = area_rectangle(length, width)
circle_area = area_circle(radius)

print(f"Area of Rectangle = {rect_area}")
print(f"Area of Circle = {circle_area:.2f}")
