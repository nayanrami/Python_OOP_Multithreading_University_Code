"""Class method as an alternate constructor."""

from datetime import date

class Employee:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def from_age(cls, name: str, age: int):
        return cls(name, date.today().year - age)

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    def approximate_age(self):
        return date.today().year - self.birth_year


def main():
    employee = Employee.from_age("Krish", 25)
    print(employee.name, employee.birth_year, employee.approximate_age())
    print(Employee.is_adult(17), Employee.is_adult(21))


if __name__ == "__main__":
    main()
