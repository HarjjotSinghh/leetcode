from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class Solution2:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        no_swap = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(
            root1.right, root2.right
        )
        swap = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(
            root1.right, root2.left
        )
        return no_swap or swap


# Best / Most Optimal Solution
class Solution2:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        left_res = self.flipEquiv(root1.left, root2.left)
        if left_res:
            right_res = self.flipEquiv(root1.right, root2.right)
        else:
            left_res = self.flipEquiv(root1.left, root2.right)
            if left_res:
                right_res = self.flipEquiv(root1.right, root2.left)
            else:
                return False
        return left_res and right_res
