"""Supplement: scalar multiplication."""

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __repr__(self):
        return f"({self.x}, {self.y})"

if __name__ == "__main__":
    print(Vector(2, 3) * 4)
