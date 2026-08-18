"""LeetCode 155-inspired: Min Stack.

Encapsulation keeps the two internal stacks consistent.
"""

class MinStack:
    def __init__(self):
        self._values = []
        self._minimums = []

    def push(self, val: int) -> None:
        self._values.append(val)
        new_min = val if not self._minimums else min(val, self._minimums[-1])
        self._minimums.append(new_min)

    def pop(self) -> None:
        self._values.pop()
        self._minimums.pop()

    def top(self) -> int:
        return self._values[-1]

    def getMin(self) -> int:
        return self._minimums[-1]


def main():
    stack = MinStack()
    for value in [5, 2, 7, 1]:
        stack.push(value)
        print("push", value, "min =", stack.getMin())
    stack.pop()
    print("after pop, top =", stack.top(), "min =", stack.getMin())


if __name__ == "__main__":
    main()
