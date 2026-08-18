"""Computed and read-only properties."""

class Employee:
    def __init__(self, first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self._monthly_salary = monthly_salary

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value):
        if value < 0:
            raise ValueError("salary cannot be negative")
        self._monthly_salary = value

    @property
    def annual_salary(self):
        return self.monthly_salary * 12


def main():
    employee = Employee("Rohan", "Patel", 60000)
    print(employee.full_name)
    employee.monthly_salary = 65000
    print(employee.annual_salary)


if __name__ == "__main__":
    main()
