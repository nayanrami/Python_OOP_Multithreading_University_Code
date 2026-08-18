"""Sortable Student objects."""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return f"Student({self.name!r}, marks={self.marks})"


def main():
    students = [Student("Nisha", 91), Student("Raj", 72), Student("Devanshi", 84)]
    print(sorted(students))
    print("Length of first student's name:", len(students[0]))


if __name__ == "__main__":
    main()
