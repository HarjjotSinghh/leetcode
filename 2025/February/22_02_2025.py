import re


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class Solution:
    def __init__(self):
        self.index = 0

    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        return self.helper(traversal, 0)

    def helper(self, traversal, depth):
        if self.index >= len(traversal):
            return None
        dash_count = 0
        while (
            self.index + dash_count < len(traversal)
            and traversal[self.index + dash_count] == "-"
        ):
            dash_count += 1
        if dash_count != depth:
            return None
        self.index += dash_count
        value = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            value = value * 10 + int(traversal[self.index])
            self.index += 1
        node = TreeNode(value)
        node.left = self.helper(traversal, depth + 1)
        node.right = self.helper(traversal, depth + 1)
        return node


# Best / Most Optimal Solution
class Solution2:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        dash_map = {}
        dash_cnt = 0
        first_num = ""
        for ch in S:
            if ch == "-":
                break
            first_num += ch
        dash_map[0] = TreeNode(int(first_num))
        s = re.findall(r"(-+)(\d+)", S)
        for dash, num in s:
            dash_num = len(dash)
            num = int(num)
            n = TreeNode(num)
            fa = dash_map[dash_num - 1]
            if not fa.left:
                fa.left = n
            elif not fa.right:
                fa.right = n
            dash_map[dash_num] = n
        return dash_map[0]
