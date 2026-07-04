import math

radius = float(input("Enter the radius of the circle to calculate the circumference: "))
Circumference = 2 * math.pi * radius
print(f"The Circumference of the circle: {round(Circumference,2)}")

r = float(input("Enter the radius to calculate the area of the circle: "))
area = math.pi * math.pow(r,2)
print(f"The area : {round(area,2)}")

base = float(input("\nEnter the base length of the triangle: "))
n_side = float(input("Enter the next side length of the triangle: "))
hypotenuse = math.sqrt(math.pow(base,2) + math.pow(n_side,2))
print(f"Hypotenuse side length : {hypotenuse}")