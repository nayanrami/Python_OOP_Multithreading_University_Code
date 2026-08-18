"""Getter/setter/deleter behavior with @property."""

class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("temperature cannot be below absolute zero")
        self._celsius = float(value)

    @celsius.deleter
    def celsius(self):
        print("Temperature value deleted")
        del self._celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


def main():
    t = Temperature(25)
    print(t.celsius, t.fahrenheit)
    t.celsius = 30
    print(t.celsius, t.fahrenheit)
    del t.celsius


if __name__ == "__main__":
    main()
