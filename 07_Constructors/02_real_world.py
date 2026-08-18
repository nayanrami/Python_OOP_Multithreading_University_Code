"""Constructor validation prevents invalid objects."""

class Product:
    def __init__(self, sku: str, name: str, price: float, stock: int = 0):
        if not sku.strip():
            raise ValueError("SKU cannot be empty")
        if price < 0:
            raise ValueError("price cannot be negative")
        if stock < 0:
            raise ValueError("stock cannot be negative")
        self.sku = sku
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def inventory_value(self):
        return self.price * self.stock


def main():
    product = Product("P101", "SSD", 4999, 8)
    print(product.__dict__)
    print("Inventory value:", product.inventory_value())


if __name__ == "__main__":
    main()
