"""Safe money addition and comparison."""

class Money:
    def __init__(self, amount: float, currency: str = "INR"):
        self.amount = float(amount)
        self.currency = currency

    def _check(self, other):
        if not isinstance(other, Money) or other.currency != self.currency:
            raise TypeError("Money objects must use the same currency")

    def __add__(self, other):
        self._check(other)
        return Money(self.amount + other.amount, self.currency)

    def __lt__(self, other):
        self._check(other)
        return self.amount < other.amount

    def __eq__(self, other):
        return isinstance(other, Money) and self.currency == other.currency and self.amount == other.amount

    def __repr__(self):
        return f"{self.currency} {self.amount:.2f}"


def main():
    a, b = Money(500), Money(750)
    print(a + b)
    print(a < b)
    print(a == Money(500))


if __name__ == "__main__":
    main()
