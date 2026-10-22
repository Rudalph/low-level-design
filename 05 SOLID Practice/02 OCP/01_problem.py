'''
Question 1: Shape Area Calculator (Easy)

You are developing a system that calculates the area of different geometric shapes.

The system should perform the following tasks:
    1. Support two shapes initially:
        - Rectangle: Area = length × width
        - Circle: Area = π × radius
    2. Calculate and display the area of each shape.
    3. Allow new shapes to be added in the future, such as:
        - Triangle: Area = 0.5 × base × height
        - Square: Area = side × side
    4. Adding a new shape should not require modifying the existing area calculation logic.

Your Task: Implement the Shape Area Calculator using OOP while following OCP and SRP. 
Demonstrate that you can add a Triangle without changing existing classes.
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def calculate_area(self):
        return self.length * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
class DisplayArea:
    def __init__(self, shape_object):
        self.area = shape_object.calculate_area()
        
    def print_area(self):
        print(f"Area of: {self.area}")
        
'''In future we need 2 more shapes Triangle and Square'''

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side
         
rectangle = Rectangle(10, 20)

area_displayer = DisplayArea(rectangle)
area_displayer.print_area()
