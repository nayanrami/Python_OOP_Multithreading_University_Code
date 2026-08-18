"""Instance, class and static methods side by side."""

class Student:
    university = "CVM University"
    count = 0

    def __init__(self, name: str, marks: float):
        self.name = name
        self.marks = marks
        Student.count += 1

    def display(self):                         # instance method
        return f"{self.name}: {self.marks}"

    @classmethod
    def total_students(cls):                   # class method
        return cls.count

    @staticmethod
    def valid_marks(marks):                    # static method
        return 0 <= marks <= 100


def main():
    print(Student.valid_marks(88))
    s1 = Student("Aditi", 88)
    s2 = Student("Parth", 91)
    print(s1.display())
    print(s2.display())
    print(Student.total_students())


if __name__ == "__main__":
    main()
