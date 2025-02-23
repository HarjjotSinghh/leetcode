from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution
class Solution:
    def __init__(self):
        self.pre_index = 0
        self.post_index = 0

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        return self._construct_tree(preorder, postorder)

    def _construct_tree(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1
        if root.val != postorder[self.post_index]:
            root.left = self._construct_tree(preorder, postorder)
        if root.val != postorder[self.post_index]:
            root.right = self._construct_tree(preorder, postorder)
        self.post_index += 1
        return root


# Best / Most Optimal Solution
class Solution2:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not postorder:
            return None
        val = postorder.pop()
        node = TreeNode(val)
        if not postorder:
            return node
        i = postorder.index(preorder[1])
        node.left = self.constructFromPrePost(preorder[1 : i + 2], postorder[: i + 1])
        node.right = self.constructFromPrePost(preorder[i + 2 :], postorder[i + 1 :])
        return node
