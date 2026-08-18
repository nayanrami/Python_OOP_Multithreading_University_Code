"""Abstract employee payroll design."""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    @abstractmethod
    def calculate_pay(self) -> float:
        pass

    def payslip(self):
        return f"{self.employee_id} | {self.name} | Pay={self.calculate_pay():.2f}"

class SalariedEmployee(Employee):
    def __init__(self, employee_id, name, monthly_salary):
        super().__init__(employee_id, name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, employee_id, name, hours, rate):
        super().__init__(employee_id, name)
        self.hours, self.rate = hours, rate

    def calculate_pay(self):
        return self.hours * self.rate


def main():
    employees = [SalariedEmployee(1, "Kunal", 70000), HourlyEmployee(2, "Ritu", 80, 500)]
    for employee in employees:
        print(employee.payslip())


if __name__ == "__main__":
    main()
