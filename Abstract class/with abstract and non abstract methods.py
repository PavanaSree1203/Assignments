from abc import ABC, abstractmethod

class Shape(ABC):
    def display(self):
        print("This is a shape.")

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Example usage:
circle = Circle(5)
circle.display()
print("Circle area:", circle.area())

square = Square(4)
square.display()
print("Square area:", square.area())