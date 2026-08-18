"""LeetCode 225-inspired stack implementation through an abstract collection."""

from abc import ABC, abstractmethod
from collections import deque

class StackInterface(ABC):
    @abstractmethod
    def push(self, x: int) -> None:
        pass

    @abstractmethod
    def pop(self) -> int:
        pass

    @abstractmethod
    def top(self) -> int:
        pass

    @abstractmethod
    def empty(self) -> bool:
        pass

class MyStack(StackInterface):
    def __init__(self):
        self._queue = deque()

    def push(self, x: int) -> None:
        self._queue.append(x)
        for _ in range(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return not self._queue


def main():
    s = MyStack()
    s.push(10)
    s.push(20)
    print(s.top(), s.pop(), s.empty())


if __name__ == "__main__":
    main()
