# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution(object):
    def bstToGst(self, root):
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ
        total = 0
        node = root
        while node is not None:
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_successor(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root
    
# Best / Most Optimal Solution
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        su = 0
        def rec(curr:TreeNode):
            nonlocal su
            if curr.right:
                rec(curr.right)
            su += curr.val
            curr.val = su
            if curr.left:
                rec(curr.left)
        rec(root)
        return root
