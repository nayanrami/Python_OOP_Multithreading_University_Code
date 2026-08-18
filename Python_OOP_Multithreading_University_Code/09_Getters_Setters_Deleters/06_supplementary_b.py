"""Supplement: computed BMI property."""

class Person:
    def __init__(self, weight_kg, height_m):
        self.weight_kg = weight_kg
        self.height_m = height_m

    @property
    def bmi(self):
        return self.weight_kg / self.height_m ** 2

if __name__ == "__main__":
    print(round(Person(70, 1.75).bmi, 2))
