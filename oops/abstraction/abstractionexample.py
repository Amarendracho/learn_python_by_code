# abstract classes have only method declaration not implementation.
#       abstract methods inherit for child classes and implement happen at child class.

# First import package (from abc import ABC, abstractmethod)
    # abc(abstract base class)

# abstract methods have Decoration with @abstarctmethod

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"{3.14 * self.radius ** 2} cm²"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return f"{self.side ** 2} cm²"

class Rectangle(Shape):
    def __init__(self, base,height):
        self.base = base
        self.height = height

    def area(self):
        return f"{self.base * self.height / 2} cm²"

shapes = [Circle(4),Square(8),Rectangle(6,7)]
for shape in shapes:
    print(shape.area())