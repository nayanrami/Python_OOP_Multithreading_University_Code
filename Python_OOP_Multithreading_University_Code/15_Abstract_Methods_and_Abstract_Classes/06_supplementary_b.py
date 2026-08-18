"""Supplement: abstract transport."""

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def fare(self, distance): pass

class Bus(Transport):
    def fare(self, distance):
        return distance * 2

if __name__ == "__main__":
    print(Bus().fare(15))
