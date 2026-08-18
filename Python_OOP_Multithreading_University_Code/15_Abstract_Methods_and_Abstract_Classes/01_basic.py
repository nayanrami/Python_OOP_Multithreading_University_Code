"""Abstract method and concrete subclasses."""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    def describe(self):
        return f"{type(self).__name__} area = {self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height


def main():
    for shape in [Circle(2), Rectangle(3, 5)]:
        print(shape.describe())


if __name__ == "__main__":
    main()
