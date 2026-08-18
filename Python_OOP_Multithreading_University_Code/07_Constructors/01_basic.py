"""Default and parameterized initialization."""

class Course:
    def __init__(self, code: str = "UNKNOWN", title: str = "Untitled", credits: int = 0):
        self.code = code
        self.title = title
        self.credits = credits

    def __repr__(self):
        return f"Course({self.code!r}, {self.title!r}, credits={self.credits})"


def main():
    print(Course())
    print(Course("202044504", "Programming with Python", 4))


if __name__ == "__main__":
    main()
