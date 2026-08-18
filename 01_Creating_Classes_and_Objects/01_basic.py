"""Basic class and object demonstration."""

class Student:
    college = "A. D. Patel Institute of Technology"   # class attribute

    def __init__(self, roll_no: int, name: str, marks: float):
        self.roll_no = roll_no      # instance attributes
        self.name = name
        self.marks = marks

    def display(self) -> None:
        print(f"{self.roll_no}: {self.name} -> {self.marks:.1f}")

    def has_passed(self, passing_marks: float = 40) -> bool:
        return self.marks >= passing_marks


def main():
    s1 = Student(101, "Aarav", 78.5)
    s2 = Student(102, "Diya", 36.0)

    # Objects of the same class contain independent instance state.
    s1.display()
    s2.display()
    print("Same college:", s1.college == s2.college)
    print("Aarav passed:", s1.has_passed())
    print("Diya passed:", s2.has_passed())


if __name__ == "__main__":
    main()
