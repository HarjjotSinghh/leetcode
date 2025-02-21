from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen

    def dfs(self, current_node, current_value):
        if current_node is None:
            return
        self.seen.add(current_value)
        self.dfs(current_node.left, current_value * 2 + 1)
        self.dfs(current_node.right, current_value * 2 + 2)


# Best / Most Optimal Solution
class FindElements2:
    def __init__(self, root: Optional[TreeNode]):
        def dfs(node, val):
            if not node:
                return
            self.vals.add(val)
            dfs(node.left, 2 * val + 1)
            dfs(node.right, 2 * val + 2)

        self.vals = set()
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals
