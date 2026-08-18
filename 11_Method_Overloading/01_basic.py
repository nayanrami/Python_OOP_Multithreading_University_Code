"""Overload-like behavior using default arguments."""

class AreaCalculator:
    def area(self, length: float, width: float | None = None) -> float:
        # One argument -> square; two arguments -> rectangle.
        if width is None:
            return length * length
        return length * width


def main():
    calc = AreaCalculator()
    print("Square:", calc.area(5))
    print("Rectangle:", calc.area(5, 8))


if __name__ == "__main__":
    main()
