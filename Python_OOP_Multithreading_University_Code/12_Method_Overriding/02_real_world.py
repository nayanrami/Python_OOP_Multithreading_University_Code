"""Overriding with super()."""

class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def calculate_pay(self):
        return self.base_pay

class FullTimeEmployee(Employee):
    def __init__(self, name, base_pay, allowance):
        super().__init__(name, base_pay)
        self.allowance = allowance

    def calculate_pay(self):
        return super().calculate_pay() + self.allowance

class ContractEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name, 0)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours * self.hourly_rate


def main():
    staff = [FullTimeEmployee("Asha", 50000, 5000), ContractEmployee("Om", 80, 700)]
    for employee in staff:
        print(employee.name, employee.calculate_pay())


if __name__ == "__main__":
    main()
