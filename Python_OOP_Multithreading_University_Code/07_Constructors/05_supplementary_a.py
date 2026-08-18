"""Supplement: alternate constructor from string."""

class Date:
    def __init__(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    @classmethod
    def from_iso(cls, text):
        y, m, d = map(int, text.split("-"))
        return cls(d, m, y)

if __name__ == "__main__":
    d = Date.from_iso("2026-08-18")
    print(d.day, d.month, d.year)
