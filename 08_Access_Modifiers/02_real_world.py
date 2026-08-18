"""Protected member shared with a subclass."""

class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self._salary = salary

    def annual_salary(self):
        return self._salary * 12

class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float):
        super().__init__(name, salary)
        self._bonus = bonus

    def annual_salary(self):
        return self._salary * 12 + self._bonus


def main():
    manager = Manager("Neel", 80000, 100000)
    print(manager.name, manager.annual_salary())


if __name__ == "__main__":
    main()
