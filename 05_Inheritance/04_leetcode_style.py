"""LeetCode 707-inspired: Design Linked List with node inheritance.

Inheritance is not required by the original problem; it is used here to teach
how a specialized node can extend a reusable node model.
"""

class BaseNode:
    def __init__(self, value: int):
        self.value = value

class ListNode(BaseNode):
    def __init__(self, value: int, next_node=None):
        super().__init__(value)
        self.next = next_node

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size += 1

    def get(self, index: int) -> int:
        if not 0 <= index < self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value


def main():
    linked = MyLinkedList()
    linked.addAtHead(10)
    linked.addAtHead(20)
    print(linked.get(0), linked.get(1), linked.get(2))


if __name__ == "__main__":
    main()
