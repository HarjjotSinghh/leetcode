from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution:
    def _post_order(self, currentNode: Optional[TreeNode], distance: int) -> int:
        if currentNode is None:
            return [0] * 12
        elif currentNode.left is None and currentNode.right is None:
            current = [0] * 12
            current[0] = 1
            return current
        left = self._post_order(currentNode.left, distance)
        right = self._post_order(currentNode.right, distance)
        current = [0] * 12
        for i in range(10):
            current[i + 1] += left[i] + right[i]
        current[11] = left[11] + right[11]
        for d1 in range(distance + 1):
            for d2 in range(distance + 1):
                if 2 + d1 + d2 <= distance:
                    current[11] += left[d1] * right[d2]
        return current
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self._post_order(root, distance)[11]
    
# Best / Most Optimal Solution
class Solution2:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        def solve(root):
            if root is None:
                return {}
            if root.left is None and root.right is None:
                return {1: 1}
            lhNodes = solve(root.left)            
            rhNodes = solve(root.right)
            for leftNodeHeight in lhNodes:
                for rightNodeHeight in rhNodes:
                    if leftNodeHeight + rightNodeHeight <= distance:
                        self.res += lhNodes[leftNodeHeight] * rhNodes[rightNodeHeight]
            nhNodes = {}
            for key in lhNodes:
                if key <= distance:
                    nhNodes[key + 1] = lhNodes[key]
            for key in rhNodes:
                if key <= distance:
                    nhNodes[key + 1] = nhNodes.get(key + 1, 0) + rhNodes[key]                    
            return nhNodes
        solve(root)
        return self.res
