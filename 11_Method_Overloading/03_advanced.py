"""Type-based dispatch with functools.singledispatchmethod."""

from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    def format(self, value):
        return f"generic:{value}"

    @format.register
    def _(self, value: int):
        return f"integer:{value:,}"

    @format.register
    def _(self, value: float):
        return f"float:{value:.2f}"

    @format.register
    def _(self, value: list):
        return "list:[" + ", ".join(map(str, value)) + "]"


def main():
    formatter = Formatter()
    for value in [123456, 3.14159, [1, 2, 3], {"a": 1}]:
        print(formatter.format(value))


if __name__ == "__main__":
    main()
