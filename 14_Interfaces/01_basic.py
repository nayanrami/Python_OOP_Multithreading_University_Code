"""Interface-like contract with ABC."""

from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_data(self) -> None:
        pass

class Invoice(Printable):
    def __init__(self, number):
        self.number = number

    def print_data(self):
        print(f"Invoice #{self.number}")


def main():
    Invoice("INV-101").print_data()


if __name__ == "__main__":
    main()
