"""LeetCode 232-inspired: Implement Queue using Stacks.

The queue's internal stacks are treated as implementation details.
"""

class MyQueue:
    def __init__(self):
        self._incoming = []
        self._outgoing = []

    def _shift(self):
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())

    def push(self, x: int) -> None:
        self._incoming.append(x)

    def pop(self) -> int:
        self._shift()
        return self._outgoing.pop()

    def peek(self) -> int:
        self._shift()
        return self._outgoing[-1]

    def empty(self) -> bool:
        return not self._incoming and not self._outgoing


def main():
    q = MyQueue()
    q.push(10)
    q.push(20)
    print(q.peek())
    print(q.pop())
    print(q.empty())


if __name__ == "__main__":
    main()
