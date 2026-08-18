"""Overriding a special method and a normal method."""

class Document:
    def __init__(self, title):
        self.title = title

    def render(self):
        return self.title

    def __str__(self):
        return f"Document<{self.title}>"

class MarkdownDocument(Document):
    def render(self):
        return f"# {super().render()}"

    def __str__(self):
        return f"MarkdownDocument<{self.title}>"


def main():
    document = MarkdownDocument("OOP Notes")
    print(document.render())
    print(document)


if __name__ == "__main__":
    main()
