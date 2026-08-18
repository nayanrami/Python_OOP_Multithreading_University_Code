"""Single inheritance."""

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I am {self.name}, age {self.age}"

class Student(Person):
    def __init__(self, name: str, age: int, enrollment_no: str):
        super().__init__(name, age)
        self.enrollment_no = enrollment_no

    def study(self):
        return f"{self.name} is studying"


def main():
    student = Student("Anaya", 19, "IT2026001")
    print(student.introduce())
    print(student.study())


if __name__ == "__main__":
    main()
