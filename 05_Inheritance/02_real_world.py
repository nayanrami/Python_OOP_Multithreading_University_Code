"""Hierarchical inheritance."""

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def monthly_pay(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self, name, base_salary, skill_bonus):
        super().__init__(name, base_salary)
        self.skill_bonus = skill_bonus

    def monthly_pay(self):
        return super().monthly_pay() + self.skill_bonus

class SalesEmployee(Employee):
    def __init__(self, name, base_salary, commission):
        super().__init__(name, base_salary)
        self.commission = commission

    def monthly_pay(self):
        return super().monthly_pay() + self.commission


def main():
    staff = [Developer("Vivan", 50000, 5000), SalesEmployee("Sara", 40000, 12000)]
    for employee in staff:
        print(employee.name, employee.monthly_pay())


if __name__ == "__main__":
    main()
