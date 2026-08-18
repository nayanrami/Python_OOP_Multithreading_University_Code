"""Strategy-style polymorphism."""

class Discount:
    def apply(self, amount: float) -> float:
        return amount

class StudentDiscount(Discount):
    def apply(self, amount):
        return amount * 0.90

class FestivalDiscount(Discount):
    def apply(self, amount):
        return amount * 0.80

class NoDiscount(Discount):
    pass

class Checkout:
    def __init__(self, discount: Discount):
        self.discount = discount

    def total(self, amount: float) -> float:
        return self.discount.apply(amount)


def main():
    for strategy in [NoDiscount(), StudentDiscount(), FestivalDiscount()]:
        bill = Checkout(strategy)
        print(type(strategy).__name__, "=>", bill.total(1000))


if __name__ == "__main__":
    main()
