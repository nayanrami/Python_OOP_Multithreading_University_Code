"""Supplement: property-backed percentage."""

class Percentage:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not 0 <= new_value <= 100:
            raise ValueError("0..100 only")
        self._value = new_value

if __name__ == "__main__":
    p = Percentage(75)
    p.value = 82
    print(p.value)
