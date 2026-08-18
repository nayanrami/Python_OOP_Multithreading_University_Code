"""Supplement: class-level configuration."""

class Tax:
    rate = 0.05

    @classmethod
    def change_rate(cls, new_rate):
        cls.rate = new_rate

    def amount(self, price):
        return price * self.rate

if __name__ == "__main__":
    t = Tax()
    print(t.amount(1000))
    Tax.change_rate(0.08)
    print(t.amount(1000))
