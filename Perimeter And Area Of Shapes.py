import math

# Define the base class "Shape" that contains the "perimeter" and "area" methods
class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass

# Define the "Circle" class that inherits from "Shape" and contains the "perimeter" and "area" methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

# Define the "Triangle" class that inherits from "Shape" and contains the "perimeter" and "area" methods
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def perimeter(self):
        return self.base + 2 * math.sqrt((0.5 * self.base) ** 2 + self.height ** 2)

    def area(self):
        return 0.5 * self.base * self.height

# Define the "Rectangle" class that inherits from "Shape" and contains the "perimeter" and "area" methods
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

# Test the program

# Prompt the user to select the shape type
shape_type = input("Please select the shape type (Circle, Triangle, Rectangle): ")

if shape_type == "Circle":
    # If "Circle" is selected, prompt the user to enter the radius value
    radius = float(input("Please enter the radius value of the circle: "))
    # Create an object of the "Circle" class using the entered radius value
    circle = Circle(radius)
    # Print the perimeter and area of the circle using the appropriate methods in the "Circle" class
    print("Circle perimeter:", circle.perimeter())
    print("Circle area:", circle.area())

elif shape_type == "Triangle":
    # If "Triangle" is selected, prompt the user to enter the base and height values of the triangle
    base = float(input("Please enter the base value of the triangle: "))
    height = float(input("Please enter the height value of the triangle: "))
    # Create an object of the "Triangle" class using the entered base and height values
    triangle = Triangle(base, height)
    # Print the perimeter and area of the triangle using the appropriate methods in the "Triangle" class
    print("Triangle perimeter:", triangle.perimeter())
    print("Triangle area:", triangle.area())

elif shape_type == "Rectangle":
    # If "Rectangle" is selected, prompt the user to enter the length and width values of the rectangle
    length = float(input("Please enter the length value of the rectangle: "))
    width = float(input("Please enter the width value of the rectangle: "))
    # Create an object of the "Rectangle" class using the entered length and width values
    rectangle = Rectangle(length, width)
    # Print the perimeter and area of the rectangle using the appropriate methods in the "Rectangle" class
    print("Rectangle perimeter:", rectangle.perimeter())
    print("Rectangle area:", rectangle.area())

else:
    print("Invalid shape type!")