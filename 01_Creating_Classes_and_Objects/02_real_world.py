"""Real-world object interaction: library books and members."""

class Book:
    def __init__(self, isbn: str, title: str):
        self.isbn = isbn
        self.title = title
        self.borrowed_by = None

    @property
    def available(self) -> bool:
        return self.borrowed_by is None

    def issue_to(self, member) -> bool:
        if not self.available:
            return False
        self.borrowed_by = member
        member.borrowed_books.append(self)
        return True

    def return_book(self) -> None:
        if self.borrowed_by:
            self.borrowed_by.borrowed_books.remove(self)
            self.borrowed_by = None


class Member:
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def show_books(self) -> None:
        titles = [book.title for book in self.borrowed_books]
        print(f"{self.name}'s books: {titles}")


def main():
    book = Book("978-001", "Python Fundamentals")
    member = Member(1, "Meera")

    print("Issued:", book.issue_to(member))
    member.show_books()
    print("Available:", book.available)

    book.return_book()
    member.show_books()
    print("Available after return:", book.available)


if __name__ == "__main__":
    main()
