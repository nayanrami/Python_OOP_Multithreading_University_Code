"""Supplement: custom equality."""

class Book:
    def __init__(self, isbn):
        self.isbn = isbn

    def __eq__(self, other):
        return isinstance(other, Book) and self.isbn == other.isbn

if __name__ == "__main__":
    print(Book("A") == Book("A"))
    print(Book("A") == Book("B"))
