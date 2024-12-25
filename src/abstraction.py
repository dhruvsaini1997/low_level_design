from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes.
    Forces all subclasses to implement the `area` method.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method for calculating the area of the shape.
        Must be implemented by subclasses.
        """
        pass


class Square(Shape):
    """
    Subclass of Shape representing a square.
    """
    def __init__(self, side):
        self.side = side

    def area(self):
        """
        Calculate and return the area of the square.
        """
        return self.side ** 2


class Circle(Shape):
    """
    Subclass of Shape representing a circle.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return 3.14 * self.radius ** 2


if __name__ == '__main__':
    shapes = [
        Square(4),
        Circle(3),
        Square(7),
        Circle(1.5)
    ]


    for shape in shapes:
        print(f"The area of the shape is: {shape.area()}")
