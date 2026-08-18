"""Traditional getter and setter functions."""

class Student:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = 0
        self.set_age(age)

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if not 15 <= age <= 100:
            raise ValueError("age must be between 15 and 100")
        self._age = age


def main():
    student = Student("Jiya", 20)
    print(student.get_age())
    student.set_age(21)
    print(student.get_age())


if __name__ == "__main__":
    main()
