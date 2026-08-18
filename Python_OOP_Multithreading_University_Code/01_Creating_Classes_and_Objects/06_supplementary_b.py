"""Supplement: object identity versus object equality."""

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def same_coordinates(self, other):
        return self.x == other.x and self.y == other.y

if __name__ == "__main__":
    a = Point(1, 2)
    b = Point(1, 2)
    c = a
    print("a is b:", a is b)
    print("a is c:", a is c)
    print("same coordinates:", a.same_coordinates(b))
