"""Supplement: encapsulated exam result."""

class ExamResult:
    def __init__(self, marks):
        self.__marks = None
        self.update(marks)

    def update(self, marks):
        if not 0 <= marks <= 100:
            raise ValueError("marks out of range")
        self.__marks = marks

    def grade(self):
        return "A" if self.__marks >= 80 else "B" if self.__marks >= 60 else "C"

if __name__ == "__main__":
    r = ExamResult(84)
    print(r.grade())
