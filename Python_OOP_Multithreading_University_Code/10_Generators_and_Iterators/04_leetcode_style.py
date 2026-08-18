"""LeetCode 173-inspired: Binary Search Tree Iterator."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode | None):
        self._stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self._stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self._stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self._stack)


def main():
    root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
    iterator = BSTIterator(root)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    print(result)


if __name__ == "__main__":
    main()
