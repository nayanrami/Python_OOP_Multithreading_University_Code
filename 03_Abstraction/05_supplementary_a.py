"""Supplement: storage abstraction."""

from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def write(self, key, value): pass
    @abstractmethod
    def read(self, key): pass

class MemoryStorage(Storage):
    def __init__(self):
        self.data = {}
    def write(self, key, value):
        self.data[key] = value
    def read(self, key):
        return self.data.get(key)

if __name__ == "__main__":
    s = MemoryStorage()
    s.write("x", 42)
    print(s.read("x"))
