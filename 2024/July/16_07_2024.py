from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution:
    def getDirections(
        self, root: TreeNode, startValue: int, destValue: int
    ) -> str:
        start_path = []
        dest_path = []
        self._find_path(root, startValue, start_path)
        self._find_path(root, destValue, dest_path)
        directions = []
        common_path_length = 0
        while (
            common_path_length < len(start_path)
            and common_path_length < len(dest_path)
            and start_path[common_path_length] == dest_path[common_path_length]
        ):
            common_path_length += 1
        directions.extend("U" * (len(start_path) - common_path_length))
        directions.extend(dest_path[common_path_length:])
        return "".join(directions)
    def _find_path(self, node: TreeNode, target: int, path: List[str]) -> bool:
        if node is None:
            return False
        if node.val == target:
            return True
        path.append("L")
        if self._find_path(node.left, target, path):
            return True
        path.pop()
        path.append("R")
        if self._find_path(node.right, target, path):
            return True
        path.pop()
        return False

# Best / Most Optimal Solution
class Solution2:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def find(node, val, path):
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path.append('L')
                return True
            if node.right and find(node.right, val, path):
                path.append('R')
                return True
            return False
        p1 = []
        p2 = []
        find(root, startValue, p1)
        find = find(root, destValue, p2)
        while p1 and p2 and p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()
        return 'U' * len(p1) + ''.join(p2[::-1])
