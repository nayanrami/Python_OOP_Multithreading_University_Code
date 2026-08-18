"""Supplement: inheritance-aware constructors."""

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

if __name__ == "__main__":
    car = Car("ExampleBrand", 5)
    print(car.brand, car.seats)
