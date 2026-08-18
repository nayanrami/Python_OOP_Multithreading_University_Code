"""Custom iterator implementing the iterator protocol."""

class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def main():
    for value in Countdown(5):
        print(value, end=" ")
    print()


if __name__ == "__main__":
    main()
