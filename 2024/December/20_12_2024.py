from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
class Solution:
    def reverseOddLevels(self, root) -> TreeNode:
        self.__traverse_DFS(root.left, root.right, 0)
        return root
    def __traverse_DFS(self, left_child, right_child, level):
        if left_child is None or right_child is None:
            return
        if level % 2 == 0:
            temp = left_child.val
            left_child.val = right_child.val
            right_child.val = temp
        self.__traverse_DFS(left_child.left, right_child.right, level + 1)
        self.__traverse_DFS(left_child.right, right_child.left, level + 1)
        
# Best / Most Optimal Solution
class Solution2:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        def traverse(leftNode, rightNode, level):
            if leftNode is None or rightNode is None:
                return
            if (level % 2 != 0):
                leftNode.val, rightNode.val = rightNode.val, leftNode.val
            traverse(leftNode.left, rightNode.right,  level+1)
            traverse(leftNode.right, rightNode.left, level+1)
        traverse(root.left, root.right, 1)
        return root
