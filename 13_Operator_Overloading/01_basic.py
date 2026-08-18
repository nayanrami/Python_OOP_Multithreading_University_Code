"""Vector addition using __add__."""

class Vector:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"


def main():
    print(Vector(2, 3) + Vector(5, 7))


if __name__ == "__main__":
    main()
