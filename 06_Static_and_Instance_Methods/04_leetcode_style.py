"""LeetCode 622-inspired: Design Circular Queue.

A class method creates a queue from an iterable; a static method validates
capacity. These additions are educational.
"""

class MyCircularQueue:
    def __init__(self, k: int):
        if not self.valid_capacity(k):
            raise ValueError("capacity must be positive")
        self.data = [None] * k
        self.capacity = k
        self.front = 0
        self.count = 0

    @staticmethod
    def valid_capacity(k: int) -> bool:
        return isinstance(k, int) and k > 0

    @classmethod
    def from_values(cls, capacity: int, values):
        queue = cls(capacity)
        for value in values:
            if not queue.enQueue(value):
                break
        return queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        index = (self.front + self.count) % self.capacity
        self.data[index] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.front + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


def main():
    q = MyCircularQueue.from_values(3, [10, 20, 30, 40])
    print(q.Front(), q.Rear(), q.isFull())
    q.deQueue()
    q.enQueue(40)
    print(q.Front(), q.Rear())


if __name__ == "__main__":
    main()
