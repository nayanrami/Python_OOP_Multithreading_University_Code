"""Supplement: incomplete subclass cannot be instantiated."""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def run(self): pass

class B(A):
    def run(self):
        return "running"

if __name__ == "__main__":
    print(B().run())
