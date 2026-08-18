"""Supplement: algorithm abstraction."""

from abc import ABC, abstractmethod

class Sorter(ABC):
    @abstractmethod
    def sort(self, values): pass

class BuiltinSorter(Sorter):
    def sort(self, values):
        return sorted(values)

def report(sorter, values):
    print(sorter.sort(values))

if __name__ == "__main__":
    report(BuiltinSorter(), [4, 1, 3])
