"""LRU-cache-style example with an overridden cache hook.

The data structure is inspired by LeetCode 146; inheritance is added to teach
method overriding.
"""

from collections import OrderedDict

class BaseCache:
    def on_hit(self, key):
        pass

    def on_miss(self, key):
        pass

class LRUCache(BaseCache):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data:
            self.on_miss(key)
            return -1
        self.data.move_to_end(key)
        self.on_hit(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)

class InstrumentedLRUCache(LRUCache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.hits = 0
        self.misses = 0

    def on_hit(self, key):
        self.hits += 1

    def on_miss(self, key):
        self.misses += 1


def main():
    cache = InstrumentedLRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    print(cache.get(1))
    print(cache.get(99))
    print("hits:", cache.hits, "misses:", cache.misses)


if __name__ == "__main__":
    main()
