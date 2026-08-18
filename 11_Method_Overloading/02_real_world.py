"""Overload-like behavior using *args."""

class Calculator:
    def add(self, *values):
        if not values:
            return 0
        if not all(isinstance(v, (int, float)) for v in values):
            raise TypeError("all values must be numeric")
        return sum(values)


def main():
    calculator = Calculator()
    print(calculator.add())
    print(calculator.add(10))
    print(calculator.add(10, 20))
    print(calculator.add(10, 20, 30, 40))


if __name__ == "__main__":
    main()
