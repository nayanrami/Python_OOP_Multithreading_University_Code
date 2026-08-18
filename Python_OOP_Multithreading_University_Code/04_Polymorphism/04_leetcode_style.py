"""LeetCode-style tree processing using polymorphic visitors.

This is an educational design example rather than a copied problem statement.
"""

class NodeOperation:
    def apply(self, value: int):
        raise NotImplementedError

class SumOperation(NodeOperation):
    def __init__(self):
        self.result = 0

    def apply(self, value):
        self.result += value

class MaxOperation(NodeOperation):
    def __init__(self):
        self.result = float("-inf")

    def apply(self, value):
        self.result = max(self.result, value)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def traverse(root: TreeNode | None, operation: NodeOperation):
    if root is None:
        return
    traverse(root.left, operation)
    operation.apply(root.value)
    traverse(root.right, operation)


def main():
    root = TreeNode(4, TreeNode(2), TreeNode(9))
    for operation in [SumOperation(), MaxOperation()]:
        traverse(root, operation)
        print(type(operation).__name__, operation.result)


if __name__ == "__main__":
    main()
