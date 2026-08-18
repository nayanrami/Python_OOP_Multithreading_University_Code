"""LeetCode 146-inspired cache programmed against an interface."""

from abc import ABC, abstractmethod
from collections import OrderedDict

class Cache(ABC):
    @abstractmethod
    def get(self, key: int) -> int:
        pass

    @abstractmethod
    def put(self, key: int, value: int) -> None:
        pass

class LRUCache(Cache):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._data = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._data:
            return -1
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key: int, value: int) -> None:
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)

def use_cache(cache: Cache):
    cache.put(1, 100)
    cache.put(2, 200)
    print(cache.get(1))


def main():
    use_cache(LRUCache(2))


if __name__ == "__main__":
    main()
