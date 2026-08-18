"""Abstract class can contain both abstract and concrete functionality."""

from abc import ABC, abstractmethod

class Repository(ABC):
    def __init__(self):
        self._items = {}

    def save(self, key, value):
        self._items[key] = self.normalize(value)

    def get(self, key):
        return self._items.get(key)

    @abstractmethod
    def normalize(self, value):
        pass

class StringRepository(Repository):
    def normalize(self, value):
        return str(value).strip()

class IntegerRepository(Repository):
    def normalize(self, value):
        return int(value)


def main():
    strings = StringRepository()
    strings.save("course", "  Python  ")
    numbers = IntegerRepository()
    numbers.save("credits", "4")
    print(strings.get("course"))
    print(numbers.get("credits"))


if __name__ == "__main__":
    main()
