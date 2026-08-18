"""Class attributes, composition and object collaboration."""

class Item:
    def __init__(self, name: str, unit_price: float):
        self.name = name
        self.unit_price = unit_price


class Cart:
    tax_rate = 0.05

    def __init__(self, owner: str):
        self.owner = owner
        self._lines: list[tuple[Item, int]] = []

    def add(self, item: Item, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._lines.append((item, quantity))

    def subtotal(self) -> float:
        return sum(item.unit_price * qty for item, qty in self._lines)

    def total(self) -> float:
        return self.subtotal() * (1 + self.tax_rate)

    def receipt(self) -> None:
        print(f"Cart owner: {self.owner}")
        for item, qty in self._lines:
            print(f"  {item.name:15} x {qty:<2} = {item.unit_price * qty:.2f}")
        print(f"Subtotal: {self.subtotal():.2f}")
        print(f"Total:    {self.total():.2f}")


def main():
    mouse = Item("Mouse", 650)
    keyboard = Item("Keyboard", 1200)
    cart = Cart("Riya")
    cart.add(mouse, 2)
    cart.add(keyboard)
    cart.receipt()


if __name__ == "__main__":
    main()
