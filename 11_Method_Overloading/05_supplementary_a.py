"""Supplement: keyword-driven overload-like behavior."""

class Greeting:
    def greet(self, name, title=None):
        return f"Hello, {title + ' ' if title else ''}{name}"

if __name__ == "__main__":
    g = Greeting()
    print(g.greet("Riya"))
    print(g.greet("Riya", "Dr."))
