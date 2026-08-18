"""Supplement: Python does not keep earlier same-name definitions."""

class Demo:
    def show(self):
        return "second definition replaces first"

if __name__ == "__main__":
    print(Demo().show())
