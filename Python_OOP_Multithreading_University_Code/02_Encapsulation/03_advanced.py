"""Encapsulation preserves class invariants."""

class InventoryItem:
    def __init__(self, sku: str, quantity: int):
        self.sku = sku
        self.__quantity = 0
        self.restock(quantity)

    @property
    def quantity(self) -> int:
        return self.__quantity

    def restock(self, units: int) -> None:
        if units < 0:
            raise ValueError("units cannot be negative")
        self.__quantity += units

    def sell(self, units: int) -> None:
        if units <= 0:
            raise ValueError("units must be positive")
        if units > self.__quantity:
            raise ValueError("insufficient stock")
        self.__quantity -= units


def main():
    item = InventoryItem("KB-101", 10)
    item.sell(3)
    item.restock(5)
    print("Safe quantity:", item.quantity)


if __name__ == "__main__":
    main()
