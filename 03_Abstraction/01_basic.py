"""Abstraction using ABC."""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Return area of the shape."""

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.141592653589793 * self.radius ** 2


def print_area(shape: Shape):
    print(type(shape).__name__, "area =", round(shape.area(), 2))


def main():
    print_area(Rectangle(4, 5))
    print_area(Circle(3))


if __name__ == "__main__":
    main()
