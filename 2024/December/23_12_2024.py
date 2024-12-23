from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class Solution:
    _SHIFT = 20
    _MASK = 0xFFFFF

    def minimumOperations(self, root: Optional["TreeNode"]) -> int:
        queue = deque([root])
        swaps = 0
        while queue:
            level_size = len(queue)
            nodes = []
            for i in range(level_size):
                node = queue.popleft()
                nodes.append((node.val << self._SHIFT) + i)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nodes.sort()
            i = 0
            while i < level_size:
                orig_pos = nodes[i] & self._MASK
                if orig_pos != i:
                    nodes[i], nodes[orig_pos] = nodes[orig_pos], nodes[i]
                    swaps += 1
                    i -= 1
                i += 1
        return swaps


# Best / Most Optimal Solution
class Solution2:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            a = []
            for _ in range(len(q)):
                node = q.popleft()
                a.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            n = len(a)
            a = sorted(range(n), key=lambda i: a[i])
            vis = [False] * n
            ans += n
            for v in a:
                if vis[v]:
                    continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                ans -= 1
        return ans
